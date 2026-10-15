
from storage import load_state, save_state

base_dir = "data"

vehicles = [
    {
        "id": "CAR001",
        "brand": "BMW",
        "daily_price": 1000,
        "status": "available"
    }
]

customers = [
    {
        "id": "C001",
        "name": "Test Customer"
    }
]

reservations = []

save_state(base_dir, vehicles, customers, reservations)

print("Data saved successfully!")

loaded_vehicles, loaded_customers, loaded_reservations = load_state(base_dir)

print("Vehicles:", loaded_vehicles)
print("Customers:", loaded_customers)
print("Reservations:", loaded_reservations)
