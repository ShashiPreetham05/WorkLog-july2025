#User inputs are been taken
employees = []

n = int(input("How many employee records do you want to enter? "))

for i in range(n):
    print(f"\nEnter details for Employee {i+1}:")
    emp_name = input("Enter employee name: ")
    emp_id = int(input("Enter employee ID: "))
    emp_salary = float(input("Enter salary: "))
    is_permanent = input("Is the employee permanent? (yes/no): ").lower() == "yes"

    emp = {
        "name": emp_name,
        "id": emp_id,
        "salary": emp_salary,
        "permanent": is_permanent
    }
    employees.append(emp)

# Display all employee records
print(" All Employee Records:")
for emp in employees:
    print("Employee Record ")
    print("Name       :", emp["name"])
    print("Employee ID:", emp["id"])
    print("Salary     : ₹", emp["salary"])
    print("Permanent? :", emp["permanent"])

    if emp["salary"] > 50000 and emp["permanent"]:
        print(" Eligible for bonus")
    else:
        print(" Not eligible for bonus")

print(".................................................")

# Hardcoded employee list (developer input)
employees = [
    {"name": "Anjali", "id": 1001, "salary": 60000, "permanent": True},
    {"name": "Rakesh", "id": 1002, "salary": 40000, "permanent": False},
    {"name": "Priya",  "id": 1003, "salary": 52000, "permanent": True}
]

# Display all employee records
print(" Developer's Employee Records:")
for emp in employees:
    print(" Employee Record")
    print("Name       :", emp["name"])
    print("Employee ID:", emp["id"])
    print("Salary     : ₹", emp["salary"])
    print("Permanent? :", emp["permanent"])

    if emp["salary"] > 50000 and emp["permanent"]:
        print(" Eligible for bonus")
    else:
        print(" Not eligible for bonus")
