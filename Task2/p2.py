def palindrome(usin):
    checkchar = bool(0)
    for i in usin:
        for j in reversed(usin):
            if i == j:
                checkchar = 1
            else:
                checkchar = 0
    return checkchar
            

def main():
    userinput = str(input("Input : \n"))
    x = palindrome(userinput)
    
    if (x):
        print("yes")
        exit(0)
    print("no")
    exit(0)


main()