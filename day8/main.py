from itertools import combinations
from collections import defaultdict
import math


with open('./input.txt', 'r') as inputs:
    data = inputs.read().strip().split("\n")

def main():
        
    antennas = defaultdict(list)

    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] != ".":
                antennas[data[i][j]].append((i, j))

    antinode_list = set()
    for antenna in antennas:
        coords = antennas[antenna]
        for a, b in combinations(coords, r=2):
            ax, ay = a
            bx, by = b
            dx, dy = (bx - ax), (by - ay)

            i = 0 
            while True:
                if is_bounds(bx + dx * i, by + dy * i):
                    antinode_list.add((bx + dx * i, by + dy * i))
                else:
                    break
                i += 1
            
            i = 0 
            while True:
                if is_bounds(ax - dx * i, ay - dy * i):
                    antinode_list.add((ax - dx * i, ay - dy * i))
                else:
                    break
                i += 1

            #     cx, cy = ax - (bx - ax), ay - (by - ay)
            #     dx, dy = bx + (bx - ax), by + (by - ay)

            # if is_bounds(cx, cy):
            #     antinode_list.add((cx, cy))
            # if is_bounds(dx, dy):
            #     antinode_list.add((dx, dy))

    print(len(antinode_list))

def is_bounds(x, y):
    return 0 <= x < len(data) and 0 <= y < len(data)




if __name__ == "__main__":
    main()