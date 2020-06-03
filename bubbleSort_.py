import time
# O(N^2) Time Complexity 
# O(1) Space Complexity 
def bubbleSort(data, drawData, timeTick):
    for i in range(0, len(data) - 1): 
        for j in range(0, len(data) - 1 - i): 
            if data[j] > data[j+1]: 
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['#03fc77' if x == j or x == j + 1 else '#3ea9f0' for x in range(len(data))])
                time.sleep(timeTick)