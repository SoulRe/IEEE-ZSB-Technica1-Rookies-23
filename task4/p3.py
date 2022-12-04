def get_input():
    numbers = input("Input: \n").split()
    return numbers


def get_distance(numbers):
    distance = 100
    check = 0
    for i in range(len(numbers) - 1):
        for j in range(i + 1,len(numbers)):
            if numbers[i] == numbers[j]:
                check = abs(j - i)
                if check < distance:
                    distance = check
    
    return distance
    

def main():
    numbers = get_input()
    distance = get_distance(numbers)
    print(distance)
    
    
main()