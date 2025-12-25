import json
import os
import shutil
from datetime import datetime
def load_state(base_dir: str) -> tuple[list, list, list]:
    def load_file(filename):
        path = os.path.join(base_dir, filename)
        if not os.path.exists(path):
            return []
        with open(path, "r") as f:
            return json.load(f)

    vehicles = load_file("vehicles.json")
    customers = load_file("customers.json")
    reservations = load_file("reservations.json")

    return vehicles, customers, reservations
def save_state(base_dir: str,
               vehicles: list,
               customers: list,
               reservations: list) -> None:
    os.makedirs(base_dir, exist_ok=True)

    def save_file(filename, data):
        path = os.path.join(base_dir, filename)
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    save_file("vehicles.json", vehicles)
    save_file("customers.json", customers)
    save_file("reservations.json", reservations)

def validate_reservation(reservation: dict) -> bool:
    required_fields = [
        "id",
        "vehicle_id",
        "start_date",
        "end_date",
        "status"
    ]

    for field in required_fields:
        if field not in reservation:
            return False

    if reservation["status"] not in {"active", "cancelled", "completed"}:
        return False

    return True
