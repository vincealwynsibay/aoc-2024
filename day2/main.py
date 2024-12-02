def main():
    with open("./input.txt", 'r') as inputs:
        lines = inputs.readlines()
        total_safe = 0
        for line in lines:
            parsed_line = [int(x) for x in line.strip().split(" ")]
            if evaluate_line(parsed_line):
                total_safe += 1
        
        print(total_safe)

def evaluate_line(line):
    is_increasing = line[0] < line[1]

    for i in range(0, len(line) - 1):
        if not evaluate_level(line[i], line[i + 1], is_increasing):
            return False
        
    return True

def evaluate_level(a, b, is_increasing):
    if is_increasing:
        # b is bigger than a
        return b - a >= 1 and b - a <= 3
    else:
        return a - b >= 1 and a - b <= 3

if __name__ == "__main__":
    main()