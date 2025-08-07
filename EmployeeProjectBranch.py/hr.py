# === hr.py ===

hr_employees = [
    {"name": "Aarti Sharma", "id": 101, "salary": 48000.0, "permanent": True},
    {"name": "Rohan Verma", "id": 102, "salary": 52000.0, "permanent": False},
    {"name": "Nikita Mehra", "id": 103, "salary": 60000.0, "permanent": True}
]

'''
def get_hr_employees():
    employees = []
    print("\nEnter HR department employee details:")
    for i in range(3):
        name = input(f"Enter name of employee {i+1}: ")
        emp_id = int(input("Enter ID: "))
        salary = float(input("Enter salary: "))
        permanent = input("Is permanent (yes/no): ").lower() == "yes"
        employees.append({"name": name, "id": emp_id, "salary": salary, "permanent": permanent})
    return employees
'''