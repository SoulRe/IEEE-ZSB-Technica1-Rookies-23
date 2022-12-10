def count_days(number_of_days, seconds_needed, input2):
    counter = 0
    usedtime = 0
    for i in range(number_of_days):
        freetime = 86400 - input2[i]
        usedtime += freetime
        counter += 1
        if usedtime >= seconds_needed:
            return counter
    

def main():
    input1 = list(map(int, input().split()))
    number_of_days = input1[0]
    seconds_needed = input1[1]
    input2 = list(map(int, input().split()))
    
    count = count_days(number_of_days, seconds_needed, input2)
    print(count)
    
    
main()
    