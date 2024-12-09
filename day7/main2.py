from itertools import product

def main():
    with open('./input.txt', 'r') as data:
        lines = data.readlines()

        total = 0
        for line in lines:
            target, nums = line.split(":")
            target = int(target)
            nums = nums.strip().split(" ")
            
            for equations in product(["*", "+", "||"], repeat=len(nums)-1):
                expression = nums[0]
                curr = nums[0]
                for i in range(1, len(nums)):
                    if equations[i - 1] == "+":
                        curr = int(curr) + int(nums[i])
                    elif equations[i - 1] == "*":
                        curr = int(curr) * int(nums[i])
                    elif equations[i - 1] == "||":
                        curr = int(str(curr) + nums[i])
                if curr == target:
                    print(target)
                    total += curr
                    break
            
        print(total)
            



        
if __name__ == "__main__":
    main()