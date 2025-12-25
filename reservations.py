{
    "id": "51 EA 192",
    "vehicle_id": "F10 520i",
    "start_date": "2025-04-17",
    "end_date": "2025-04-17",
    "pickup": "Istanbul",
    "return": "Istanbul",
    "estimated_mileage": 57000,
    "status": "active",
    "checkout": {
        "odometer": 15000,
        "fuel": 1.6
    },
    "checkin": None
}
def dates_overlap(start1, end1, start2, end2):
    return not (end1 < start2 or start1 > end2)
def check_availability(reservations: list, vehicle_id: str,
                       start_date: str, end_date: str) -> bool:
    for r in reservations:
        if r["vehicle_id"] == vehicle_id and r["status"] == "active":
            if dates_overlap(r["start_date"], r["end_date"],
                             start_date, end_date):
                return False
    return True
def create_reservation(reservations: list, reservation_data: dict,
                       vehicles: list) -> dict:
    vehicle_id = reservation_data["vehicle_id"]

    if not check_availability(reservations,
                              vehicle_id,
                              reservation_data["start_date"],
                              reservation_data["end_date"]):
        raise ValueError("Vehicle is not available for selected dates")

    reservation = {
        "id": f"R-{len(reservations) + 1}",
        "status": "active",
        "checkout": None,
        "checkin": None
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
def complete_rental(reservations: list, reservation_id: str,
                    return_data: dict, vehicles: list) -> dict:
    for r in reservations:
        if r["id"] == reservation_id and r["status"] == "active":
            r["checkin"] = return_data
            r["status"] = "completed"
            return r
    raise ValueError("Reservation not found or already closed")
def calculate_invoice(reservation: dict, pricing_rules: dict) -> dict:
    days = pricing_rules["days"]
    daily_rate = pricing_rules["daily_rate"]
    mileage_rate = pricing_rules["mileage_rate"]
    tax_rate = pricing_rules["tax_rate"]
    insurance = pricing_rules.get("insurance", 0)

    base_cost = days * daily_rate
    mileage_cost = reservation["estimated_mileage"] * mileage_rate

    subtotal = base_cost + mileage_cost + insurance
    tax = subtotal * tax_rate
    total = subtotal + tax

    return {
        "base_cost": base_cost,
        "mileage_cost": mileage_cost,
        "insurance": insurance,
        "tax": tax,
        "total": total
    }
