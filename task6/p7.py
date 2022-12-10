def check_for_triplets(array, length, difference):
    triplets = []
    for i in range(length):
        # print(array[i])
        for j in range(i+1, length):
            # print(array[j])
            if array[j] == array[i] + difference:
                for k in range(j+1, length):
                    if array[k] == array[j] + difference:
                            triplets.append([array[i], array[j], array[k]])
                            if k == length - 1:
                                return triplets
                            break
    return triplets
    
def main():
    inputs = list(map(int, input().split()))
    length = inputs[0]
    difference = inputs[1]
    
    array = list(map(int, input().split()))
    
    check = check_for_triplets(array, length, difference)
    
    print(len(check))
    
    
main()