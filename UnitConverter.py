def show_menu():
    print("\nUnit Converter Menu:")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")

def length_converter():
    print("\nLength Converter:")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    choice = input("Choose a conversion (1-4): ")

    if choice == '1':
        meters = float(input("Enter length in meters: "))
        feet = meters * 3.28084
        print(f"{meters} meters is {feet:.2f} feet.")
    elif choice == '2':
        feet = float(input("Enter length in feet: "))
        meters = feet / 3.28084
        print(f"{feet} feet is {meters:.2f} meters.")
    elif choice == '3':
        kilometers = float(input("Enter length in kilometers: "))
        miles = kilometers * 0.621371
        print(f"{kilometers} kilometers is {miles:.2f} miles.")
    elif choice == '4':
        miles = float(input("Enter length in miles: "))
        kilometers = miles / 0.621371
        print(f"{miles} miles is {kilometers:.2f} kilometers.")
    else:
        print("Invalid choice.")

def weight_converter():
    print("\nWeight Converter:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Choose a conversion (1-2): ")

    if choice == '1':
        kilograms = float(input("Enter weight in kilograms: "))
        pounds = kilograms * 2.20462
        print(f"{kilograms} kilograms is {pounds:.2f} pounds.")
    elif choice == '2':
        pounds = float(input("Enter weight in pounds: "))
        kilograms = pounds / 2.20462
        print(f"{pounds} pounds is {kilograms:.2f} kilograms.")
    else:
        print("Invalid choice.")

def temperature_converter():
    print("\nTemperature Converter:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose a conversion (1-2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius * 9/5 + 32
        print(f"{celsius}°C is {fahrenheit:.2f}°F.")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is {celsius:.2f}°C.")
    else:
        print("Invalid choice.")

def main():
    while True:
        show_menu()
        choice = input("\nChoose a category (1-4): ")
        if choice == '1':
            length_converter()
        elif choice == '2':
            weight_converter()
        elif choice == '3':
            temperature_converter()
        elif choice == '4':
            print("Exiting the Unit Converter. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
