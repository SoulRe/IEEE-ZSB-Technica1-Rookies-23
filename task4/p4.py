def get_input():
    n = input("Input: \n")
    number = input().split()
    return number


def increment_by_one(number):
    newnumber = []
    for i in reversed(range(len(number))):
        j = int(number[i]) + 1
        
        if str(0) in str(j):
            number[i] = '0'
            newnumber.append(0)
            if i == 0:
                newnumber.append(1)
            continue
        #else add the number into a different list and append the rest of the numbers list to it
        newnumber.append(j)
        for x in reversed(range(len(number) - 1)):
            newnumber.append(number[x])
        break
    
    return newnumber


def return_output(newnumber):
    for i in reversed(range(len(newnumber))):
        print(newnumber[i], end=" ")


def main():
    number = get_input()
    newnumber = increment_by_one(number)
    return_output(newnumber)
    

main()