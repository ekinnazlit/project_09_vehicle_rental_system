
from storage import load_state
from reports import revenue_summary

vehicles, customers, reservations = load_state("data")

period = ("2026-11-01", "2026-11-30")

revenue = revenue_summary(reservations, period)

print("MONTHLY REVENUE REPORT")

for month, total in revenue.items():
    print(month, ":", total, "TL")

from reports import utilization_report

period = ("2026-11-01", "2026-12-01")

utilization = utilization_report(
    reservations,
    vehicles,
    period
)

print("\nVEHICLE UTILIZATION REPORT")

for vehicle_id, percentage in utilization.items():
    print(vehicle_id, ":", percentage, "%")

from reports import upcoming_returns

returns = upcoming_returns(reservations, "2026-11-01")

print("\nUPCOMING RETURNS")

for r in returns:
    print(r["id"], "-", r["vehicle_id"], "-", r["end_date"])

if not returns:
    print("No upcoming returns")



test_reservations = [
    {
        "id": "R-101",
        "vehicle_id": "V-1",
        "status": "active",
        "end_date": "2026-11-03"
    },
    {
        "id": "R-102",
        "vehicle_id": "V-1",
        "status": "active",
        "end_date": "2026-11-06"
    },
    {
        "id": "R-103",
        "vehicle_id": "V-1",
        "status": "active",
        "end_date": "2026-11-15"
    },
    {
        "id": "R-104",
        "vehicle_id": "V-1",
        "status": "cancelled",
        "end_date": "2026-11-04"
    }
]

upcoming = upcoming_returns(
    test_reservations,
    "2026-11-01",
    days_ahead=7
)

print("\nUPCOMING RETURNS TEST")

for r in upcoming:
    print(r["id"], "-", r["end_date"])



from reports import export_report

report_data = {
    "2026-11": 7205.0
}

filename = export_report(
    report_data,
    "test_revenue_report.json"
)

print("\nEXPORT REPORT TEST")
print("Report saved to:", filename)
