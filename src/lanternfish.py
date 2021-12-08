"""lanternfish.py"""

"""
Solution for Advent of Code, Day 7 Puzzle
https://adventofcode.com/2021/day/7
"""

import datetime

def main():
    print("---------Lanternfish----------")

    with open('../resources/lanternfish_input.txt', 'r') as data:
        lines = data.readlines()

    # split the list and convert all elements of lines to integers
    lines = lines[0].split(',')
    lines = [int(i) for i in lines]

    new_list = []  # init a new list

    #print("Start of Day: {}".format(lines))

    for i in range(80):
        #print("Day: {} : # of fish: {} : {}".format((i + 1), len(lines) ,datetime.datetime.now()))
        count = 0
        for x in lines:
            if x == 0:
                lines[count] = 6
                lines.append(9)
            else:
                lines[count] -= 1
            count += 1
        #print("End of Day {}: {}".format((i + 1), lines))

    print(len(lines))

if __name__ == "__main__":
    main()
