import math


def fuel_of(mass):
    return math.floor(mass / 3) - 2


def calc(masses):
    return sum([fuel_of(int(mass)) for mass in masses])


def main():
    f = open('input')
    lines = f.readlines()
    print(calc(lines))


if __name__ == '__main__':
    main()
