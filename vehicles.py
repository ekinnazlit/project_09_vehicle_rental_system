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
    if vehicle_data["brand"].strip() == "":
        raise ValueError("Brand cannot be empty")

    if vehicle_data["model"].strip() == "":
        raise ValueError("Model cannot be empty")

    if not isinstance(vehicle_data["year"], int):
        raise ValueError("Year must be a number")

    if vehicle_data["year"] < 1990 or vehicle_data["year"] > 2029:
        raise ValueError("Vehicle year must be between 1990 and 2029")

    allowed_types = ["sedan", "suv", "hatchback", "van"]

    vehicle_type = vehicle_data["type"].lower()

    if vehicle_type not in allowed_types:
        raise ValueError("Invalid vehicle type")
    vehicle_data["type"] = vehicle_type

    if not isinstance(vehicle_data["daily_price"], (int, float)):
        raise ValueError("Daily price must be a number")

    if vehicle_data["daily_price"] <= 0:
        raise ValueError("Daily price must be greater than zero")

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

