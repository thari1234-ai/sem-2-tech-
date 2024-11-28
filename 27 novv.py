name = input("Enter student's name: ")
roll_number = input("Enter roll number: ")


marks1 = float(input("Enter marks in subject 1: "))
marks2 = float(input("Enter marks in subject 2: "))
marks3 = float(input("Enter marks in subject 3: "))

total_marks = marks1 + marks2 + marks3
percentage = (total_marks / 300) * 100

if percentage >= 85:
    grade = "S"
elif percentage >= 75:
    grade = "A"
elif percentage >= 65:
    grade = "B"
elif percentage >= 55:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"  # Failing grade

print("\nStudent Details:")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Marks: {marks1}, {marks2}, {marks3}")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
