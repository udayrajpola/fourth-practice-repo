print("Welcome to the calculator app")




def calc(num1,operation,num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Please enter valid operation")



val_gen=calc(int(input("Enter your first number?\n")),input('''Select the operation you want to use
+
-
%
*\n'''),int(input("input the next number\n")))
print(val_gen)

def nxt_round(val_gen,operation2,num3):
    if operation2 == "+":
        return val_gen + num3
    elif operation2 == "-":
        return val_gen - num3
    elif operation2 == "*":
        return val_gen * num3
    elif operation2 == "/":
        return val_gen / num3
    else:
        print("Please enter valid operation")





user_Choice=input("Do you want to calculate again with same number then y or n")
if user_Choice=="y":
    nxt_round(val_gen,input('''Select the operation you want to use
+
-
%
*\n'''),int(input("input the next number\n")))
elif user_Choice=="n":
    calc(int(input("Enter your first number?\n")), input('''Select the operation you want to use
    +
    -
    %
    *\n'''), int(input("input the next number\n")))

val_gen2= nxt_round(val_gen,input('''Select the operation you want to use
+
-
%
*\n'''),int(input("input the next number\n")))
print(val_gen2)

