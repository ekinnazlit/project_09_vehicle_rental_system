from storage import load_state, save_state, backup_state
from vehicles import add_vehicle
from customers import register_customer
from reservations import create_reservation
from datetime import date

BASE = "data"
BACKUPS = "backups"

vehicles, customers, reservations = load_state(BASE)

while True:
    print("\n1. Add Vehicle")
    print("2. Register Customer")
    print("3. Create Reservation")
    print("4. Backup")
    print("0. Exit")

    choice = input("Choice: ")

    try:
        if choice == "1":
            v = add_vehicle(vehicles, {
                "make": input("Make: "),
                "model": input("Model: "),
                "year": int(input("Year: ")),
                "type": input("Type: "),
                "mileage": int(input("Mileage: ")),
                "rate_per_day": int(input("Rate/day: ")),
                "rate_per_km": int(input("Rate/km: ")),
                "features": input("Features (comma): ").split(",")
            })
            print("Added:", v)

        elif choice == "2":
            c = register_customer(customers, {
                "name": input("Name: "),
                "license_number": input("License: "),
                "pin": input("PIN: "),
                "contact": {"phone": input("Phone: ")},
                "payment": {"method": "card"}
            })
            print("Registered:", c)

        elif choice == "3":
            r = create_reservation(reservations, {
                "vehicle_id": input("Vehicle ID: "),
                "customer_id": input("Customer ID: "),
                "start_date": input("Start (YYYY-MM-DD): "),
                "end_date": input("End (YYYY-MM-DD): "),
                "pickup": input("Pickup: "),
                "return": input("Return: "),
                "estimated_mileage": int(input("KM: "))
            }, vehicles)
            print("Reservation created:", r)

        elif choice == "4":
            backup_state(BASE, BACKUPS)
            print("Backup completed")

        elif choice == "0":
            save_state(BASE, vehicles, customers, reservations)
            break

    except Exception as e:
        print("Error:", e)
