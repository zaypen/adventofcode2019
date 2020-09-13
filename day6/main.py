def process(lines):
    mappings = {satellite: parent for (parent, satellite) in [line.split(')') for line in lines]}

    def orbits_of(satellite):
        parent = mappings.get(satellite)
        if parent:
            return 1 + orbits_of(parent)
        return 0

    return sum([orbits_of(satellite) for satellite in mappings.keys()])


def main():
    f = open('input')
    lines = f.readlines()
    print(process(list(map(lambda l: l.strip(), lines))))


if __name__ == '__main__':
    main()
