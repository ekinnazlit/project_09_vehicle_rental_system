import json
def generate_id(vehicles):
    return len(vehicles) +1
def load_vehicles(path: str) -> list:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        print("error")
        return []

def save_vehicles(path:str, vehicles:list) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(vehicles, f, indent=4)
def add_vehicle(vehicles: list, vehicle_data: dict):
    vehicle = {
        "id": generate_id(vehicles),
        "model": vehicle_data["model"],
        "year": vehicle_data["year"],
        "availability": "available",
        "rate_per_day": vehicle_data.get("rate_per_day",0),
        "rate_per_week": vehicle_data.get("rate_per_week",0),
        "rate_per_hour": vehicle_data.get("rate_per_hour",0),
    }
    vehicles.append(vehicle)

    return vehicle
def update_vehicle(vehicles: list, vehicle_id: int, updates: dict) -> dict:
    for v in vehicle:
        if v["id"] == vehicle.id:
            v.update(updates)
            return v
        raise ValueError("Vehicle id not found, please enter another id.")

def list_available_vehicles(
        vehicles: list,
        vehicle_type: str | None = None
) -> list:
    available_vehicles = []
    for v in vehicles:
        if v["availability"] == "available":
            if vehicle_type is None or v["type"] == vehicle_type:
                available_vehicles.append(v)
    return available_vehicles
