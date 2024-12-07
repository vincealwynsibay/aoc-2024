secret_word = "XMAS"
def main():
    with open('./input.txt', 'r') as lines:
        matrix = [[str(y) for y in x.strip()] for x in lines.readlines()]
        total_xmas = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == 'X':

                    # check 3 steps to the right
                    if j + 3 < len(matrix[0]):
                        if is_equal_secret(matrix[i][j:j+4]):
                            total_xmas += 1

                    # check 3 steps to the left
                    if j - 3 >= 0:
                        if is_equal_secret(matrix[i][j-3:j+1]):
                            total_xmas += 1
                        
                    # check 3 steps above
                    if i - 3 >= 0:
                        word = ""
                        for k in range(i, i-4, -1):
                            word += matrix[k][j]
                        if is_equal_secret(word):
                            total_xmas += 1

                    # check 3 steps below
                    if i + 3 < len(matrix):
                        word = ""
                        for k in range(i, i+4):
                            word += matrix[k][j]
                        if is_equal_secret(word):
                            total_xmas += 1

                    # check 3 steps top left
                    if i - 3 >= 0 and j - 3 >= 0:
                        word = ""
                        for k in range(0, 4):
                            word += matrix[i-k][j-k]
                        if is_equal_secret(word):
                            total_xmas += 1

                    # check 3 steps top right
                    if i - 3 >= 0 and j + 3 < len(matrix[0]):
                        word = ""
                        for k in range(0, 4):
                            word += matrix[i-k][j+k]
                        if is_equal_secret(word):
                            total_xmas += 1

                    # check 3 steps bottom left
                    if i + 3 < len(matrix) and j - 3 >= 0:
                        word = ""
                        for k in range(0, 4):
                            word += matrix[i+k][j-k]
                        if is_equal_secret(word):
                            total_xmas += 1

                    # check 3 steps bottom right
                    if i + 3 < len(matrix) and j + 3 < len(matrix[0]):
                        word = ""
                        for k in range(0, 4):
                            word += matrix[i+k][j+k]
                        if is_equal_secret(word):
                            total_xmas += 1
                        

        print(total_xmas)

def is_equal_secret(word_arr):
    word = "".join(word_arr)
    return word == secret_word or word[::-1] == secret_word


if __name__ == "__main__":
    main()