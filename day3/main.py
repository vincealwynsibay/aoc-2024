def main():
    with open("./input.txt", 'r') as inputs:
        data = inputs.read()
        total_product = 0
        
        i = 0
        while i < len(data):
            num1 = ""
            num2 = ""

            if len(data[i:]) > 4 and data[i] == "m":
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
                    
                    total_product += (int(num1) * int(num2))
            i += 1



        print(total_product)



if __name__ == "__main__":
    main()