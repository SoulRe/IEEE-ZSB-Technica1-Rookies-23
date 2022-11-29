def get_input(): 
    global bottlenum
    bottlenum = int(input("Bottles num: "))
    bottles = []
    for i in range(bottlenum):
        bottles.append(input().split(" "))
    return bottles


def bottlesort(bottles):
    for i in range(bottlenum - 1):
        for j in range(i + 1, bottlenum):
            if bottles[j][1] < bottles[i][1]:
                switch = bottles[i]
                bottles[i] = bottles[j]
                bottles[j] = switch
    return bottles
    

def bottlecalc(bottles):
    filled = capacity = 0
    bottles = bottlesort(bottles)
    for i in range(bottlenum):
        filled += int(bottles[i][0])
    capacity += int(bottles[bottlenum - 1][1]) + int(bottles[bottlenum - 2][1])
    
    if capacity > (capacity - filled):
        print("Yes")
        exit(0)
    print("No")
    exit(0)
    
    
def main():
    bottles = get_input()
    bottlecalc(bottles)
    

main()