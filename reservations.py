import json
from datetime import datetime

def utilization_report(reservations: list, vehicles: list, period):
    start, end = period
    days_total = (datetime.fromisoformat(end) -
                  datetime.fromisoformat(start)).days + 1
    report = {}

    for v in vehicles:
        used = 0
        for r in reservations:
            if r["vehicle_id"] == v["id"] and r["status"] == "completed":
                s = max(start, r["start_date"])
                e = min(end, r["end_date"])
                if s <= e:
                    used += (datetime.fromisoformat(e) -
                             datetime.fromisoformat(s)).days + 1
        report[v["id"]] = round((used / days_total) * 100, 2)

    return report

def revenue_summary(reservations: list, period):
    start, end = period
    revenue = {}

    for r in reservations:
        if r["status"] != "completed":
            continue
        if start <= r["end_date"] <= end:
            month = r["end_date"][:7]
            revenue[month] = revenue.get(month, 0) + r["invoice"]["total"]

    return revenue

def upcoming_returns(reservations: list, reference_date: str) -> list:
    return [
        r for r in reservations
        if r["status"] == "active" and r["end_date"] >= reference_date
    ]

def export_report(report: dict, filename: str) -> str:
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)
    return filename



def create_reservation(reservations: list, reservation_data: dict, vehicles: list) -> dict:

    required = [
        "vehicle_id", "customer_id",
        "start_date", "end_date",
        "pickup", "return",
        "estimated_mileage"
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

    for r in reservations:
        if r["vehicle_id"] == reservation_data["vehicle_id"]:
            existing_start = datetime.strptime(r["start_date"], "%Y-%m-%d")
            existing_end = datetime.strptime(r["end_date"], "%Y-%m-%d")
            if start < existing_end and end > existing_start:
                raise ValueError("Vehicle already reserved in this period")

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
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }

    reservations.append(reservation)
    return reservation


