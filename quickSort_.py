import time

# O(Nlog(N)) Time Complexity
# O(N) Space Complexity (Worst Case) and O(logN) Space Complexity average case
def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, getColourArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for i in range(head, tail): 
        if data[i] < pivot: 
            drawData(data, getColourArray(len(data), head, tail, border, i, True)) # calling visualisation function
            time.sleep(timeTick)
            data[border], data[i] = data[i], data[border] 
            border += 1
        drawData(data, getColourArray(len(data), head, tail, border, i))
        time.sleep(timeTick)
    # swap pivot with border
    drawData(data, getColourArray(len(data), head, tail, border, tail, True)) # calling visualisation function
    time.sleep(timeTick) 

    data[border], data[tail] = data[tail], data[border]
    return border 

def quickSort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIndex = partition(data, head, tail, drawData, timeTick) 

        # LEFT PARTITION
        quickSort(data, head, partitionIndex-1, drawData, timeTick)

        # RIGHT PARTITION 
        quickSort(data, partitionIndex+1, tail, drawData, timeTick)

def getColourArray(dataLength, head, tail, border, currentIndex, isSwapping=False):
    colourArray = [] 
    for i in range(dataLength):
        #base colouring 
        if i <= head and i <= tail: 
            colourArray.append('#eca1ff') # partially sorted lighter pink
        else:
            colourArray.append('#3ea9f0') # blue 
        if i == tail: 
            colourArray[i] = '#0a8cc4' # pivot, darker blue 
        elif i == border: 
            colourArray[i] = '#03fc77'  # green 
        elif i == currentIndex:
            colourArray[i] = '#de2c3b' # red 
        
        if isSwapping: 
            if i == border or i == currentIndex: 
                colourArray[i] = '#03fc77' # green for selected elements 
    return colourArray  