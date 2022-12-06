def check_number(number):
    sum = 0
    for i in number:
        sum += int(i)**2
        
    if sum == 1:
        print("true")
        return True
    
    if sum == 4:
        print("false")
        return False
    check_number(str(sum))
    

def main():
    number = input("Input: ")
    counter = 0
    check_number(number)
    
    
main()