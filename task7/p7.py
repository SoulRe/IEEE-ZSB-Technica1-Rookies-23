def chocolates_eaten(money, price, wrappersneeded):
    chocolates= money // price
    wrappers = chocolates
    while wrappers >= wrappersneeded:
        chocolates += 1
        wrappers -= wrappersneeded
        wrappers += 1
    print(chocolates)
    
    
def main():
    testcases = int(input())
    for i in range(testcases):
        inputline = list(map(int, input().split()))
        money, price, wrappersneeded = inputline[0], inputline[1], inputline[2]
        # print(money, price, wrappersneeded)
        
        chocolates_eaten(money, price, wrappersneeded)
        
        
main()