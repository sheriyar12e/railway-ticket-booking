import sqlite3

def initialize_database():
    conn = sqlite3.connect('data/railway.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS trains (
                        train_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        source TEXT,
                        destination TEXT,
                        seats_available INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                        booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        train_id INTEGER,
                        user_name TEXT,
                        seats_booked INTEGER,
                        date TEXT)''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
