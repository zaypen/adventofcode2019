from itertools import dropwhile, zip_longest


def process(lines):
    mappings = {satellite: parent for (parent, satellite) in [line.split(')') for line in lines if len(line)]}

    def orbits_of(satellite):
        parent = mappings.get(satellite)
        if parent:
            return [satellite] + orbits_of(parent)
        return []

    orbits_of_you = orbits_of('YOU')
    orbits_of_santa = orbits_of('SAN')

    paths = dropwhile(lambda pair: pair[0] == pair[1], zip_longest(reversed(orbits_of_you), reversed(orbits_of_santa)))
    path1, path2 = map(lambda path: filter(lambda v: v, path), zip(*paths))
    transfer_path = list(path1) + ['SHARED'] + list(reversed(list(path2)))
    return len(transfer_path) - 3


def main():
    f = open('input')
    lines = f.readlines()
    print(process(list(map(lambda l: l.strip(), lines))))


if __name__ == '__main__':
    main()
