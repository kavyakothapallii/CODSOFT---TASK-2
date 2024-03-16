print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Percentage")
choice = input("Enter Choice: ")
num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        print("Division by 0 is Invalid.")
    else:
        return a / b

def percentage(a, b):
    if b == 0:
        print("Percentage cannot be calculated when the denominator is 0.")
    else:
        return (a / b) * 100

if choice == '1':
    print(add(num1, num2))
elif choice == '2':
    print(sub(num1, num2))
elif choice == '3':
    print(mul(num1, num2))
elif choice == '4':
    print(div(num1, num2))
elif choice == '5':
    print(percentage(num1, num2))
else:
    print("Wrong Choice!")
