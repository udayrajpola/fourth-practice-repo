def sum1(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2



def calc():
    num1=float(input("input the first number\n"))
    uday=True
    while uday:
        operations = {
            "+": sum1,
            "-": subtraction,
            "*": multiplication,
            "/": division
        }
        for symbols in operations:
            print(symbols)
        operation = input("Please select the operation you want to do?")
        num2 = float(input("input the second number\n"))
        answer1 = operations[operation](num1, num2)
        print(f"{num1} + {num2} = {answer1}")
        user_choice = input("Please select do tou want to continue or stop")
        if user_choice == "y":
            num1 = answer1
        else:
            uday = False
            print("\n"*20)
            calc()


calc()


