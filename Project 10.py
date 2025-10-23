#this program takes obtained marks and total marks and tells your grade
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
    case _ if grade >=400:
        print("C")
    case _ if grade >=30:
        print("D")
    case _:
        print("Fail")
