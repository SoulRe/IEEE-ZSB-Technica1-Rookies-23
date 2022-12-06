def create_heap(heap, size, i):
    largest = i
    leftchild = 2 * i + 1
    rightchild = 2 * i + 2
    
    if leftchild < size and heap[leftchild] > heap[largest]:
        largest = leftchild
        
    if rightchild < size and heap[rightchild] > heap[largest]:
        largest = rightchild
        
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        
        create_heap(heap, size, largest)
        

def main():
    heap = input().split()
    heap = [int(item) for item in heap]
    
    size = len(heap)
    itera = int(len(heap) / 2)
    for i in range(itera, -1 , -1):
        create_heap(heap, size, i)
    for i in heap:
        print(i, end = " ")
main()





