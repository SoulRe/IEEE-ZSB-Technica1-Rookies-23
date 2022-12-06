def get_input():
    
    string = input("Input: ")
    return string


def check_bracket(string):
    
    condition = False
    size = len(string)
    
    if size % 2 != 0:
        return False
    
    for i in range(size//2):
        if ord(string[i]) != 40 and ord(string[i]) == ord(string[size - 1 - i]) - 2:
            condition = True
            continue
        elif ord(string[i]) == 40 and ord(string[i]) == ord(string[size - 1 - i]) - 1:
            condition = True
            continue
        condition = False
    return condition

def main():
    
    string = get_input()
    condition = check_bracket(string)
    print(condition)
    

main()