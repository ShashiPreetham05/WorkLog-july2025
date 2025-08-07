# === main.py ===
from hr import hr_employees
from sales import sales_employees
from tech import tech_employees

def display_branch_employees(branch_name, employees):
    print(f"\n {branch_name} Department Employees:")
    for emp in employees:
        print(f"- {emp['name']} (ID: {emp['id']}, Salary: ₹{emp['salary']}, Permanent: {emp['permanent']})")
        if emp['salary'] > 50000 and emp['permanent']:
            print("   Eligible for bonus")
        else:
            print("   Not eligible for bonus")

if __name__ == "__main__":
    display_branch_employees("HR", hr_employees)
    display_branch_employees("Sales", sales_employees)
    display_branch_employees("Tech", tech_employees)
