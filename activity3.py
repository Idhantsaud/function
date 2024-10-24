def subtraction(a, b):
    return a - b
def addition(a, b):
    return a + b 
def division(a, b):
    return a/b
def multiplication(a, b):
    return a*b

print("Welcomme to the Calculator!")
print("Enter your choice of operation from below options:")
print("a addition")
print("b Subtraction")
print("c division")
print("d multiplication")
choice = input("Select a or b or c or d:")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == "a":
    print(num1,"+",num2,"=",addition(num1,num2))
elif choice == "b":
    print(num1, "-", num2,"=",subtraction(num1,num2))
elif choice == "c":
    print(num1, "/", num2,"=",division(num1,num2))
elif choice == "d":
    print(num1, "*", num2,"=", multiplication(num1,num2))
else:
    print("Incorrect choice please try again")
