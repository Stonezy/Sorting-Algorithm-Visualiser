import time
# O(Nlog(N)) time complexity
def createHeap(arr, size, i, drawData, timeTick): 
    largest = i # Initialize largest as root 
    left = 2 * i + 1     # left = 2*i + 1 
    right = 2 * i + 2     # right = 2*i + 2 
    drawData(arr, getColourArray(len(arr), i, left, right))
    time.sleep(timeTick)
    # See if left child of root exists and is 
    # greater than root 
    if left < size and arr[i] < arr[left]: 
        largest = left 
  
    # See if right child of root exists and is 
    # greater than root 
    if right < size and arr[largest] < arr[right]: 
        largest = right 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
        drawData(arr, getColourArray(len(arr), i, left, right))
        time.sleep(timeTick)        
        # createHeap the root. 
        createHeap(arr, size, largest, drawData, timeTick) 
  
# The main function to sort an array of given size 
def heapSort(arr, drawData, timeTick): 
    size = len(arr) 
  
    # Build a maxheap. 
    for i in range(size//2 - 1, -1, -1): 
        createHeap(arr, size, i, drawData, timeTick) 
  
    # One by one extract elements 
    for i in range(size-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        createHeap(arr, i, 0, drawData, timeTick)

def getColourArray(size, i, left, right): 
    colourArray = [] 

    for j in range(size): 
        if j == i: 
            colourArray.append("#03fc77") # green elements are selected
        else:
            colourArray.append("#3ea9f0") # blue
    return colourArray