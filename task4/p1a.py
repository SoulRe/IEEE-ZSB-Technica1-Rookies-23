def get_input():
    #first line input , info[0] = arraysize, info[1] = number of elements to print
    info = input("Input: \n").split()
    array = input().split()
    
    global elenum, size
    size = int(info[0])
    elenum = int(info[1])
    
    return array


def check_frequency(array):
    array.sort()
    freq = {i:array.count(i) for i in array}
    return freq


def print_numbers(frequency):
    items = []
    for key, value in frequency.items():
        items.append(key)
        #printing numbers
    for i in range(elenum):
        print(items[i], end = " ")

def main():
    array = get_input()
    frequency = check_frequency(array)
    print_numbers(frequency)

main()
    