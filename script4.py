# def function1(name,last):
#     first_name=name
#     last_name=last
#     return first_name,last_name
#
# full_name=function1("uday","raj")
# print(full_name)
#
# def function2(function1):
#     name=function1.title()
#     return f"{name}"
#
# print(function2(function1("uday","raj")))
#
def ful_name(first_name,last_name):
    return f"{first_name.title()} {last_name.title()}"

full_name=ful_name(input("What is your  first name\nuda"),input("What is your  last name\n"))
print(full_name)