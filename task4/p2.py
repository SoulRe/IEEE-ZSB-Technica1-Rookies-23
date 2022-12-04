import itertools
def main():
    
    letters = str(input("letters: "))
    strings = str(input("String to check: "))
    
    check = []
    permutations = list(itertools.permutations(letters))
    check.append(''.join(permutations) for permutation in permutations)
    print(check[0])
    
    for i in range(len(check)):
        if check[i] in strings:
            check = True
            break
        else:
            check = False
            
    print(check)
        

main()