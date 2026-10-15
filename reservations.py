import uuid
from datetime import datetime

def create_reservation(reservations: list, reservation_data: dict, vehicles: list) -> dict:

    required = [
        "vehicle_id", "customer_id",
        "start_date", "end_date",
        "pickup", "return",
        "estimated_mileage",
    ]

    for field in required:
        if field not in reservation_data:
            raise ValueError(f"Missing field: {field}")

    start = datetime.strptime(reservation_data["start_date"], "%Y-%m-%d")
    end = datetime.strptime(reservation_data["end_date"], "%Y-%m-%d")

    if start >= end:
        raise ValueError("Start date must be before end date")

    vehicle = next(
        (v for v in vehicles if v["id"] == reservation_data["vehicle_id"]),
        None
    )

    if not vehicle:
        raise ValueError("Vehicle not found")

    if vehicle["status"] != "available":
        raise ValueError("Vehicle is not available")


    for r in reservations:
        if (
            r["vehicle_id"] == reservation_data["vehicle_id"]
            and r["status"] != "cancelled"
        ):
            existing_start = datetime.strptime(
                r["start_date"], "%Y-%m-%d"
            )
            existing_end = datetime.strptime(
                r["end_date"], "%Y-%m-%d"
            )

            if start < existing_end and end > existing_start:
                raise ValueError(
                    "Vehicle already reserved in this period"
                )

    if (
        isinstance(reservation_data["estimated_mileage"], bool)
        or not isinstance(
            reservation_data["estimated_mileage"], (int, float)
        )
    ):
        raise ValueError("Estimated mileage must be a number")

    if reservation_data["estimated_mileage"] < 0:
        raise ValueError("Estimated mileage cannot be negative")

    rental_days = (end - start).days
    estimated_price = rental_days * vehicle["daily_price"]
    reservation = {
        "id": str(uuid.uuid4())[:8],
        "vehicle_id": reservation_data["vehicle_id"],
        "customer_id": reservation_data["customer_id"],
        "start_date": reservation_data["start_date"],
        "end_date": reservation_data["end_date"],
        "pickup": reservation_data["pickup"],
        "return": reservation_data["return"],
        "estimated_mileage": reservation_data["estimated_mileage"],
        "status": "active",
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "rental_days": rental_days,
        "estimated_price": estimated_price,
    }

    reservations.append(reservation)
    return reservation


def cancel_reservation(reservations: list, reservation_id: str) -> dict:
    for r in reservations:
        if r["id"] == reservation_id:

            if r["status"] != "active":
                raise ValueError("Only active reservations can be cancelled")

            r["status"] = "cancelled"
            return r

    raise ValueError("Reservation not found")


def calculate_invoice(
    reservation: dict,
    vehicle: dict,
    actual_mileage: float,
    insurance_fee: float = 300,
    tax_rate: float = 0.10
) -> dict:

    if actual_mileage < 0:
        raise ValueError("Mileage cannot be negative")

    if insurance_fee < 0:
        raise ValueError("Insurance fee cannot be negative")

    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1")

    rental_cost = (
        reservation["rental_days"] * vehicle["daily_price"]
    )

    mileage_cost = (
        actual_mileage * vehicle["rate_per_km"]
    )

    subtotal = rental_cost + mileage_cost + insurance_fee
    tax = subtotal * tax_rate
    total = subtotal + tax

    invoice = {
        "rental_cost": round(rental_cost, 2),
        "mileage_cost": round(mileage_cost, 2),
        "insurance_fee": round(insurance_fee, 2),
        "subtotal": round(subtotal, 2),
        "tax": round(tax, 2),
        "total": round(total, 2)
    }

    return invoice



def complete_rental(
    reservations: list,
    vehicles: list,
    reservation_id: str,
    actual_mileage: float
) -> dict:

    reservation = next(
        (r for r in reservations if r["id"] == reservation_id),
        None
    )

    if reservation is None:
        raise ValueError("Reservation not found")

    if reservation["status"] != "active":
        raise ValueError("Only active reservations can be completed")

    vehicle = next(
        (v for v in vehicles if v["id"] == reservation["vehicle_id"]),
        None
    )

    if vehicle is None:
        raise ValueError("Vehicle not found")

    invoice = calculate_invoice(
        reservation,
        vehicle,
        actual_mileage
    )

    reservation["invoice"] = invoice
    reservation["actual_mileage"] = actual_mileage
    reservation["status"] = "completed"

    return reservation


