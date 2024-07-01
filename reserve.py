
tables = [
    {'number': 1, 'seats': 2},
    {'number': 2, 'seats': 4},
    {'number': 3, 'seats': 4},
    {'number': 4, 'seats': 6},
    {'number': 5, 'seats': 8},
]
reservations = {}

# function  to view the tables 
def view_tables(tables):
    for table in tables:
        print(f"Table {table['number']} - seats: {table['seats']}")

# function to make Reservations
def make_reservation(tables, reservations):
    name = input("Enter your name: ")
    contact = input("Enter your contact number: ")
    size = int(input("Enter number of people: "))
    
    available_tables = [table for table in tables if table['seats'] >= size and table['number'] not in reservations]
    
    if not available_tables:
        print("No available tables for your party size.")
        return
    
    print("Available tables:")
    for table in available_tables:
        print(f"Table {table['number']} - seats: {table['seats']}")
    
    table_number = int(input("Enter table number to reserve: "))
    
    # Check if the table is already reserved
    if table_number in reservations:
        print(f"Table {table_number} is already reserved.")
        return
    
    reservations[table_number] = {
        'name': name,
        'contact': contact,
        'size': size
    }
    print(f"Table {table_number} reserved successfully for {name}.")


# function to view Reservations
def view_reservations(reservations):
   for table_number, reservation in reservations.items():
        print(f"Table {table_number} reserved by {reservation['name']} for {reservation['size']} people. Contact: {reservation['contact']}")

#function to cancel a Reservation
def cancel_reservation(reservations):
    table_number = int(input("Enter table number to cancel reservation: "))
    if table_number not in reservations:
        print(f"No reservation found for table {table_number}.")
        return
    
    del reservations[table_number]
    print(f"Reservation for table {table_number} canceled.")

def main():
    while True:
        print("\n1. View Tables\n2. Make Reservation\n3. View Reservations\n4. Cancel Reservation\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tables(tables)
        elif choice == '2':
            make_reservation(tables, reservations)
        elif choice == '3':
            view_reservations(reservations)
        elif choice == '4':
            cancel_reservation(reservations)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
