import json
import os
import shutil
from datetime import datetime

def load_state(base_dir: str):
    def load(name):
        path = os.path.join(base_dir, name)
        if not os.path.exists(path):
            return []
        with open(path) as f:
            return json.load(f)

    return (
        load("vehicles.json"),
        load("customers.json"),
        load("reservations.json")
    )

def save_state(base_dir: str, vehicles: list,
               customers: list, reservations: list) -> None:
    os.makedirs(base_dir, exist_ok=True)

    def save(name, data):
        with open(os.path.join(base_dir, name), "w") as f:
            json.dump(data, f, indent=2)

    save("vehicles.json", vehicles)
    save("customers.json", customers)
    save("reservations.json", reservations)

def backup_state(base_dir: str, backup_dir: str) -> list[str]:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(backup_dir, f"backup_{timestamp}")
    os.makedirs(dest, exist_ok=True)

    copied = []
    for f in ["vehicles.json", "customers.json", "reservations.json"]:
        src = os.path.join(base_dir, f)
        if os.path.exists(src):
            shutil.copy(src, dest)
            copied.append(os.path.join(dest, f))
    return copied

def validate_reservation(reservation: dict) -> bool:
    required = ["id", "vehicle_id", "start_date", "end_date", "status"]
    return all(k in reservation for k in required)


