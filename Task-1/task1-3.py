listsize = int(input("Enter list size: "))

numlist = []

for i in range(listsize):
    n = int(input("Enter a number: "))
    numlist.append(n)
    
def loopsum():
    global sum1
    sum1 = 0
    for a in numlist:
        sum1 += a
    return sum1

loopsum()
print(f"Loop sum = {sum1}")

def whilesum():
    sum1 = 0
    l = 0
    while l < len(numlist):
        sum1 += numlist[l]
        l += 1
    return sum1
    
whilesum()
print(f"While sum = {sum1}")

def recursum():
    sum1 = 0
    n = len(numlist) - 1
    if (n < 0):
        exit
    sum1 += numlist[n]
    n = n - 1 
    return sum1

recursum()
print(f"Recursion sum = {sum1}")