secret_word = "XMAS"
def main():
    with open('./input.txt', 'r') as lines:
        matrix = [[str(y) for y in x.strip()] for x in lines.readlines()]
        total_xmas = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'A' and i - 1 >= 0 and i + 1 < len(matrix) and j - 1 >= 0 and j + 1 < len(matrix[0]):

                    word1 = matrix[i-1][j-1] + matrix[i][j] + matrix[i+1][j+1]
                    word2 = matrix[i-1][j+1] + matrix[i][j] + matrix[i+1][j-1]
                    
                    if is_equal_secret("MAS", word1) and is_equal_secret("MAS", word2):
                        total_xmas += 1


                   
                        

        print(total_xmas)

def is_equal_secret(secret_word, word_arr):
    word = "".join(word_arr)
    return word == secret_word or word[::-1] == secret_word


if __name__ == "__main__":
    main()