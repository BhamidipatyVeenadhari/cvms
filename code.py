import csv
from datetime import datetime

class VaccinationAppointment:
    def __init__(self, child_name, vaccination_name, appointment_date):
        self.child_name = child_name
        self.vaccination_name = vaccination_name
        self.appointment_date = appointment_date

    def __str__(self):
        return f"Child: {self.child_name}, Vaccine: {self.vaccination_name}, Appointment Date: {self.appointment_date.strftime('%Y-%m-%d')}"

class ChildVaccinationManagementSystem:
    def __init__(self):
        self.appointment_map = {}

    def load_data(self, filename):
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 3:
                        child_name, vaccination_name, date_str = row
                        appointment_date = datetime.strptime(date_str, '%Y-%m-%d')
                        self.book_appointment(child_name, vaccination_name, appointment_date)
            print(f"Data loaded successfully from {filename}")
        except Exception as e:
            print(f"Error loading data: {e}")

    def book_appointment(self, child_name, vaccination_name, appointment_date):
        if child_name not in self.appointment_map:
            self.appointment_map[child_name] = {}
        if vaccination_name not in self.appointment_map[child_name]:
            self.appointment_map[child_name][vaccination_name] = []
        self.appointment_map[child_name][vaccination_name].append(appointment_date)
        print(f"Appointment booked successfully for {child_name}")

    def view_appointments(self, child_name):
        if child_name in self.appointment_map:
            print(f"Appointments for {child_name}:")
            for vaccine, dates in self.appointment_map[child_name].items():
                for date in dates:
                    print(f"Vaccine: {vaccine}, Appointment Date: {date.strftime('%Y-%m-%d')}")
        else:
            print(f"No appointments found for {child_name}")

    def view_reminders(self, child_name):
        current_date = datetime.now()
        if child_name in self.appointment_map:
            print(f"Upcoming reminders for {child_name}:")
            for vaccine, dates in self.appointment_map[child_name].items():
                for date in dates:
                    if date > current_date:
                        print(f"Vaccine: {vaccine}, Appointment Date: {date.strftime('%Y-%m-%d')}")
        else:
            print(f"No upcoming appointments found for {child_name}")

    def cancel_appointment(self, child_name, vaccination_name, appointment_date):
        if child_name in self.appointment_map:
            if vaccination_name in self.appointment_map[child_name]:
                dates = self.appointment_map[child_name][vaccination_name]
                if appointment_date in dates:
                    dates.remove(appointment_date)
                    print(f"Appointment canceled for {child_name}")
                else:
                    print("No appointment found to cancel.")
            else:
                print("No appointment found to cancel.")
        else:
            print("No appointment found to cancel.")

def main():
    system = ChildVaccinationManagementSystem()
    system.load_data('appointments.txt')

    while True:
        print("\nChild Vaccination Management System")
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. View Reminders")
        print("4. Cancel Appointment")
        print("5. Exit")
        option = input("Choose an option: ")

        if option == '1':  # Book Appointment
            child_name = input("Enter child's name: ")
            vaccination_name = input("Enter vaccination name: ")
            date_str = input("Enter appointment date (yyyy-mm-dd): ")
            try:
                appointment_date = datetime.strptime(date_str, '%Y-%m-%d')
                system.book_appointment(child_name, vaccination_name, appointment_date)
            except ValueError:
                print("Invalid date format. Please use yyyy-mm-dd.")

        elif option == '2':  # View Appointments
            child_name = input("Enter child's name: ")
            system.view_appointments(child_name)

        elif option == '3':  # View Reminders
            child_name = input("Enter child's name: ")
            system.view_reminders(child_name)

        elif option == '4':  # Cancel Appointment
            child_name = input("Enter child's name: ")
            vaccination_name = input("Enter vaccination name: ")
            date_str = input("Enter appointment date to cancel (yyyy-mm-dd): ")
            try:
                appointment_date = datetime.strptime(date_str, '%Y-%m-%d')
                system.cancel_appointment(child_name, vaccination_name, appointment_date)
            except ValueError:
                print("Invalid date format. Please use yyyy-mm-dd.")

        elif option == '5':  # Exit
            print("Exiting the system.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
