def rotate_array(array, num_of_elements, rotation_count):
    array2 = []
    for i in range(num_of_elements - rotation_count, num_of_elements):
        array2.append(array[i])
    for i in range(num_of_elements - rotation_count):
        array2.append(array[i])
    # print(array2)
    return array2


def main():
    inputs = list(map(int, input().split()))
    num_of_elements = inputs[0]
    rotation_count = inputs[1]
    num_of_queries = inputs[2]
    queries = []
    
    if rotation_count > num_of_elements:
        rotation_count -= ((rotation_count//num_of_elements)*num_of_elements)
        # print(rotation_count)
    array = list(map(int, input().split()))
    
    array = rotate_array(array, num_of_elements,rotation_count)
        
    for i in range(num_of_queries):
        queries.append(int(input()))
        
    for i in range(num_of_queries):
        print(array[queries[i]])
        

main()
    
    