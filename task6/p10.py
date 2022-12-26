"""Couldn't solve , got help but i understand how it works"""
def main():
    testcases = int(input())
    #doing this case by case (dynamically)
    for i in range(testcases):
        #self explanatory just getting input as adviced in problem
        input1 = list(map(int, input().split()))
        friendsnum = input1[0]
        iterations = input1[1]
        popularity = list(map(int, input().split()))
        
        #making the new list of inputs
        newlist = []
        #looping through the list of inputted popularity
        for i in popularity:
            #checking if the num of friends to remove isn't = 0
            #checking if there is a newlist of friends (newlist)
            #checking if the last item is bigger than current value in popularity
            #if so
            while iterations and newlist and newlist[-1] < i:
                #remove the last item
                newlist.pop(-1)
                #decreasing the iterations by 1
                iterations -= 1
            #whatever happens we append the current value of i
            newlist.append(i)
            # print(newlist)
        #just printing
        for i in newlist:
            print(i, end = " ")
                      
main()