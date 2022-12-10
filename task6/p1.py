def check_divisors(numbers):
    divisors = []
    for i in range(len(numbers)):
        counter = 0
        number = numbers[i]
        for j in numbers[i]:
            if j == '0':
                continue
            if int(number)%int(j) == 0:
                counter += 1
        divisors.append(counter)
    return divisors
    

def print_divisors(divisors):
    for i in divisors:
        print(i)
        
        
def main():
    iterations = int(input())
    numbers = []
    for i in range(iterations):
        numbers.append(input())
        
    divisors = check_divisors(numbers)
    print_divisors(divisors)
    
    
main()