import time

def add(new_numbers):
    total = 0
    for number in new_numbers:
        total += number
    return total

def subtract(new_numbers):
    total = new_numbers[0]
    for number in new_numbers[1:]:
        total -= number
    return total

def multiply(new_numbers):
    total = 1
    for number in new_numbers:
        total *= number
    return total


def divide(new_numbers):
    total = new_numbers[0]
    for number in new_numbers[1:]:
        total /= number
    return total

def modulus(new_numbers):
    total = new_numbers[0]
    for number in new_numbers[1:]:
        total = total % number
    return  total

def power(new_numbers):
    return new_numbers[0] ** new_numbers[1]

def square(new_numbers):
    return new_numbers[0] ** 2

def exit_program():
    quit()

def show_menu():
    print("==== Simple Calculator ====")
    operation_menu = "\n".join(f"{i}. {operation['name']} {operation['symbol']}" for i, operation in enumerate(calculator_display_list))
    print(f"Available operations for this calculator are: \n{operation_menu}")

def play_again():
    while True:
        compute_again = input("Do you want to perform another operation? (Yes/No): ").strip().lower()
        if compute_again == "yes":
            time.sleep(1.5)
            print("\n\n")
            return True
        elif compute_again == "no":
            quit()
        else:
            print("Invalid input. Enter yes or no.")
def main():
    while True:
        try:
            show_menu()     
            user_choice = int(input(f"Enter the number of the operation you want to perform(0-{len(calculator_display_list) - 1}): "))

            if user_choice not in range(0, len(calculator_display_list)):
                print(f"\n\nInvalid input. Please enter a number from 0-{len(calculator_display_list) - 1}\n\n")
                continue

            menu_choice= calculator_display_list[user_choice]["key"]
            menu_operation_symbol = calculator_display_list[user_choice]["symbol"] 
            menu_operation_name = calculator_display_list[user_choice]["name"].lower()  

            if menu_choice == "exit":
                calculator_operations_dict["exit"]()
                        


            if user_choice in range (1, len(calculator_display_list)):
                while True:
                    number_list =input(f"You chose {menu_operation_name.upper()}({menu_operation_symbol}). Type the numbers you would like to {menu_operation_name}(E.g 2 86):\n").strip().split()
                    try:
                        if number_list:
                            new_number_list = [float(number.strip()) for number in number_list] 
                        else:
                            print("\nInvalid input. List empty. You have to enter a number.\n")
                            continue 
                    except ValueError as e:
                        print(f"\nInvalid input {e.args[0]}. Please enter numbers only, seperated with a space.")
                        continue

                    if (menu_choice == "modulus" or menu_choice == "power") and len(new_number_list) != 2:
                        print(f"\n{menu_choice.title()} requires exactly two numbers")
                        continue

                    if menu_choice == "square" and len(new_number_list) != 1:
                        print("Square requires exactly one number.")
                        continue

                    if menu_choice == "divide" and 0 in new_number_list[1:]:
                        print("\nYou can not divide by zero")
                        continue                
                    break
                values = f" {menu_operation_symbol} ".join(str(num) for num in new_number_list)
                print(f"{values} = {calculator_operations_dict[menu_choice](new_number_list)}")
                if play_again():
                    continue
                

        
        except ValueError:
            print("\n\nInvalid input. Please enter a valid option number.\n\n")

#Code
print("\nWelcome! This is a Simple Calculator.\n")
calculator_operations_dict = {
    "exit": exit_program,
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "modulus": modulus,
    "power": power,
    "square": square,
}

calculator_display_list = [
    {"key": "exit", "name": "EXIT", "symbol": ""},
    {"key": "add", "name": "ADD", "symbol": "+"},
    {"key": "subtract", "name": "SUBTRACT", "symbol": "-"},
    {"key": "multiply", "name": "MULTIPLY", "symbol": "x"},
    {"key": "divide", "name": "DIVIDE", "symbol": "/"},
    {"key": "modulus", "name": "MODULUS", "symbol": "%"},
    {"key": "power", "name": "POWER", "symbol": "^"},
    {"key": "square", "name": "SQUARE", "symbol":"^2"},
]
main()