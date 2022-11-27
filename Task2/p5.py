                            #INSERTION SORT#
"""Starting off i will explain what a stable sorting algorithm is.
    A stable sorting algorithm is one where the relative order of items
    should the be equal in value is maintained.
    
    Insertion sort is a stable sorting algorithm because it satisfies the
    condition previously stated.
    
    The time complexity of insertion sort is : O(n^2) on average,
        however it's best time complexity is : O(n).
        
    space complexity for such a sorting algorithm is : 1 (constant)
    """
    
'''In the following program you will find my implementation of the 
   Insertion sort algorithm .
   The following is a brief explanation from my understanding of it:
   '''
   ###Explanation###
   '''The sorting in this algorithm is quite interesting as i haven't 
      seen it before but it function in a way that "inserts" an element
      from an unsorted area of an array and into a sorted part of such 
      array.
      
      the indexing for elements starts from 1 which is the second element
      in the array and compares it to the value of the element before it
      should the value before it be bigger it replaces the positions of the 
      two like what's done in bubble sort.
      
      the algorithm then checks every 2 pairs while increasing the index
      of the checked element by 1 should there be no unsorted pairs
      
      should the array find an element like the number 5 below it proceedes
      to exchange it's position with the previous element and does so 
      repeatedly until it's setteled in it's correct position.'''

def insertionsort(arr):
    
    for i in range(1, len(arr)):
        element = arr[i]
        j = i - 1
        while j >= 0 and element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = element
    
    
arr = [12, 11, 13 ,5 ,6]
insertionsort(arr)

for i in range(len(arr)):
    print("% d" % arr[i])