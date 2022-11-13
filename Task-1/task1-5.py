n = int(input("Enter a number: "))
sum1 = 0
for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        sum1 += i

print(f"Sum = {sum1}")