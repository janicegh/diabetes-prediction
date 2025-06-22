print("Hello, AI World!")
import numpy as np
print(np.__version__)

age = 25
height = 175.5
name = "Alice"
is_student = True
scores = [85, 90, 78, 92]
person = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student,
    "scores": scores

    }


print(f"Name: {name}, Age: {age}, Scores: {scores}")



score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")
    
for i in range(5):
    print(f"Iteration {i}")
    
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1