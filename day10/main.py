with open('./input.txt', 'r') as input:
    data = input.read().strip().split()
trailheads = list()
map = list(list())

for i, row in enumerate(data):
    for j, ele in enumerate(row):
        if ele == '0':
            trailheads.append((i, j))
    map.append(list(row))

def next_position(i, j, curr_set, prev=None, count=0):
    if i < 0 or i >= len(map) or j < 0 or j >= len(map[0]):
        return 0
    elif prev != None and (int(prev) + 1) != int(map[i][j]):
        return 0
    elif int(map[i][j]) == 9 and not (i, j) in curr_set:
        curr_set.add((i,j))
        return 1
    
    
    curr = map[i][j]
    count = 0
    count += next_position(i + 1, j, curr_set, curr, count)
    count += next_position(i - 1, j, curr_set, curr, count)
    count += next_position(i, j + 1, curr_set, curr, count)
    count += next_position(i, j - 1, curr_set, curr, count)

    return count

total = 0
for head in trailheads:
    curr_set = set()
    i, j = head
    total +=  next_position(i, j, curr_set)
print(total)
    

    

