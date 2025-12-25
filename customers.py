{
    "id": "C-1",
    "name": "Ekin Nazli Tas",
    "license_number": "51 EA 192",
    "pin": "1234",
    "contact": {
        "email": "ekin@example.com",
        "phone": "5347568791"
    },
    "payment": {
        "card_last4": "4242",
        "method": "credit"
    },
    "rentals": [],
    "flags": []
}
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
        if c["license_number"] == profile["license_number"]:
            raise ValueError("Customer already registered")

    customer = {
        "id": f"C-{len(customers) + 1}",
        "rentals": [],
        "flags": []
    }

    customer.update(profile)
    customers.append(customer)
    return customer
def authenticate_customer(customers: list,
                          license_number: str,
                          pin: str) -> dict | None:
    for c in customers:
        if c["license_number"] == license_number and c["pin"] == pin:
            return c
    return None
def update_customer_profile(customers: list,
                            customer_id: str,
                            updates: dict) -> dict:
    for c in customers:
        if c["id"] == customer_id:
            c.update(updates)
            return c
    raise ValueError("Customer not found")


