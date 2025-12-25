{
  "id": "51 EA 192",
  "vehicle_id": "F10 520i",
  "start_date": "2025-04-17",
  "end_date": "2025-04-17",
  "status": "active",
  "invoice": {
      "total": 57350
  }
}
import json
from datetime import datetime
def days_between(start: str, end: str) -> int:
    d1 = datetime.strptime(start, "%Y-%m-%d")
    d2 = datetime.strptime(end, "%Y-%m-%d")
    return (d2 - d1).days + 1
def utilization_report(reservations: list,
                       vehicles: list,
                       period: tuple[str, str]) -> dict:
    period_start, period_end = period
    total_period_days = days_between(period_start, period_end)

    utilization = {}

    for v in vehicles:
        rented_days = 0

        for r in reservations:
            if r["vehicle_id"] == v["id"] and r["status"] == "completed":
                start = max(r["start_date"], period_start)
                end = min(r["end_date"], period_end)

                if start <= end:
                    rented_days += days_between(start, end)

        utilization[v["id"]] = round(
            (rented_days / total_period_days) * 100, 2
        )

    return utilization
def export_report(report: dict, filename: str) -> str:
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)
    return filename


