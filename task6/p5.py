def checkinstance(sentences):
    try:
        h = sentences.index('h')
        a = sentences.index('a',h)
        c = sentences.index('c',a)
        k = sentences.index('k',c)
        e = sentences.index('e',k)
        r = sentences.index('r',e)
        r2 = sentences.index('r', r + 1)
        a2 = sentences.index('a',r2)
        n2 = sentences.index('n',a2)
        k2 = sentences.rindex('k')
    except ValueError:
        return "NO"
    
    # print(h,a,c,k,e,r,r2,a2,n2,k2)
    if h < a < c < k < e < r < r2 < a2 < n2 < k2:
        return "YES"
    else :
        return "NO"
    
def main():
    numofsentences = int(input())
    check = []
    for i in range(numofsentences):
        sentences = str(input())
        check.append(checkinstance(sentences))
    
    for i in range(numofsentences):
        print(check[i])


main()