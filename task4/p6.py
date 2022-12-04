def get_input():
    number = list(input("input: \n"))
    return number


def check_num(number):
    number = int(''.join(number))
    if number < 1000:
        number *= 10
    elif number < 100:
        number *= 100 
    elif number < 10:
        number *= 1000
    
    return str(number)
    
    
def get_ascending(number):
    ascending = ''.join(sorted(number))
    return int(ascending)


def get_descending(number):
    descending = ''.join(sorted(number, reverse = True))
    return int(descending)
    
    
def get_steps(number, counter):
    number = check_num(number)
    ascending = get_ascending(number)
    descending = get_descending(number)
    difference = descending - ascending
    counter += 1
    # print(descending, ascending, difference, number, counter)
    if difference == 6174:
        print("Output: ")
        print(counter)
        exit(0)
    number = str(difference)
    get_steps(number, counter)


def main():
    number = get_input()
    steps = 0
    get_steps(number, steps)
 
 
main()