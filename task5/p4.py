def get_primes(number):
    primes = []
    for i in range(2, number):
        for j in range(2, int(i**.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes


def check_even_odd(number):
    while number%2 == 0:
        number /= 2
        print(2, end = " ")
    return int(number)
    
    
def check_factor(number, primes):
    for i in reversed(primes):
        while number%i == 0:
            number /= i
            print(i, end = " ")
            

def main():
    number = int(input("Input: "))
    primes = get_primes(number)
    number = check_even_odd(number)
    check_factor(number, primes)
    
    
main()