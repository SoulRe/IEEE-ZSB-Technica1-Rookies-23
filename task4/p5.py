def get_input():
    global matrix_size
    matrix_size = int(input("Input: \n"))
    matrix = []
    for i in range(matrix_size):
        matrix.append(input().split())
    return matrix


def rotate_matrix(matrix):
    newmatrix = []
    for i in range(matrix_size):
        for j in reversed(range(matrix_size)):
            newmatrix.append(matrix[j][i])
            
    return newmatrix            


def return_output(newmatrix):
    for i in range(len(newmatrix)):
        print(newmatrix[i], end=" ")
        if (i+1)%matrix_size == 0 :
            print()


def main():
    matrix = get_input()
    newmatrix = rotate_matrix(matrix)
    print("output:")
    return_output(newmatrix)
    
    
main()