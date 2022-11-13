n = str(input("Enter the number: "))

check = False
lenn = int(len(n))
revn = []

for i in range(lenn):
    for j in range(lenn - 1, -1, -1):
        if n[i] == n[j]:
            check = True
        else:
            check = False
            
        if n[j] != '0':
            revn.append(n[j])
        i += 1
    break

if check:
    for i in range(len(revn)):
        print(revn[i], end = "")
    print()
    print("YES")
    exit(0)
    
for i in range(len(revn)):
        print(revn[i], end = "")
print()
print("NO")
 