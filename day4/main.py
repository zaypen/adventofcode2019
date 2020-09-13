adjacentDigits = list(map(lambda n: "{}{}".format(n, n), range(0, 10)))


def verify(password):
    string = str(password)
    digits = list(map(int, string))
    return all(map(lambda pair: pair[0] <= pair[1], zip(digits[:-1], digits[1:]))) and any([adjacent in string for adjacent in adjacentDigits])


def count_from_range(begin, end):
    return len(list(filter(verify, range(begin, end))))


def main():
    print(count_from_range(235741, 706948))


if __name__ == '__main__':
    main()
