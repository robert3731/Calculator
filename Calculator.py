import logging
from math import prod

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def add(a, b, *args):
    logging.info("Dodawanie {} {} {}".format(a, b, args))
    return a + b + sum(args)


def sub(a, b, *args):
    logging.info("Odejmowanie {} {} {}".format(a, b, args))
    return a - b


def multiply(a, b, *args):
    logging.info("Mnożenie {} {} {}".format(a, b, args))
    return a * b * prod(args)


def divide(a, b, *args):
    logging.info("Dzielenie {} {} {}".format(a, b, args))
    if b == 0:
        return "Nie można dzielić przez 0"
    return a / b


def get_data():
    a = float(input('Podaj wartość a: ').replace(',', '.'))
    b = float(input('Podaj wartość b: ').replace(',', '.'))
    c = list(input("Naciśnij Enter lub podaj inne wartości (np. 1, 2.3, 13): ").split(','))
    if c[0] == '':
        c.clear()
        args = c.copy()
    else:
        args = [float(arg) for arg in c]

    return a, b, args


operations = {
    "1": add,
    "2": sub,
    "3": multiply,
    "4": divide
}


def main():
    op = input('Wybierz działanie, posługując się odpowiednią liczbą:\n'
               '1.Dodawanie\n'
               '2.Odejmowanie\n'
               '3.Mnożenie\n'
               '4.Dzielenie\n')
    a, b, args = get_data()

    result = operations[op](a, b, *args)
    print('Wynik działania to: {}'.format(result))


if __name__ == '__main__':
    main()
