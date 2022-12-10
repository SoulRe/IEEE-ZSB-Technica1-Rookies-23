def deletefreind(popularity, friendsnum):
    for i in range(friendsnum - 1):
        if popularity[i] < popularity[i + 1]:
            popularity.pop(i)
            # print(popularity)
            return popularity
    

def main():
    testcases = int(input())
    for i in range(testcases):
        input1 = list(map(int, input().split()))
        friendsnum = input1[0]
        iterations = input1[1]
        popularity = list(map(int, input().split()))
        check = 0
        for i in range(iterations):
            popularity = deletefreind(popularity, friendsnum)
        for i in range(len(popularity)):
            print(popularity[i], end = " ")
        print()
                      
                      
main()