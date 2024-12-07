def main():
    with open('./input.txt', 'r') as data:
        lines = data.readlines()
        ordering_rules = {}
        pages_list = []
        total_middle_page_sum = 0
        for line in lines:
            if "|" in line:
                a, b = line.strip().split("|")

                if a not in ordering_rules:
                    ordering_rules[a] = []
                
                ordering_rules[a].append(b)
            elif line != "\n":
                pages_list.append(line.strip().split(","))

        for pages in pages_list:
            is_valid = True

            # repeat until correct updates
            while not is_update_valid(ordering_rules, pages):
                is_valid = False
                for i in range(len(pages)):
                    current = pages[i]

                    for j in range(i+1, len(pages)):
                        if (pages[j] in ordering_rules.keys() and pages[i] in ordering_rules[pages[j]]) or (current in ordering_rules.keys() and not pages[j] in ordering_rules[current]):
                            # swap invalid order
                            temp = pages[i]
                            pages[i] = pages[j]
                            pages[j] = temp
                            break
            if not is_valid:
                middle_page = pages[int(len(pages) / 2)]
                total_middle_page_sum += int(middle_page)

                
        print(total_middle_page_sum)

def is_update_valid(rules, pages):
    is_valid = True

    for i in range(len(pages)):
        current = pages[i]

        for j in range(i+1, len(pages)):
            if not current in rules or not pages[j] in rules[current]:
                # swap invalid order
                temp = pages[i]
                pages[i] = pages[j]
                pages[j] = temp
                is_valid = False
                break
        if not is_valid:
            break
    return is_valid

if __name__ == "__main__":
    main()