from collections import namedtuple

Operation = namedtuple('Operation', ['code', 'execute', 'number_of_parameters', 'write_value'])


class HaltError(RuntimeError):
    pass


class Context:
    def __init__(self, program):
        self.pc = 0
        self.program = program

    def __setitem__(self, key, value):
        self.program[key] = value

    def __getitem__(self, item):
        return self.program[item]

    def get(self, address=None):
        address = address or self.pc
        return self.program[address]

    def get_by_offset(self, offset):
        return self.program[self.pc + offset]


def halt():
    raise HaltError()


class Computer:
    operations = [
        Operation(1, lambda *args: (None, args[0] + args[1]), 2, True),
        Operation(2, lambda *args: (None, args[0] * args[1]), 2, True),
        Operation(3, lambda *args: (None, 5), 0, True),
        Operation(4, lambda *args: (None, print(args[0])), 1, False),
        Operation(5, lambda *args: (args[1] if args[0] else None, None), 2, False),
        Operation(6, lambda *args: (args[1] if not args[0] else None, None), 2, False),
        Operation(7, lambda *args: (None, 1 if args[0] < args[1] else 0), 2, True),
        Operation(8, lambda *args: (None, 1 if args[0] == args[1] else 0), 2, True),
        Operation(99, halt, 0, False)
    ]

    def __init__(self, program):
        self._context = Context(program)

    def _execute(self, operation: Operation):
        parameter_modes = [self._context.get() // 10 ** n % 10 for n in range(2, 5)]
        parameters = [value if parameter_modes[n] else self._context[value] for (n, value) in
                      [(n, self._context.get_by_offset(n + 1)) for n in range(operation.number_of_parameters)]]

        pc, value_to_write = operation.execute(*parameters)
        if operation.write_value:
            address_to_write = self._context.get_by_offset(1 + operation.number_of_parameters)
            self._context[address_to_write] = value_to_write

        self._context.pc = pc or self._context.pc + self._length_of_instruction(operation)

    def _step(self):
        op_code = self._context.get() % 100
        operation = self._find_first(lambda i: i.code == op_code, self.operations)
        if operation is None:
            raise RuntimeError()
        self._execute(operation)

    def run(self):
        try:
            while True:
                self._step()
        except HaltError:
            pass
        except RuntimeError:
            print('Failed at PC={}\n{} ...'.format(
                self._context.pc,
                self._context.program[self._context.pc: self._context.pc + 10])
            )

    @staticmethod
    def _find_first(predicate, iterable, default=None):
        return next((x for x in iterable if predicate(x)), default)

    @staticmethod
    def _length_of_instruction(operation: Operation) -> int:
        return 1 + operation.number_of_parameters + (1 if operation.write_value else 0)


def main():
    f = open('input')
    lines = f.readlines()
    Computer(list([int(byte) for line in lines for byte in line.split(',')])).run()


if __name__ == '__main__':
    main()
