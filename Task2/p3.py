def sequence(usin):
    #finding the index of each of the chars of hello
    try:
        h = usin.index('h')
        e = usin.index('e')
        o = usin.rindex('o')
        #checking if 'll' exists between e and o
        ll = usin.rindex('ll', e, o)
    except ValueError:
        return False
    
    #checking if the chars are indexed correctly
    if h < e < ll < o:
        return True
    return False
        

def main():
    userinput = str(input("Input :\n"))
    x = sequence(userinput)
    if x:
        print("YES")
        exit(0)
    print("NO")
    exit(0)
    

main()