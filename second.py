#Range(stop) using a random input
for i in range(10):
    print("Saas")

#Using range(start, stop)
for i in range(1, 6):
    print(i)

#Using range(start, stop, step)
for i in range(1, 11, 2):
    print(i)

#Backward loop with negative step
for i in range(5, 0, -1):
    print(i)


#Print Table of a Number
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
