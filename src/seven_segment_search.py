"""seven_segment_search.py"""

"""
Solution for Advent of Code, Day 8 Puzzle
https://adventofcode.com/2021/day/8
"""

def main():
    print("---------Seven Segment Search----------")

    with open('../resources/seven_segment_search_input.txt', 'r') as data:
        lines = data.readlines()

    # 0 - OFF
    # 1 - ?
    # 2 - 1
    # 3 - 7
    # 4 - 4
    # 5 - ?
    # 6 - ?
    # 7 - 8
    # 8 - ?
    # 9 - ?

    unique_segments = [7, 4, 3, 2]

    total_hits = 0
    for x in lines:
        output = x.split('|')
        a = output[1].split()
        for y in a:
            if len(y) in unique_segments:
                total_hits += 1

    print(total_hits)


if __name__ == "__main__":
    main()
