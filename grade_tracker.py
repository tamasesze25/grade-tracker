grades = {}

while True:
    subject  = input("Enter the name of the subject: ")
    if subject == "stop":
        break
    grade = int(input("Grade: "))
    grades[subject] = grade

print(grades)

def average (grades):
   return sum(grades.values()) / len(grades)

def best_grade (grades):
    return max(grades.values())

print ("The average:", round (average(grades), 2))
best = max(grades, key=grades.get)
print(f"Best subject: {best} with grade {grades[best]}")