#Task 1

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
gr_index = 0

for x in grades:
    if x < 80:
        gr_index = grades.index(x)
        print(students[gr_index], grades[gr_index], activities[gr_index])


#Task 2
        
students_approved = []

for x in grades:
    if x > 80:
        gr_index = grades.index(x)
        students_approved.append(students[gr_index])

print(students_approved)
