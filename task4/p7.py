from collections import defaultdict

def get_input():
    wordcount = int(input("Input: \n"))
    words = []
    for i in range(wordcount):
        words.append(str(input()))
    
    return words

    
def main():
    words = get_input()
    temp = defaultdict(list)
    for ele in words:
        temp[str(sorted(ele))].append(ele)
    res = list(temp.values())
    
    print("Output: ")
    for i in range(len(res)):
        for j in range(len(res[i])):
            print(res[i][j], end =" ")
        print()
        
        
main()