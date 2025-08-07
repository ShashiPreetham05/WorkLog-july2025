#Range(stop) using a random input
'''for i in range(10):
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
    print(f"{num} x {i} = {num * i}")'''

# Creating a list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("Original list:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Slicing
print("First 3 fruits:", fruits[:3])
print("Fruits from index 2:", fruits[2:])
print("Middle 3 fruits:", fruits[1:4])

# Adding elements
fruits.append("fig")
print("After append:", fruits)

fruits.insert(2, "grape")
print("After insert at index 2:", fruits)

# Removing elements
fruits.remove("banana")
print("After removing 'banana':", fruits)

popped = fruits.pop()
print("Popped last item:", popped)
print("After pop:", fruits)

# Changing an element
fruits[1] = "blueberry"
print("After modifying index 1:", fruits)

# Length of list
print("Number of fruits:", len(fruits))

# Sorting
fruits.sort()
print("Sorted fruits:", fruits)

# Reversing
fruits.reverse()
print("Reversed fruits:", fruits)

# Checking membership
print("Is 'apple' in list?", "apple" in fruits)
print("Is 'mango' in list?", "mango" in fruits)

# Iterating over list
print("All fruits:")
for fruit in fruits:
    print("-", fruit)

# List comprehension (create new list)
lengths = [len(fruit) for fruit in fruits]
print("Lengths of each fruit name:", lengths)

# Clear all items
fruits.clear()
print("After clearing the list:", fruits)

