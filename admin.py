import sqlite3

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Train")
        print("2. View All Trains")
        print("3. View All Bookings")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            add_train()
        elif choice == '2':
            view_trains()
        elif choice == '3':
            view_bookings()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

def add_train():
    conn = sqlite3.connect('data/railway.db')
    cursor = conn.cursor()

    train_name = input("Enter train name: ")
    source = input("Enter source: ")
    destination = input("Enter destination: ")
    seats_available = int(input("Enter number of seats: "))

    cursor.execute("INSERT INTO trains (name, source, destination, seats_available) VALUES (?, ?, ?, ?)", 
                   (train_name, source, destination, seats_available))
    conn.commit()
    conn.close()
    print("Train added successfully!")

def view_trains():
    conn = sqlite3.connect('data/railway.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM trains")
    trains = cursor.fetchall()

    if not trains:
        print("No trains available.")
    else:
        print("\nTrain List:")
        print("ID | Name       | Source      | Destination | Seats Available")
        print("-" * 50)
        for train in trains:
            print(f"{train[0]}  | {train[1]} | {train[2]} | {train[3]} | {train[4]}")

    conn.close()

def view_bookings():
    conn = sqlite3.connect('data/railway.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bookings")
    bookings = cursor.fetchall()

    if not bookings:
        print("No bookings found.")
    else:
        print("\nBooking List:")
        print("ID | Train ID | User Name | Seats Booked | Date")
        print("-" * 50)
        for booking in bookings:
            print(f"{booking[0]}  | {booking[1]} | {booking[2]} | {booking[3]} | {booking[4]}")

    conn.close()
