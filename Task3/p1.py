def get_input():
    global lines
    lines = int(input("Matrix Size: "))
    
    matrix = []*lines
    columns = 0
    
    for i in range(lines):
         columns = input().split(" ")
         matrix.append(columns)
    
    print(matrix)
    return matrix
    
def get_diagonal_sum(matrix):
    sum1 = sum2 = 0
    
    for i in range(lines):
        sum1 += int(matrix[i][i])
        sum2 += int(matrix[i][lines - i - 1])
    summ = abs(sum1 - sum2)
    return summ

def main():
    matrix = get_input()
    summ = get_diagonal_sum(matrix)
    
    print(summ)
    

main()