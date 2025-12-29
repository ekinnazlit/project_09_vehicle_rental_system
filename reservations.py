from datetime import datetime

def _overlap(s1, e1, s2, e2):
    return not (e1 < s2 or s1 > e2)

def check_availability(reservations: list, vehicle_id: str,
                       start_date: str, end_date: str) -> bool:
    for r in reservations:
        if r["vehicle_id"] == vehicle_id and r["status"] == "active":
            if _overlap(r["start_date"], r["end_date"], start_date, end_date):
                return False
    return True

def create_reservation(reservations: list, reservation_data: dict,
                       vehicles: list) -> dict:
    if not check_availability(
        reservations,
        reservation_data["vehicle_id"],
        reservation_data["start_date"],
        reservation_data["end_date"]
    ):
        raise ValueError("Vehicle not available")

    reservation = {
        "id": f"R-{len(reservations)+1}",
        "status": "active",
        "checkout": None,
        "checkin": None,
        "invoice": None
    }
    reservation.update(reservation_data)
    reservations.append(reservation)
    return reservation

def cancel_reservation(reservations: list, reservation_id: str) -> bool:
    for r in reservations:
        if r["id"] == reservation_id and r["status"] == "active":
            r["status"] = "cancelled"
            return True
    return False

def calculate_invoice(reservation: dict, pricing_rules: dict) -> dict:
    days = pricing_rules["days"]
    base = days * pricing_rules["rate_per_day"]
    mileage = reservation["estimated_mileage"] * pricing_rules["rate_per_km"]
    insurance = pricing_rules.get("insurance", 0)
    tax = (base + mileage + insurance) * pricing_rules["tax_rate"]

    return {
        "base": base,
        "mileage": mileage,
        "insurance": insurance,
        "tax": tax,
        "total": base + mileage + insurance + tax
    }

def complete_rental(reservations: list, reservation_id: str,
                    return_data: dict, vehicles: list) -> dict:
    for r in reservations:
        if r["id"] == reservation_id and r["status"] == "active":
            r["checkin"] = return_data
            r["status"] = "completed"
            return r
    raise ValueError("Reservation not active")

