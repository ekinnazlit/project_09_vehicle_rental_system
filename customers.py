import json
import os

def load_customers(path: str) -> list:
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

def save_customers(path: str, customers: list) -> None:
    with open(path, "w") as f:
        json.dump(customers, f, indent=2)


def register_customer(customers: list, profile: dict) -> dict:
    for c in customers:
        if c.get("license_number") == profile["license_number"]:
            raise ValueError("License already exists")

    numbers = []

    for c in customers:
        customer_id = c.get("id", "")

        if customer_id.startswith("C-"):
            number_part = customer_id[2:]

            if number_part.isdigit():
                numbers.append(int(number_part))

    next_id = max(numbers, default=0) + 1

    customer = {
        "id": f"C-{next_id}",
        "rentals": [],
        "flags": []
    }

    customer.update(profile)
    customers.append(customer)

    return customer

def authenticate_customer(customers: list, license_number: str, pin: str):
    for c in customers:
        if c["license_number"] == license_number and c["pin"] == pin:
            return c
    return None

def update_customer_profile(customers: list, customer_id: str, updates: dict) -> dict:
    for c in customers:
        if c["id"] == customer_id:
            c.update(updates)
            return c
    raise ValueError("Customer not found")



