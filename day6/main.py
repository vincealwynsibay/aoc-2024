import time
def main():
    with open('./input.txt', 'r') as data:
        lines = data.readlines()
        lab_map = list(list())
        guard_directions = ["^", ">", "v", "<"]
        guard_direction = None
        guard_pos = [0, 0]
        distinct_positions = []
        total_distinct_visited = 1

        for i in range(len(lines)):
            row = []
            for j in range(len(lines[i])):
                if not lines[i][j] == "\n":
                    row.append(lines[i][j])
                if lines[i][j] in guard_directions:
                    guard_pos = [i, j]
                    guard_direction = lines[i][j]
                    distinct_positions.append([i,j])
            lab_map.append(row)

        while True:
            # move based on direction
            x, y = guard_pos
            updates_pos = guard_pos

            if guard_direction == guard_directions[0]:
                # up
                updates_pos = [x - 1, y]
            elif guard_direction == guard_directions[1]:
                # right
                updates_pos = [x, y + 1]
            elif guard_direction == guard_directions[2]:
                # down
                updates_pos = [x + 1, y]
            elif guard_direction == guard_directions[3]:
                # left
                updates_pos = [x, y - 1]

            x2, y2 = updates_pos
            
            # if outside map
            if not x2 >= 0 or not x2 < len(lines) or not y2 >= 0 or not y2 < len(lines[0]):
                break

            # obstacle
            if lines[x2][y2] == "#":
                guard_direction = guard_directions[(guard_directions.index(guard_direction) + 1) % len(guard_directions)]
            else:
                # if not obstacle move there
                lab_map[x2][y2] = "X"
                guard_pos = updates_pos

                if not guard_pos in distinct_positions:
                    total_distinct_visited += 1
                    distinct_positions.append(guard_pos)
            
            # print(total_distinct_visited)
            # for row in lab_map:
            #     for ele in row:
            #         print(ele, end="")
            #     print()
            # print()
        print(total_distinct_visited, distinct_positions)
if __name__ == "__main__":
    main()