from calc_func import add, subtract
from calc_multiply import multiply
 
 
def main():
    print("""Select the function from the given options:
    1. Add
    2. Subtract
    3. Multiply
    4. Area of Rectangle
 
    """)
    choice = input("Enter your choice (1/2/3): ")
 
    if choice == "1":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"The result is: {add(a, b)}")
    elif choice == "2":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"The result is: {subtract(a, b)}")
    elif choice == "3":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"The result is: {multiply(a, b)}")
    elif choice == "4":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        print(f"The result is: {area_of_rectangle(length, width)}")
    else:
        print("Invalid choice.")
 
if __name__ == "__main__":
    main()
