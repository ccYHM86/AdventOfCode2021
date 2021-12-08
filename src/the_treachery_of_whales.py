"""the_treachery_of_whales.py"""

"""
Solution for Advent of Code, Day 7 Puzzle
https://adventofcode.com/2021/day/7
"""
import statistics
import datetime

def main():
    print("---------The Treachery of Whales----------")

    with open('../resources/the_treachery_of_whales_input.txt ', 'r') as data:
        lines = data.readlines()

    # split the list and convert all elements of lines to integers
    lines = lines[0].split(',')
    lines = [int(i) for i in lines]

    part_1_start = datetime.datetime.now().microsecond

    # get the median
    most_common = int(statistics.median(lines))

    fuel_used = 0
    for x in lines:
        difference = abs(most_common - x)
        fuel_used += difference

    print("PART 01: total fuel used to move to position {} is: {} units"
          .format(most_common, fuel_used))

    part_1_end = datetime.datetime.now().microsecond
    print("part 01 completed in: {} milliseconds"
          .format(part_1_end - part_1_start))

    # part 2
    # using the brute force solution. Simply get the max value out of the
    # list and test every combination from 0 to the max value

    part_2_start = datetime.datetime.now().microsecond

    max_value = max(lines)
    results = []
    for x in range(max_value):
        fuel_used = 0
        for y in lines:
            # print("checking {} vs {}".format(x, y))
            difference = abs(x - y)
            fuel_used += difference * ((abs(x - y)) + 1) // 2
        results.append(fuel_used)

    print("PART 02: total fuel used to move to position {} is: {} units"
          .format(results.index(min(results)), min(results)))

    part_2_end = datetime.datetime.now().microsecond
    print("part 02 completed in: {} milliseconds"
          .format(part_2_end - part_2_start))


if __name__ == "__main__":
    main()
