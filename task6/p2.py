def main():
    return_date = input().split()
    due_date = input().split()
    fines = [15, 500, 10000]
    
    fine = 0
    for i in reversed(range(3)):
        date = int(return_date[i]) - int(due_date[i])
        if date < 0:
            break
        elif date > 0:
            fine = date * fines[i]
            break
        
    print(fine)


main()
    