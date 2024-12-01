def main():
    with open("./input.txt", 'r') as inputs:
        lines = inputs.readlines()
        left_list = []
        right_list = []
        for line in lines:
            a,b = line.strip().split("   ")
            left_list.append(int(a))
            right_list.append(int(b))
        print(get_total_distance(left_list, right_list))


def get_total_distance(left_list, right_list):
    left_list.sort()            
    right_list.sort()
    total_distance = 0
    for i in range(len(left_list)):
        total_distance += (abs(left_list[i] - right_list[i])) 

    return total_distance

if __name__ == "__main__":
    main()