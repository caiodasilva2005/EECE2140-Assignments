import math

class BasicMathOperations:
    
    def GreetUser(self, firstName, lastName):
        return "Welcome {} {}".format(firstName, lastName)
    
    def AddNumbers(self, num1, num2):
        return num1 + num2

    def PerformOperation(num1, num2, operation):
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
        return math.pow(base, exponent)
    
    def ArgumentType(self, arg):
        return type(arg)
    
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
    print("9. Number to a Power")
    print("10. Return Type")   

main()