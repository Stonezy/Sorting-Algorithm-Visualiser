import time
# O(Nlog(N)) Time Complexity
# O(N) Space Complexity 
def mergeSort(data, drawData, timeTick): 
    mergeSortAlg(data, 0, len(data)-1, drawData, timeTick)

def mergeSortAlg(data, left, right, drawData, timeTick): 
    if left < right: 
        midpoint = (left + right) // 2
        mergeSortAlg(data, left, midpoint, drawData, timeTick)
        mergeSortAlg(data, midpoint+1, right, drawData, timeTick)
        merge(data, left, midpoint, right, drawData, timeTick)

def merge(data, left, midpoint, right, drawData, timeTick): 
    drawData(data, getColourArray(len(data), left, midpoint, right))
    time.sleep(timeTick)

    leftPart = data[left:midpoint+1]
    rightPart = data[midpoint+1:right+1]

    left_pointer = right_pointer = 0 

    for i in range(left, right+1): 
        if left_pointer < len(leftPart) and right_pointer < len(rightPart): 
            if leftPart[left_pointer] < rightPart[right_pointer]: 
                data[i] = leftPart[left_pointer]
                left_pointer += 1
            else: 
                data[i] = rightPart[right_pointer]
                right_pointer += 1 
        elif left_pointer < len(leftPart): 
            data[i] = leftPart[left_pointer]
            left_pointer += 1 
        else: 
            data[i] = rightPart[right_pointer]
            right_pointer += 1 
    drawData(data, ["#f274fc" if x >= left and x <= right else "#3ea9f0" for x in range(len(data))])
    time.sleep(timeTick)
def getColourArray(length, left, middle, right): 
    colourArray = [] 
    for i in range(length): 
        if i >= left and i <= right: 
            if i <= middle: 
                colourArray.append("#03fc77") # green
            else:
                colourArray.append("#f274fc") # pink 
        else: 
            colourArray.append("#3ea9f0") # blue

    return colourArray