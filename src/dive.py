"""dive.py"""


def main():
    print("---------Dive----------")

    with open('../resources/dive_input.txt', 'r') as data:
        lines = data.readlines()

    depth = 0
    horizontal = 0
    aim = 0

    for line in lines:
        temp = line.split()
        if temp[0] == 'forward':
            horizontal += int(temp[1])
            depth += (aim * int(temp[1]))
        elif temp[0] == 'down':
            aim += int(temp[1])
        elif temp[0] == 'up':
            aim -= int(temp[1])
        else:
            print("ERROR: Invalid direction")
            exit(-1)

    print("horizontal position is set to: {}".format(horizontal))
    print("depth is set to: {}".format(depth))

    print("solution is: {}".format(horizontal * depth))


if __name__ == "__main__":
    main()
