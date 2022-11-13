a = int(input("Enter first number: "))
b = int(input("Enter first number: "))

smaller = b+1
if a > b:
    samller = a+1

for i in range(1,smaller):
    if a%i == 0 and b%i == 0:
        div = i
        
print(f"Number is: {div}")