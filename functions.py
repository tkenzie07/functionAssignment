import math

# Function to calculate the area of a circle
def area_of_circle(pi, radius):
    return pi * (radius ** 2)

# Function to calculate the total due
def total_due(money, tax_rate):
    return money + (money * tax_rate)

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

# Main program
def main():
    # Prompt for input and calculate area of a circle
    radius = float(input("Enter the radius of the circle: "))
    area = area_of_circle(math.pi, radius)
    print(f"The area of the circle is: {area:.2f}")

    # Prompt for input and calculate total due
    money = float(input("Enter the amount of money: "))
    tax_rate = float(input("Enter the tax rate (as a decimal): "))
    total = total_due(money, tax_rate)
    print(f"The total due is: {total:.2f}")

    # Prompt for input and convert Fahrenheit to Celsius
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"The temperature in Celsius is: {celsius:.5f}")

if __name__ == "__main__":
    main()
