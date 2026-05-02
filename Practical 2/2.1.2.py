# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

# print original dictionary
print("Original Dictionary:", student)

# insertion
k = int(input())
v = input()
student[k] = v
print("After Insertion:", student)

# update
k = int(input())
v = input()
if k in student:
	student[k] = v
print("After Update:", student)

# deletion
k = int(input())
if k in student:
	student.pop(k)
print("After Deletion:", student)

# traversal
print("Traversing Dictionary:")
for k in student:
	print(k, ":", student[k])
