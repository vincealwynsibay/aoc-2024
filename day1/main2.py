def main():
    with open("./input.txt", 'r') as inputs:
        lines = inputs.readlines()
        count_map = dict()
        left_list = []
        for line in lines:
            a,b = line.strip().split("   ")

            if not a in count_map:
                count_map[a] = 0

            if not b in count_map:
                count_map[b] = 1
            else:
                count_map[b] = (count_map[b] + 1)

            left_list.append(a)
        
        print(get_total_similarity_score(left_list, count_map))

def get_total_similarity_score(left_list, count_map):
    total_similarity_score = 0
    for i in left_list:
        total_similarity_score += (int(i) * count_map[i])

    return total_similarity_score

if __name__ == "__main__":
    main()