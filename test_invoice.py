
from reservations import calculate_invoice

reservation = {
    "rental_days": 5
}

vehicle = {
    "daily_price": 1000,
    "rate_per_km": 5
}

invoice = calculate_invoice(
    reservation,
    vehicle,
    actual_mileage=250
)

print("INVOICE RESULT")
print("Rental cost:", invoice["rental_cost"])
print("Mileage cost:", invoice["mileage_cost"])
print("Insurance:", invoice["insurance_fee"])
print("Tax:", invoice["tax"])
print("Total:", invoice["total"])
