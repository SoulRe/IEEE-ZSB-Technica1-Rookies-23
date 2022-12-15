def fliplights(i, j, lightmatrix):
    #vertical neighbouring lights
    for v in range(i - 1, i + 2):
        if v < 0: continue
        if v > 2: break
        if lightmatrix[v][j] == 0:
            lightmatrix[v][j] = 1
        else:
            lightmatrix[v][j] = 0
    #horizontal neighbouring lights
    for h in range(j - 1, j + 2):
        if h < 0 or h == j: continue
        if h > 2: break
        if lightmatrix[i][h] == 0:
            lightmatrix[i][h] = 1
        else: lightmatrix[i][h] = 0
        
    return lightmatrix


def main():
    lightmatrix = [[1,1,1],[1,1,1],[1,1,1]]
    # for i in range(3):
    #     print(lightmatrix[i])
    
    switchmatrix = []
    for i in range(3):
        switchmatrix.append(list(map(int, input().split())))
    # print(switchmatrix)
    
    for i in range(3):
        for j in range(3):
            if switchmatrix[i][j] != 0 and switchmatrix[i][j]%2 != 0:
                fliplights(i, j, lightmatrix)
    
    for i in range(3):
        for j in range(3):
            print(lightmatrix[i][j], end = "")
        print()    
    
main()