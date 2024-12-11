from itertools import combinations
import math
def main():
    matrix = dict()
    with open('./input.txt', 'r') as inputs:
        data = inputs.read().strip()

        for x, line in enumerate(data.split("\n")):
            for y, c in enumerate(line):
                matrix[x, y] = c
        antennas = set(matrix.values())
        antennas.remove(".")

        total_distinct = 0
        for antenna in antennas:
            coordinates = []

            for key, val in matrix.items():
                if val == antenna:
                    coordinates.append(key)
                    
            for a, b in combinations(coordinates, 2):
                slope = get_slope(a, b)
                # check if there is in line thru slope
                for curr in add_coordinates(a, slope), get_slope(b, slope):
                    if curr in matrix:
                        total_distinct += 1
        print(total_distinct)


def add_coordinates(a, b):
    return abs(b[0] + a[0]), abs(b[1] + a[1])


def get_slope(a, b):
    return abs(b[0] - a[0]), abs(b[1] - a[1])

def get_distance(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)
        

if __name__ == "__main__":
    main()