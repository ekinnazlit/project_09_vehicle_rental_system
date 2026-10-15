import json
from datetime import datetime, timedelta


def utilization_report(reservations: list, vehicles: list, period):
    start, end = period

    period_start = datetime.fromisoformat(start)
    period_end = datetime.fromisoformat(end)

    days_total = (period_end - period_start).days

    if days_total <= 0:
        raise ValueError("End date must be after start date")

    report = {}

    for v in vehicles:
        used = 0

        for r in reservations:
            if (
                r["vehicle_id"] == v["id"]
                and r["status"] == "completed"
            ):
                s = max(start, r["start_date"])
                e = min(end, r["end_date"])

                if s < e:
                    used += (
                        datetime.fromisoformat(e)
                        - datetime.fromisoformat(s)
                    ).days

        report[v["id"]] = round(
            (used / days_total) * 100, 2
        )

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


def upcoming_returns(
    reservations: list,
    reference_date: str,
    days_ahead: int = 7
) -> list:

    if days_ahead < 0:
        raise ValueError("Days ahead cannot be negative")

    start = datetime.fromisoformat(reference_date)
    end = start + timedelta(days=days_ahead)

    result = []

    for r in reservations:
        if r["status"] != "active":
            continue

        return_date = datetime.fromisoformat(r["end_date"])

        if start <= return_date <= end:
            result.append(r)

    return sorted(result, key=lambda r: r["end_date"])


def export_report(report: dict, filename: str) -> str:
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)
    return filename


