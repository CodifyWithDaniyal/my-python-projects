# This program calculates a student's grade based on obtained and total marks.
# It computes the percentage and uses match–case with conditional patterns
# to determine and print the grade according to predefined ranges.
ob=int(input("Enter your obtained marks:"))
to=int(input("Enter total marks:"))
grade=ob/to*100
match grade:
    case _ if grade >= 90 :
        print("A+")
    case _ if grade >= 80:
        print("A")
    case _ if grade >=70:
        print("B+")
    case _ if grade >=60:
        print("B")
    case _ if grade >=50:
        print("C+")
    case _ if grade >=40:
        print("C")
    case _ if grade >=30:
        print("D")
    case _:
        print("Fail")
