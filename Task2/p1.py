import random

#function to iterate over the user's input and check if it's in the random number
def numcheck(userin, num):
        hit = miss = 0
        for i in range(len(userin)):
            if userin[i] == num[i]:
                hit += 1
            else:
                miss += 1
        print(num)
        print(f"{hit} hit {miss} miss")

def getinput():
        usin = input("Enter a 3 digit number :\n")
        if usin.isdecimal:
            return usin
    
def main():
    #making a random number and getting input from user
    number = str(random.choice(range(0, 999))).zfill(3)
    userinput = getinput()
    
    #running the function and printing num of hits and misses
    numcheck(userinput, number)
    
    #checking if the input is correct or not 
    while(userinput != number):
        userinput = getinput()
        numcheck(userinput, number)
        
        #exiting in case of correct input
        if(userinput == number):
            exit(0)
        
main()
