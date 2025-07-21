student = int(input("Enter the student: "))
total_per =0
for i in range(1,student + 1):
    print("Enter marks for student: ", i)
    total_marks=0

    for j in range(1,6):
        marks = int(input("Enter the marks: "))
        print("Enter marks for student " )
        total_marks += marks

    per = total_marks / 500 * 100
    total_per += per
    print("percentage for student", i)
    print(per)

average_per = per /student
print("average per: ",average_per)