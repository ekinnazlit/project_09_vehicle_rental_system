
import vehicle
FILENAME = "vehicles.json"
vehicles = vehicle.load_vehicles(FILENAME)
vehicle.add_vehicle(vehicles, {
    "model": "Kamiq",
    "year": 2024
})

vehicle.save_vehicles(FILENAME, vehicles)
print("Available Vehicles:")
for v in vehicle.list_available_vehicles(vehicles):
    print(v)
