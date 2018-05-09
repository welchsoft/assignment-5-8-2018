class Calculator:
    def __init__(self):
        pass

    def user_input(self):
        first_number = float(input("Enter first number: "))
        operand = input("Enter the operand +,-,*,/ ")
        second_number = float(input("Enter second number"))
        return first_number,operand,second_number

    def add(self,num1,num2):
        return num1+num2

    def subtraction(self,num1,num2):
        return num1-num2

    def multiply(self,num1,num2):
        return num1*num2

    def divide(self,num1,num2):
        return num1/num2
