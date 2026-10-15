def main():
    print("Vehicle Rental Management System")
    print("Welcome!")



from reservations import create_reservation

vehicles = [
    {
        "id": "CAR001",
        "daily_price": 500,
        "status": "available"
    }
]

reservations = []

reservation_data = {
    "vehicle_id": "CAR001",
    "customer_id": "C001",
    "start_date": "2026-11-01",
    "end_date": "2026-11-04",
    "pickup": "Istanbul",
    "return": "Istanbul",
    "estimated_mileage": -50
}

try:
    create_reservation(reservations, reservation_data, vehicles)
except ValueError as e:
    print("Error:", e)
