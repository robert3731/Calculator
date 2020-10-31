import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


select = int(input('''
Select operations form: 
1. Add 
2. Subtract
3. Multiply
4. Divide
'''))

number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))

if select == 1:
    logging.info("Adding {} and {}".format(number_1, number_2))
    print('Result {}'.format(add(number_1, number_2)))

elif select == 2:
    logging.info("Subtracting {} and {}".format(number_1, number_2))
    print('Result {}'.format(subtract(number_1, number_2)))

elif select == 3:
    logging.info("Multiplying {} and {}".format(number_1, number_2))
    print('Result {}'.format(multiply(number_1, number_2)))

elif select == 4:
    logging.info("Dividing {} and {}".format(number_1, number_2))
    print('Result {}'.format(divide(number_1, number_2)))
else:
    print("Invalid input!")


