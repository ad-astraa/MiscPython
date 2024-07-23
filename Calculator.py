import math
import matplotlib.pyplot as plt
import numpy as np

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def log(x):
    return math.log(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def cot(x):
    return 1 / math.tan(math.radians(x))

def sec(x):
    return 1 / math.cos(math.radians(x))

def cosec(x):
    return 1 / math.sin(math.radians(x))

def sqrt(x):
    return math.sqrt(x)

def plot_function(func, start, end, label):
    x = np.linspace(start, end, 400)
    y = [func(xi) for xi in x]
    plt.plot(x, y, label=label)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Graph of {label}')
    plt.grid(True)
    plt.show()

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Logarithm")
    print("6. Sine")
    print("7. Cosine")
    print("8. Tangent")
    print("9. Cotangent")
    print("10. Secant")
    print("11. Cosecant")
    print("12. Square Root")
    print("13. Plot Graph")

    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

    elif choice in ['5', '6', '7', '8', '9', '10', '11', '12']:
        num = float(input("Enter the number: "))

        if choice == '5':
            print(f"log({num}) = {log(num)}")

        elif choice == '6':
            print(f"sin({num}) = {sin(num)}")

        elif choice == '7':
            print(f"cos({num}) = {cos(num)}")

        elif choice == '8':
            print(f"tan({num}) = {tan(num)}")

        elif choice == '9':
            print(f"cot({num}) = {cot(num)}")

        elif choice == '10':
            print(f"sec({num}) = {sec(num)}")

        elif choice == '11':
            print(f"cosec({num}) = {cosec(num)}")

        elif choice == '12':
            print(f"sqrt({num}) = {sqrt(num)}")

    elif choice == '13':
        print("Select function to plot:")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        print("4. Cotangent")
        print("5. Secant")
        print("6. Cosecant")
        print("7. Logarithm")
        print("8. Square Root")

        func_choice = input("Enter choice(1/2/3/4/5/6/7/8): ")
        start = float(input("Enter start of range: "))
        end = float(input("Enter end of range: "))

        if func_choice == '1':
            plot_function(lambda x: math.sin(math.radians(x)), start, end, 'sin(x)')

        elif func_choice == '2':
            plot_function(lambda x: math.cos(math.radians(x)), start, end, 'cos(x)')

        elif func_choice == '3':
            plot_function(lambda x: math.tan(math.radians(x)), start, end, 'tan(x)')

        elif func_choice == '4':
            plot_function(lambda x: 1 / math.tan(math.radians(x)), start, end, 'cot(x)')

        elif func_choice == '5':
            plot_function(lambda x: 1 / math.cos(math.radians(x)), start, end, 'sec(x)')

        elif func_choice == '6':
            plot_function(lambda x: 1 / math.sin(math.radians(x)), start, end, 'cosec(x)')

        elif func_choice == '7':
            plot_function(lambda x: math.log(x), start, end, 'log(x)')

        elif func_choice == '8':
            plot_function(lambda x: math.sqrt(x), start, end, 'sqrt(x)')

    else:
        print("Invalid input")

# Run the calculator
calculator()
