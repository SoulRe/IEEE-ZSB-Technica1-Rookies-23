def main():
    year = int(input())
    check = True
    #While this isn't Truly Dynamic it still satisfies the input conditions
    for i in range(year + 1, 10000):
        currentyear = str(i)
        #starting from the back to check
        for j in reversed(range(4)):
            #checking if current digit is in the rest of the year
            if currentyear[j] in currentyear[0:j]:
                check = False
                break
            check = True
        if check == False:
            continue
        print(currentyear)
        break
        
        
main()
        