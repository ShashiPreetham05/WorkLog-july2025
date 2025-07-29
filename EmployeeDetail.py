emp_name="Sai kiran"
emp_id=6066
emp_salary=29000
is_permenent=True

print("Employee Record")
print("Name       :",emp_name)
print("Employee ID:",emp_id)
print("Salary     :",emp_salary,"/-")
print("Permenent  :",is_permenent)
#checking whether salary above threshold or Not
salary_threshold=50000
if emp_salary > salary_threshold and is_permenent:
    print("Eligible for bonus")
else:
    print("Not Eligible for bonus")

#Program which takes input from user
emp_name=input("Enter employee name:")
emp_id=int(input("Enter employee Id:"))
emp_salary=float(input("Enter salary:"))
is_permenent=input("Is the employee perment(yes/no):")=="yes"

print("\n Employee Record")
print(" Name      :",emp_name)
print("Employee ID:",emp_id)
print("Salary     :",emp_salary)
print("Permenent  :",is_permenent)

if emp_salary > 50000 and is_permenent:
    print("Eligible for bonus")
else:
    print("Not Eligible for bonus")