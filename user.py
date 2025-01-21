import sqlite3
from datetime import datetime

def user_menu():
    while True:
        print("\nUser Menu:")
        print("1. Search Trains")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. View Booking History")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            search_trains()
        elif choice == '2':
            book_ticket()
        elif choice == '3':
            cancel_ticket()
        elif choice == '4':
            view_booking_history()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def search_trains():
    source = input("Enter source: ")
    destination = input("Enter destination: ")

    conn = sqlite3.connect('data/railway.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM trains WHERE source=? AND destination=?", (source, destination))
    trains = cursor.fetchall()

    if not trains:
        print("No trains found.")
    else:
        print("\nAvailable Trains:")
        print("ID | Name       | Source      | Destination | Seats Available")
        print("-" * 50)
        for train in trains:
            print(f"{train[0]}  | {train[1]} | {train[2]} | {train[3]} | {train[4]}")

    conn.close()

def book_ticket():
    user_name = input("Enter your name: ")
    train_id = int(input("Enter train ID to book: "))
    seats_to_book = int(input("Enter number of seats to book: "))

    conn = sqlite3.connect('data/railway.db')
    cursor = conn.cursor()

    cursor.execute("SELECT seats_available FROM trains WHERE train_id=?", (train_id,))
    train = cursor.fetchone()

    if train and train[0] >= seats_to_book:
        new_seats = train[0] - seats_to_book
        cursor.execute("UPDATE trains SET seats_available=? WHERE train_id=?", (new_seats, train_id))

        booking_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO bookings (train_id, user_name, seats_booked, date) VALUES (?, ?, ?, ?)",
                       (train_id, user_name, seats_to_book, booking_date))
        conn.commit()
        print("Ticket booked successfully!")
    else:
        print("Not enough seats available.")

    conn.close()

def cancel_ticket():
    booking_id = int(input("Enter booking ID to cancel: "))

    conn = sqlite3.connect('data/railway.db')
    cursor = conn.cursor()

    cursor.execute("SELECT train_id, seats_booked FROM bookings WHERE booking_id=?", (booking_id,))
    booking = cursor.fetchone()

    if booking:
        train_id, seats_to_cancel = booking
        cursor.execute("DELETE FROM bookings WHERE booking_id=?", (booking_id,))

        cursor.execute("SELECT seats_available FROM trains WHERE train_id=?", (train_id,))
        train = cursor.fetchone()
        if train:
            new_seats = train[0] + seats_to_cancel
            cursor.execute("UPDATE trains SET seats_available=? WHERE train_id=?", (new_seats, train_id))

        conn.commit()
        print("Booking canceled successfully!")
    else:
        print("Booking ID not found.")

    conn.close()

def view_booking_history():
    user_name = input("Enter your name: ")

    conn = sqlite3.connect('data/railway.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bookings WHERE user_name=?", (user_name,))
    bookings = cursor.fetchall()

    if not bookings:
        print("No bookings found for this user.")
    else:
        print("\nYour Bookings:")
        print("ID | Train ID | User Name | Seats Booked | Date")
        print("-" * 50)
        for booking in bookings:
            print(f"{booking[0]}  | {booking[1]} | {booking[2]} | {booking[3]} | {booking[4]}")

    conn.close()
