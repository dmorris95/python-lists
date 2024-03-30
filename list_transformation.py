#Task 1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()
print(grades)


#Task 2
#Much easier and more efficient to use a for loop
average = grades[0] + grades[1] + grades[2] + grades[3] + grades[4] + grades[5] + grades[6] + grades[7] + grades[8] + grades[9]
average /= len(grades)
print(average)


#Task 3

#because the list is in descending order you just have to find where the grade becomes less than 80
grades[9] = "Failed"
grades[8] = "Failed"
grades[7] = "Failed"
print(grades)
