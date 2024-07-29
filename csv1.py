import csv

class EmployeeManagementSystem:
    def __init__(self, filename):
        self.filename = filename

    def add_employee(self, employee_data):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(employee_data)
        print(f"Employee {employee_data[0]} added successfully!")

    def update_employee(self, employee_id, updated_data):
        employees = self.read_all_employees()
        found = False
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for employee in employees:
                if employee[0] == employee_id:
                    writer.writerow(updated_data)
                    found = True
                    print(f"Employee {employee_id} updated successfully!")
                else:
                    writer.writerow(employee)
        if not found:
            print(f"Employee {employee_id} not found.")

    def read_all_employees(self):
        employees = []
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            employees = list(reader)
        return employees

    def display_employees(self):
        employees = self.read_all_employees()
        for emp in employees:
            print(emp)

    def generate_report(self):
        employees = self.read_all_employees()
        department_counts = {}
        for emp in employees:
            department = emp[2]  # Assuming department is the third column
            if department in department_counts:
                department_counts[department] += 1
            else:
                department_counts[department] = 1
        print("Department-wise Employee Report:")
        for department, count in department_counts.items():
            print(f"{department}: {count} employees")

