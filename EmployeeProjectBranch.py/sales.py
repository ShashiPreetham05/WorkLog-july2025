# === sales.py ===

sales_employees = [
    {"name": "Suresh Iyer", "id": 201, "salary": 45000.0, "permanent": True},
    {"name": "Neha Das", "id": 202, "salary": 55000.0, "permanent": True},
    {"name": "Karan Patel", "id": 203, "salary": 40000.0, "permanent": False}
]

'''
def get_sales_employees():
    employees = []
    print("\nEnter Sales department employee details:")
    for i in range(3):
        name = input(f"Enter name of employee {i+1}: ")
        emp_id = int(input("Enter ID: "))
        salary = float(input("Enter salary: "))
        permanent = input("Is permanent (yes/no): ").lower() == "yes"
        employees.append({"name": name, "id": emp_id, "salary": salary, "permanent": permanent})
    return employees
'''