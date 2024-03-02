import math

class BasicMathOperations:
    
    def GreetUser(self, firstName, lastName):
        return "Welcome {} {}!".format(firstName, lastName)
    
    def AddNumbers(self, num1, num2):
        return num1 + num2

    def PerformOperation(self, num1, num2, operation):
        if (operation == "+"):
            return num1 + num2
        elif (operation == "-"):
            return num1 - num2
        elif (operation == "*"):
            return num1 * num2
        elif (operation == "/"):
            return num1 / num2
        else:
            return None
        
    def SquareNumber(self, num):
        return num ** 2
    
    def Factorial(self, num):
        return math.factorial(num)
    
    def Counting(self, start, end):
        if (start > end):
            return ""
        else:
            return "{} {}".format(start, self.Counting(start+1, end))
        
    def ComputeHypotnuse(self, leg1, leg2):
        return math.sqrt(self.SquareNumber(leg1) + self.SquareNumber(leg2))
    
    def RectangleArea(self, width, height):
        return width * height
    
    def Power(self, base, exponent):
        return base ** exponent
    
    def ArgumentType(self, arg):
        try:
            newArg = int(arg)
        except ValueError:
            try:
                newArg = float(arg)
            except ValueError:
                newArg = arg
        if arg == "True" or arg == "False":
            newArg = bool(arg)

        return type(newArg)
    
def main():

    mathOps = BasicMathOperations()

    print("========== CHOOSE AN OPTION =============")
    print("1. Greet")
    print("2. Add Numbers")
    print("3. Perform Operation")
    print("4. Square Number")
    print("5. Factorial Of Number")
    print("6. Count")
    print("7. Calculate Hypotnuse")
    print("8. Rectangle Area")
    print("9. Number To Power")
    print("10. Type") 
    print("11. Quit Menu")
    print("==========================================") 
    
    print() 

    userInput = ""
    while (userInput != "11"):
        userInput = input("Enter An Option: ")
        if (userInput == "1"):
            print("~ Greet ~")
            firstName = input("Enter Your First Name: ")
            lastName = input("Enter Your Last Name: ")
            print(mathOps.GreetUser(firstName, lastName))
        elif (userInput == "2"):
            print("~ Add Numbers ~")
            num1 = float(input("Enter Number 1: "))
            num2 = float(input("Enter Number 2: "))
            print ("{} + {} = {}".format(num1, num2, mathOps.AddNumbers(num1, num2)))
        elif (userInput == "3"):
            print("~ Perform Operation ~")
            num1 = float(input("Enter Number 1: "))
            num2 = float(input("Enter Number 2: "))
            operation = input("Enter An Operation [+, -, *, /]: ")
            while (mathOps.PerformOperation(num1, num2, operation) == None):
                print("Invalid Operation.")
                operation = input("Enter An Operation [+, -, *, /]: ")
            print("{} {} {} = {}".format(num1, operation, num2, mathOps.PerformOperation(num1, num2, operation)))
        elif (userInput == "4"):
            print("~ Square Number ~")
            num = float(input("Enter A Number: "))
            print("{}^2: {}".format(num, mathOps.SquareNumber(num)))
        elif (userInput == "5"):
            print("~ Factorial Of Number ~")
            num = int(input("Enter A Number: "))
            print("{}!: {}".format(num, mathOps.Factorial(num)))
        elif (userInput == "6"):
            print("~ Count ~")
            start = int(input("Enter Start Value: "))
            end = int(input("Enter End Value: "))
            print("Counting From {} to {}: {}".format(start, end, mathOps.Counting(start, end)))
        elif (userInput == "7"):
            print("~ Calculate Hypotnuse ~")
            leg1 = float(input("Enter Leg 1: "))
            leg2 = float(input("Enter Leg 2: "))
            print("Hypotnuse Of Triangle With Sides {} And {}: {}".format(leg1, leg2, mathOps.ComputeHypotnuse(leg1, leg2)))
        elif (userInput == "8"):
            print("~ Rectangle Area ~")
            width = float(input("Enter Width: "))
            height = float(input("Enter Height: "))
            print("Area Of Rectangle With Width Of {} And Height Of {}: {}". format(width, height, mathOps.RectangleArea(width, height)))
        elif (userInput == "9"):
            print("~ Number To Power ~")
            base = float(input("Enter Base: "))
            exponent = float(input("Enter Exponent: "))
            print("{} To The Power Of {}: {}".format(base, exponent, mathOps.Power(base, exponent)))
        elif (userInput == "10"):
            print("~ Type ~")
            arg = input("Enter An Argument: ")
            print("Type Of {}: {}".format(arg, mathOps.ArgumentType(arg)))
        elif (userInput == "11"):
            print("Quitting Menu...")
        else:
            print("Invalid Input.")

        print()

main()