def main():
    ternary_number = input()
    decoding_list = [',','-.', '--']
    check = 0
    for i in range(len(ternary_number)):
        if check == 1:
            check = 0
            continue
        if i == len(ternary_number) - 1:
            print(0, end = "")
            break 
        num = ternary_number[i] + ternary_number[i+1]
        # print(num)
        if num in decoding_list:
            print(decoding_list.index(num), end = "")
            check = 1
        else:
            print(0, end = "")
            
main()