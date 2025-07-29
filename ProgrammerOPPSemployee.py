class Employee:
    def __init__(self, name, emp_id, salary, permanent):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.permanent = permanent

    def display(self):
        print("\n Employee Record ")
        print("Name       :", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary     : ", self.salary)
        print("Permanent? :", self.permanent)
        print(" Eligible for bonus" if self.salary > 50000 and self.permanent else " Not eligible for bonus")


# Hardcoded employee objects
emp1 = Employee("Neha", 2001, 60000, True)
emp2 = Employee("Raj", 2002, 40000, False)
emp3 = Employee("Ankit", 2003, 51000, True)

# List of employees
employee_list = [emp1, emp2, emp3]

# Displaying employee data
print(" Developer-Defined Employee Records (OOP Version):")
for emp in employee_list:
    emp.display()
