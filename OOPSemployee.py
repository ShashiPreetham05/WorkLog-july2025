class Employee:
    def __init__(self, name, emp_id, salary, permanent):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.permanent = permanent

    def display(self):
        print(" Employee Record ")
        print("Name       :", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary     : ", self.salary)
        print("Permanent? :", self.permanent)
        print(" Eligible for bonus" if self.salary > 50000 and self.permanent else " Not eligible for bonus")


# List to store multiple employees
employee_list = []

n = int(input("How many employees do you want to enter? "))

for i in range(n):
    print(f"\nEnter details for Employee {i+1}:")
    name = input("Enter name: ")
    emp_id = int(input("Enter ID: "))
    salary = float(input("Enter salary: "))
    permanent = input("Is the employee permanent? (yes/no): ").lower() == "yes"

    emp = Employee(name, emp_id, salary, permanent)
    employee_list.append(emp)

# Displaying all employee records
print(" All Employee Records (OOP Version):")
for emp in employee_list:
     emp.display()
