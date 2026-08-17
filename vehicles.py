import json
import os

def load_vehicles(path: str) -> list:
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

def save_vehicles(path: str, vehicles: list) -> None:
    with open(path, "w") as f:
        json.dump(vehicles, f, indent=2)

def add_vehicle(vehicles: list, vehicle_data: dict) -> dict:
    numbers = []

    for v in vehicles:
        number = int(v["id"].replace("V-", ""))
        numbers.append(number)

    if len(vehicles) == 0:
        next_id = 1
    else:
        next_id = max(numbers) + 1

    vehicle = {
        "id": f"V-{next_id}",
        "status": "available",
        "maintenance": []
    }

    vehicle.update(vehicle_data)
    vehicles.append(vehicle)
    return vehicle

def update_vehicle(vehicles: list, vehicle_id: str, updates: dict) -> dict:
    for v in vehicles:
        if v["id"] == vehicle_id:
            v.update(updates)
            return v
    raise ValueError("Vehicle not found")

def set_vehicle_status(vehicles: list, vehicle_id: str, status: str) -> dict:
    for v in vehicles:
        if v["id"] == vehicle_id:
            v["status"] = status
            return v
    raise ValueError("Vehicle not found")

def list_available_vehicles(
    vehicles: list,
    rental_dates: tuple[str, str],
    vehicle_type: str | None = None
) -> list:
    result = []
    for v in vehicles:
        if v["status"] != "available":
            continue
        if vehicle_type and v["type"] != vehicle_type:
            continue
        result.append(v)
    return result

