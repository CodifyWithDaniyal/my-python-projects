# This program tells the user what action to take based on a traffic light color.
# The user enters the color of the traffic light.
# Using match–case, it prints STOP for red, Get ready for yellow, and GO for green.
# Both lowercase and capitalized inputs are accepted. Invalid inputs print an error message.
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