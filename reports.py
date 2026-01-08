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


