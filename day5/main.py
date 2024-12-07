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

            for i in range(len(pages)):
                current = pages[i]

                for j in range(i+1, len(pages)):
                    if not current in ordering_rules or not pages[j] in ordering_rules[current]:
                        is_valid = False
                        break

                if not is_valid:
                    break
            if is_valid:
                middle_page = pages[int(len(pages) / 2)]
                total_middle_page_sum += int(middle_page)

        print(total_middle_page_sum)

if __name__ == "__main__":
    main()