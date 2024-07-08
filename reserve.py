import csv
import os
import datetime

tables = [
    {'number': 1, 'seats': 2},
    {'number': 2, 'seats': 4},
    {'number': 3, 'seats': 4},
    {'number': 4, 'seats': 6},
    {'number': 5, 'seats': 8},
]
reservations_file = 'reservations.csv'

# Function to view tables
def view_tables():
    for table in tables:
        print(table)

# Function to make reservations
def make_reservation(tables, reservations_file, reservations):
    name = input("Enter your name: ")
    contact = input("Enter your contact number: ")
    size = int(input("Enter number of people: "))
    date = input("Enter date (YYYY-MM-DD): ")
    
    available_tables = [table for table in tables if table['seats'] >= size and (table['number'], date) not in reservations]
    
    if not available_tables:
        print("No available tables for your party size or the tables are already reserved.")
        return
    
    print("Available tables:")
    for table in available_tables:
        print(f"Table {table['number']} - seats: {table['seats']}")
    
    table_number = int(input("Enter table number to reserve: "))
    if table_number not in [table['number'] for table in available_tables]:
        print("Invalid table number.")
        return
    
    new_row = [table_number, name, contact, size, date]
    file_exists = os.path.isfile(reservations_file)
    
    try:
        with open(reservations_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Table Number", "Name", "Contact", "Size", "Date"])
            writer.writerow(new_row)
        print(f"Table {table_number} reserved successfully for {name}.")
    except Exception as e:
        print(f"Error saving reservation: {e}")
    
    reservations[(table_number, date)] = {
        'name': name,
        'contact': contact,
        'size': size,
        'date': date,
    }

# Function to cancel reservations
def cancel_reservation(reservations_file, reservations):
    name = input("Enter your name: ")
    table_number = int(input("Enter table number to cancel: "))
    date = input("Enter date (YYYY-MM-DD): ")
    
    if (table_number, date) in reservations and reservations[(table_number, date)]['name'] == name:
        del reservations[(table_number, date)]
        print(f"Reservation for {name} at table {table_number} on {date} has been canceled.")
        
        try:
            updated_reservations = []
            with open(reservations_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    if int(row[0]) != table_number or row[1] != name or row[4] != date:
                        updated_reservations.append(row)
            
            with open(reservations_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(updated_reservations)
        except Exception as e:
            print(f"Error updating reservations file: {e}")
    else:
        print(f"No reservation found for {name} at table {table_number} on {date}.")

# Function to view reservations
def view_reservations(reservations):
    if not reservations:
        print("No reservations found.")
    else:
        for (table_number, date), reservation in reservations.items():
            print(f"Table {table_number} on {date}: {reservation}")

# Function to modify reservations
def modify_reservation(reservations_file, reservations):
    table_number = int(input("Enter table number to modify: "))
    date = input("Enter current reservation date (YYYY-MM-DD): ")
    name = input("Enter your name: ")
    
    try:
        with open(reservations_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)
            reservations_list = list(reader)
        
        updated_reservations = []
        reservation_found = False
        
        for res in reservations_list:
            if int(res[0]) == table_number and res[1] == name and res[4] == date:
                reservation_found = True
                print("Reservation found!")
                
                new_name = input("Enter new name: ")
                new_contact = input("Enter new contact number: ")
                new_size = int(input("Enter new number of people: "))
                new_date = input("Enter new date (YYYY-MM-DD): ")
                
                updated_reservations.append([table_number, new_name, new_contact, new_size, new_date])
                del reservations[(table_number, date)]
                reservations[(table_number, new_date)] = {
                    'name': new_name,
                    'contact': new_contact,
                    'size': new_size,
                    'date': new_date,
                }
            else:
                updated_reservations.append(res)
        
        if reservation_found:
            with open(reservations_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(updated_reservations)
            print("Reservation modified successfully.")
        else:
            print("No matching reservation found.")
    except Exception as e:
        print(f"Error modifying reservation: {e}")

# Function to get daily summary of reservations
def daily_summary(date, reservations):
    print(f"Reservations for {date}:")
    daily_reservations = {key: value for key, value in reservations.items() if key[1] == date}
    
    if not daily_reservations:
        print("No reservations found for this date.")
    else:
        for (table_number, _), reservation in daily_reservations.items():
            print(f"Table {table_number}: {reservation}")

# Function to start the application
def start_App():
    reservations = {}
    if os.path.isfile(reservations_file):
        try:
            with open(reservations_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                headers = next(reader)
                for row in reader:
                    table_number = int(row[0])
                    date = row[4]
                    reservations[(table_number, date)] = {
                        'name': row[1],
                        'contact': row[2],
                        'size': int(row[3]),
                        'date': row[4],
                    }
        except Exception as e:
            print(f"Error loading reservations: {e}")
    
    while True:
        print("\nMenu:")
        print("1. View tables")
        print("2. Make a reservation")
        print("3. View reservations")
        print("4. Cancel a reservation")
        print("5. Modify a reservation")
        print("6. Daily summary")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            view_tables()
        elif choice == '2':
            make_reservation(tables, reservations_file, reservations)
        elif choice == '3':
            view_reservations(reservations)
        elif choice == '4':
            cancel_reservation(reservations_file, reservations)
        elif choice == '5':
            modify_reservation(reservations_file, reservations)
        elif choice == '6':
            date = input("Enter date (YYYY-MM-DD): ")
            daily_summary(date, reservations)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

# Start the application
start_App()
