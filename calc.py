import math


def basic_calculator(num1, num2, operator):
    if operator == "1":
        return num1 + num2
    elif operator == "2":
        return num1 - num2
    elif operator == "3":
        return num1 * num2
    elif operator == "4":
        if num2 != 0:
            return num1 / num2
        else:
            return "(INVALID)"
    elif operator == "5":
        return num1 ** num2
    else:
        return "Invalid Operator"


def geometric_calculator(shape):
    if shape == "1":
        width = abs(float(input("Enter the width: ")))
        height = abs(float(input("Enter the height: ")))
        return width * height
    
    elif shape == "2":
        radius = abs(float(input("Enter the radius: ")))
        return math.pi * radius ** 2

    elif shape == "3":
        base = abs(float(input("Enter the base: ")))
        height = abs(float(input("Enter the height: ")))
        return 0.5 * base * height

    else:
        return "Invalid Shape"


def run_geometric_calculator():
    geoRunning = True
    shapes = {"1", "2", "3"}

    while geoRunning:
        print("Geometric Calculator")
        print("1: Area of a rectangle")
        print("2: Area of a circle")
        print("3: Area of a triangle")
    
        shape = input("Choose an option (1/2/3): ")

        if shape not in shapes:
            print("Invalid Shape Entered")
            continue

        try:
            area = geometric_calculator(shape)
            print("Your answer is:", area)
        except ValueError:
            print("Invalid Value Entered (Try Using A Number!)")

        keepGeoRunning = input("Do you want to run another geometric calculation? (yes/no): ").lower()
        if keepGeoRunning == "no":
            geoRunning = False


def run_basic_calculator():
    running = True
    operators = {"1", "2", "3", "4", "5"}

    while running:
        print("Basic Calculator")
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Division")
        print("5: Power")

        operator = input("Choose an operator (1/2/3/4/5): ")

        if operator not in operators:
            print("Invalid Operator Entered")
            continue

        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            result = basic_calculator(num1, num2, operator)
            print("Your answer is:", result)
        except ValueError:
            print("Invalid Value Entered (Try Using A Number!)")

        keepRunning = input("Do you want to run another calculation? (yes/no): ").lower()
        if keepRunning == "no":
            running = False

choice = input("Choose a calculator (basic/geometric): ").lower()

if choice == "basic":
    run_basic_calculator()
elif choice == "geometric":
    run_geometric_calculator()
else:
    print("Invalid choice, please choose 'basic' or 'geometric'")























    


        
       