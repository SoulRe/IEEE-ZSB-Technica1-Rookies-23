def get_input():
    #takes input for num of students and adds data into a nested list
    global studentnum
    studentnum = int(input())
    p = []*studentnum
    #adding data where p[i][0] = name, p[i][1] = degree 
    for i in range(studentnum):
        name = str(input())
        degree = float(input())
        p.append([name, degree])
        
    return p
    
#sorting the list based on degrees
def sort(p):
    for i in range(studentnum - 1):
        for j in range(i + 1, studentnum):
            if p[j][1] < p[i][1]:
                switch = p[i]
                p[i] = p[j]
                p[j] = switch
            
    return p
    
#getting students with similar degrees, sorting them alphabetically and printing their names
def getdegree(p):
    secondlast = 0
    sortednames = []
    for i in range(studentnum):
        if p[i][1] == p[0][1]:
            continue
        else:
            secondlast = p[i][1]
            break
            
    for i in range(studentnum):
        if p[i][1] == secondlast:
            sortednames.append(p[i])
    
    sortednames.sort()
    for i in range(len(sortednames)):
        print(sortednames[i][0])
            
# main function to call all other functions 
def main():
    p = get_input()
    
    p = sort(p)
    
    getdegree(p)

main()