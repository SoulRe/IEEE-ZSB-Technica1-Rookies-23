x = str(input("Input :\n"))
y = str(" ")
for i in x:
    if i not in y:
        y += i
        print(i, end = " ")   
        