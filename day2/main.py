operations = {
    1: lambda a, b: a + b,
    2: lambda a, b: a * b,
}


def execute(program):
    i = 0
    while True:
        op = program[i]
        operation = operations.get(op)
        if operation is None:
            break
        src1, src2, dest = program[i + 1:i + 4]
        program[dest] = operation(program[src1], program[src2])
        i = i + 4
    return program


def main():
    f = open('input')
    lines = f.readlines()
    print(execute(list(map(int, ''.join(lines).strip().split(',')))))


if __name__ == '__main__':
    main()