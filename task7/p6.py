def kaprekar_number(i, check):
    length = len(i)
    square = str(int(i)**2)
    if len(square) != 2*length:
        if len(square) != 2*length - 1:
            return 
    # print(i, square)
    rightHalf = square[len(square) - length:]
    leftHalf = square[:len(square) - length]
    if leftHalf == "":
        leftHalf = 0
    # print(leftHalf, rightHalf)
    if int(rightHalf) + int(leftHalf) != int(i):
        return check
    print(i, end = " ")
    check = True
    


def main():
    #lower and upper limit respectively
    p = int(input())
    q = int(input())
    check = False
    for i in range(p, q + 1):
        i = str(i)
        check = kaprekar_number(i,check)
    
    if check == False:
        print("INVALID RANGE")
        
main()