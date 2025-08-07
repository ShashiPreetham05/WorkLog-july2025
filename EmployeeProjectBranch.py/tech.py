# === tech.py ===

tech_employees = [
    {"name": "Anil Kumar", "id": 301, "salary": 75000.0, "permanent": True},
    {"name": "Divya Singh", "id": 302, "salary": 67000.0, "permanent": True},
    {"name": "Sameer Joshi", "id": 303, "salary": 50000.0, "permanent": False},
    {"name": "Kavita Rao", "id": 304, "salary": 58000.0, "permanent": True},
    {"name": "Rahul Jain", "id": 305, "salary": 62000.0, "permanent": True}
]

'''
def get_tech_employees():
    employees = []
    print("\nEnter Tech department employee details:")
    for i in range(5):
        name = input(f"Enter name of employee {i+1}: ")
        emp_id = int(input("Enter ID: "))
        salary = float(input("Enter salary: "))
        permanent = input("Is permanent (yes/no): ").lower() == "yes"
        employees.append({"name": name, "id": emp_id, "salary": salary, "permanent": permanent})
    return employees
'''