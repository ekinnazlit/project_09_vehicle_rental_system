from storage import load_state, save_state, backup_state
from vehicles import add_vehicle
from customers import register_customer
from reservations import create_reservation, cancel_reservation, complete_rental
from datetime import date

BASE = "data"
BACKUPS = "backups"

vehicles, customers, reservations = load_state(BASE)

while True:
    print("\n1. Add Vehicle")
    print("2. Register Customer")
    print("3. Create Reservation")
    print("4. Backup")
    print("5. Cancel Reservation")
    print("6. Complete Rental")
    print("0. Exit")

    choice = input("Choice: ")

    try:
        if choice == "1":
            v = add_vehicle(vehicles, {
                "brand": input("Brand: "),
                "model": input("Model: "),
                "year": int(input("Year: ")),
                "type": input("Type: "),
                "mileage": int(input("Mileage: ")),
                "daily_price": float(input("Daily price: ")),
                "rate_per_km": float(input("Rate/km: ")),
                "features": input("Features (comma): ").split(",")
            })

            save_state(BASE, vehicles, customers, reservations)
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
            save_state(BASE, vehicles, customers, reservations)

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


            save_state(BASE, vehicles, customers, reservations)
            print("Reservation created:", r)


        elif choice == "4":
            backup_state(BASE, BACKUPS)
            print("Backup completed")


        elif choice == "5":
            reservation_id = input("Reservation ID: ")

            cancelled = cancel_reservation(
                reservations,
                reservation_id
            )

            save_state(BASE, vehicles, customers, reservations)

            print("Reservation cancelled:", cancelled)



        elif choice == "6":
            reservation_id = input("Reservation ID: ")
            actual_mileage = float(input("Actual mileage (KM): "))

            completed = complete_rental(
                reservations,
                vehicles,
                reservation_id,
                actual_mileage
            )

            save_state(BASE, vehicles, customers, reservations)

            print("Rental completed:", completed)
            print("Invoice total:", completed["invoice"]["total"])




        elif choice == "0":
            save_state(BASE, vehicles, customers, reservations)
            break

    except Exception as e:
        print("Error:", e)
