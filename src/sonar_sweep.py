"""sonar_sweep.py"""

"""
Solution for Advent of Code, Day 1 Puzzle
https://adventofcode.com/2021/day/1
"""
def main():
    print("---------Sonar Sweep----------")

    with open('../resources/SonarSweepInput.txt', 'r') as data:
        lines = data.readlines()

    x = 0
    y = 1
    z = 2

    new_list = []
    for l in lines:
        temp_sum = int(lines[x]) + int(lines[y]) + int(lines[z])
        new_list.append(temp_sum)
        x += 1
        y += 1
        z += 1
        if z == len(lines):
            break

    no_of_increases = 0
    previous_value = 0

    for x in new_list:
        temp = int(x)
        if temp > previous_value:
            no_of_increases = no_of_increases + 1
        previous_value = temp

    # since we will not count the very first increase 1 should be subtracted
    # from the answer
    print("total number of increases is: {}".format(no_of_increases - 1))


if __name__ == "__main__":
    main()
