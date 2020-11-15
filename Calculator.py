import logging
from math import prod

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def add(numbers: list) -> float:
    return sum(numbers)


def subtract(num1, num2: float) -> float:
    return num1 - num2


def multiply(numbers: list) -> float:
    return prod(numbers)


def divide(num1, num2: float) -> float:
    return num1 / num2


def menu():
    while True:
        select = int(input('''
        Select operations form: 
        1. Add 
        2. Subtract
        3. Multiply
        4. Divide
        5. Exit
        '''))

        if select == 1:
            try:
                numbers_list = list(map(float, input("Enter a multiple value(ex. 1 2.3 13): ").split()))
            except ValueError:
                print("Entered values cannot be added. Please enter correct values.")
                numbers_list = list(map(float, input("Enter a multiple value(ex. 1 2.3 13): ").split()))
            finally:
                logging.info("Adding {}".format(numbers_list))
                print('Result {}'.format(add(numbers_list)))

        elif select == 2:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            logging.info("Subtracting {} and {}".format(number_1, number_2))
            print('Result {}'.format(subtract(number_1, number_2)))

        elif select == 3:
            try:
                numbers_list = list(map(float, input("Enter a multiple value(ex. 1 2.3 13): ").split()))
            except ValueError:
                print("Entered values cannot be multiplied. Please enter correct values.")
                numbers_list = list(map(float, input("Enter a multiple value(ex. 1 2.3 13): ").split()))
            finally:
                logging.info("Multiplying {}".format(numbers_list))
                print('Result {}'.format(multiply(numbers_list)))

        elif select == 4:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            logging.info("Dividing {} and {}".format(number_1, number_2))
            print('Result {}'.format(divide(number_1, number_2)))

        elif select == 5:
            return False

        else:
            print("Invalid input")


if __name__ == '__main__':
    menu()
