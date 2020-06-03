import time
# O(N^2) Time Complexity 
# O(1) Space Complexity 
def insertSort(data, drawData, timeTick): 
    for i in range (len(data)): 
        j = i 
        while j > 0 and data[j-1] > data[j]: 
            data[j-1], data[j] = data[j], data[j-1]
            j -= 1
            drawData(data, ['#03fc77' if x == j or x == j + 1 else '#3ea9f0' for x in range(len(data))])
            time.sleep(timeTick)