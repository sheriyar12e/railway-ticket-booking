from admin import admin_menu
from user import user_menu

def main():
    print("Welcome to Railway Ticket Booking System")
    while True:
        print("\n1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            admin_menu()
        elif choice == '2':
            user_menu()
        elif choice == '3':
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
