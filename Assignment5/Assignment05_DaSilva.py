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