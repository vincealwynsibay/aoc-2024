def main():
    with open("./input.txt", 'r') as inputs:
        data = inputs.read()
        total_product = 0
        
        i = 0
        is_enabled = True
        while i < len(data):
            num1 = ""
            num2 = ""

            if data[i] == "d":
                if data[i:i+4] == "do()":
                    is_enabled = True
                    i += 4
                    continue
                elif data[i:i+7] == "don't()":
                    is_enabled = False
                    i += 7
                    continue
            elif len(data[i:]) > 4 and data[i] == "m":
                if  data[i:i+4] == "mul(":
                    i = i + 4
                    # first num
                    while i < len(data) and data[i].isdigit():
                        num1 += data[i]
                        i += 1

                    if not num1 or len(num1) > 3 or i >= len(data) or  not data[i] == ",": 
                        continue

                    i += 1

                    # second num
                    while i < len(data) and data[i].isdigit():
                        num2 += data[i]
                        i += 1
                    if not num2 or len(num2) > 3 or i >= len(data) or  not data[i] == ")": 
                        continue
                    
                    if is_enabled:
                        total_product += (int(num1) * int(num2))
            i += 1



        print(total_product)



if __name__ == "__main__":
    main()