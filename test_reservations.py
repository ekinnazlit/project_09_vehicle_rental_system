

from reservations import create_reservation

vehicles = [
    {
        "id": "CAR001",
        "brand": "BMW",
        "model": "320i",
        "daily_price": 1000,
        "status": "available"
    }
]

reservations = []

reservation_data = {
    "vehicle_id": "CAR001",
    "customer_id": "C001",
    "start_date": "2026-11-10",
    "end_date": "2026-11-15",
    "pickup": "Istanbul",
    "return": "Istanbul",
    "estimated_mileage": 250
}

reservation = create_reservation(
    reservations,
    reservation_data,
    vehicles
)

print("Reservation created!")
print("Reservation ID:", reservation["id"])
print("Rental days:", reservation["rental_days"])
print("Estimated price:", reservation["estimated_price"])


second_reservation = {
    "vehicle_id": "CAR001",
    "customer_id": "C002",
    "start_date": "2026-11-12",
    "end_date": "2026-11-18",
    "pickup": "Istanbul",
    "return": "Istanbul",
    "estimated_mileage": 100
}

try:
    create_reservation(
        reservations,
        second_reservation,
        vehicles
    )
    print("Second reservation created!")

except ValueError as error:
    print("Error:", error)


