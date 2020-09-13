class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def is_vertical(self):
        return self.x1 - self.x2 == 0

    def intersection_with(self, other):
        if self.is_vertical() == other.is_vertical():
            return None
        vertical, horizontal = (self, other) if self.is_vertical() else (other, self)
        if (horizontal.x1 - vertical.x1) * (horizontal.x2 - vertical.x1) >= 0:
            return None
        if (vertical.y1 - horizontal.y1) * (vertical.y2 - horizontal.y1) >= 0:
            return None
        return vertical.x1, horizontal.y1

    def __repr__(self):
        return 'Line(({}, {}), ({}, {}))'.format(self.x1, self.y1, self.x2, self.y2)


operations = {
    'U': lambda position, d: (position[0], position[1] + d),
    'D': lambda position, d: (position[0], position[1] - d),
    'L': lambda position, d: (position[0] - d, position[1]),
    'R': lambda position, d: (position[0] + d, position[1]),
}


def lines_of(position, commands):
    if len(commands):
        command = commands[0]
        next_position = operations[command[0]](position, command[1])
        return [Line(position[0], position[1], next_position[0], next_position[1])] + lines_of(next_position, commands[1:])
    return []


def commands_of(sequence):
    return map(lambda c: (c[0], int(c[1:])), sequence.split(','))


def intersections_between(wire1, wire2):
    return filter(lambda p: p, [line1.intersection_with(line2) for line1 in wire1 for line2 in wire2])


def process(sequences):
    commands = map(commands_of, sequences)
    wires = list(map(lambda s: lines_of((0, 0), list(s)), commands))
    points = intersections_between(wires[0], wires[1])
    return min(points, key=lambda p: abs(p[0]) + abs(p[1]))


def main():
    f = open('input')
    lines = f.readlines()
    print(process(map(lambda l: l.strip(), lines)))


if __name__ == '__main__':
    main()
