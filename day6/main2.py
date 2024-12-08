import cProfile
import copy
guard_directions = ["^", ">", "v", "<"]
def main():
    with open('./input.txt', 'r') as data:
        lines = data.readlines()
        lab_map = list(list())


        guard_direction = None
        guard_pos = [0, 0]
        total = 0
        for i in range(len(lines)):
            row = []
            for j in range(len(lines[i])):
                if not lines[i][j] == "\n":
                    row.append(lines[i][j])
                if lines[i][j] in guard_directions:
                    guard_pos = [i, j]
                    guard_direction = lines[i][j]
            lab_map.append(row)

        distinct_positions = get_distinct_positions(lab_map, guard_pos, guard_direction)
        print(len(distinct_positions))
        loop_count = 0
        for dpos in distinct_positions:
            lab_map_copy = copy.deepcopy(lab_map)
            if dpos != guard_pos:
                lab_map_copy[dpos[0]][dpos[1]] = "O"
                if is_time_loop(lab_map_copy, guard_pos, guard_direction):
                    loop_count += 1

        
        print(loop_count)


def is_time_loop(map, guard_pos, guard_direction):
    # check if position has already been visited with the same guard direction ([x,y], direction)
    distinct_positions = [(guard_pos, guard_direction)]
    total_distinct_visited = 1
    pos = guard_pos
    direction = guard_direction
    visited_positions = []
  
    frequency_map = [[0] * len(map[0]) for _ in range(len(map))]
    frequency_map[guard_pos[0]][guard_pos[1]] = 1


    while True:
        # move based on direction
        x, y = pos
        updates_pos = pos   

        if direction == guard_directions[0]:
            # up
            updates_pos = [x - 1, y]
        elif direction == guard_directions[1]:
            # right
            updates_pos = [x, y + 1]
        elif direction == guard_directions[2]:
            # down
            updates_pos = [x + 1, y]
        elif direction == guard_directions[3]:
            # left
            updates_pos = [x, y - 1]

        x2, y2 = updates_pos
        
        # if outside map
        if not x2 >= 0 or not x2 < len(map) or not y2 >= 0 or not y2 < len(map[0]):
            return False

        # obstacle
        if map[x2][y2] == "#" or map[x2][y2] == "O":
            direction = guard_directions[(guard_directions.index(direction) + 1) % len(guard_directions)]
        else:
            # if not obstacle move there
            map[x2][y2] = "X"
            pos = updates_pos

            if frequency_map[x2][y2] == 5:
                return True

            frequency_map[x2][y2] = frequency_map[x2][y2] + 1

            if not pos in distinct_positions:
                total_distinct_visited += 1
                distinct_positions.append((pos, guard_direction))
        


def get_distinct_positions(map, guard_pos, guard_direction):
    # check if position has already been visited with the same guard direction ([x,y], direction)
    distinct_positions = []
    total_distinct_visited = 1
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
        if not x2 >= 0 or not x2 < len(map) or not y2 >= 0 or not y2 < len(map[0]):
            break

        # obstacle
        if map[x2][y2] == "#":
            guard_direction = guard_directions[(guard_directions.index(guard_direction) + 1) % len(guard_directions)]
        else:
            # if not obstacle move there
            map[x2][y2] = "X"
            guard_pos = updates_pos

            if not guard_pos in distinct_positions:
                total_distinct_visited += 1
                distinct_positions.append(guard_pos)
        
    return distinct_positions

def print_map(map):
    for row in map:
        for ele in row:
            print(ele, end="")
        print()
if __name__ == "__main__":
    cProfile.run("main()")