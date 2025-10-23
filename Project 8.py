#This program takes the colour of the traffic light and tells either to stop,go or get ready
co=input("Please enter the colour of the traffic light: ")
match co:
    case "red" | "Red":
        print("STOP")
    case "yellow" | "Yellow":
        print("Get ready")
    case "green" | "Green":
         print("GO")
    case _:
         print("Invalid choice")