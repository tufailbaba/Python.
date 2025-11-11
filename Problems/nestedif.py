#WAP to input marks of a student and print the corresponding grade using nested if-else statements
marks = int(input("Enter the marks: "))
if marks >= 90:
    grade = 'A' 
else:
    if marks >= 80:
        grade = 'B'
    else:
        if marks >= 70:
            grade = 'C'
        else:
            if marks >= 60:
                grade = 'D'
            else:
                grade = 'F'