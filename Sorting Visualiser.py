from tkinter import * 
from tkinter import ttk 
import random
from bubbleSort_ import bubbleSort 
from insertionSort import insertSort
from quickSort_ import quickSort
from mergeSort_ import mergeSort

root = Tk() 

root.title('Sorting Algorithm Visualiser')
root.maxsize(900, 800)
root.config(bg='black')

# Variables
selected_aglo = StringVar()     
data = []

def drawData(data, colorArray):
    canvas.delete("all")
    canvas_height = 380
    canvas_width = 800
    x_width = canvas_width / (len(data) + 1)
    offset = 8
    spacing = 5 

    normalisedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalisedData):
        #top left corner
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 340
        #bottom right
        x1 = (i+1) * x_width + offset 
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()
def Generate():
    global data #global data array since we have seperate buttons for generating the array and for starting the sort
    # getters 
    minVal = int(minEntry.get())  
    maxVal = int(maxEntry.get()) 
    size = int(sizeEntry.get())

    data = [] #reset all data, clearing the array
    for _ in range(size): 
        data.append(random.randrange(minVal, maxVal+1)) #generate new data
    drawData(data, ['#3ea9f0' for x in range(len(data))]) # creates array of ['blue', 'blue', ..n] times 

def StartAlgorithm(): 
    global data
    if algoMenu.get() == "Bubble Sort": 
        bubbleSort(data, drawData, speedScale.get())
    elif algoMenu.get() == "Insertion Sort": 
        insertSort(data, drawData, speedScale.get())
    elif algoMenu.get() == "Quick Sort": 
        quickSort(data, 0, len(data)-1, drawData, speedScale.get())
    elif algoMenu.get() == "Merge Sort": 
        mergeSort(data, drawData, speedScale.get())
    
    drawData(data, ['#f274fc' for x in range(len(data))]) 
    print("Starting Algorithm")

# frame / base layout

UI_frame = Frame(root, width=800, height=200, bg='grey') # create a frame for the UI to be situated 
UI_frame.grid(row=0, column=0, padx=10, pady=5) #draw, position and pad the grid 

canvas = Canvas(root, width=800, height=380, bg='white') # create canvas to plot data on 
canvas.grid(row=1, column=0, padx=10, pady=5) # position canvas and add padding 

# UI Area
# Row[0] 
Label(UI_frame, text='Algorithm: ', bg='grey').grid(row=0, column=0, padx=5, pady=0, sticky=W) # labels
algoMenu = ttk.Combobox(UI_frame, textvariable=selected_aglo, values=['Bubble Sort', 'Merge Sort', 'Insertion Sort', 'Quick Sort']) #dropdown menu 
algoMenu.grid(row=0, column=1, padx=5, pady=5) #drawing the menu
algoMenu.current(0) #by default display the first value in the menu (index[0])

speedScale = Scale(UI_frame, from_=0.01, to=0.5, length=200, digits=2, resolution=0.01, orient=HORIZONTAL, label="Select Sorting Speed [s]") #create a scale for the sorter's speed
speedScale.grid(row=0, column=2, padx=5, pady=5) #draw the scale 

Button(UI_frame, text="Start", command=StartAlgorithm, bg='#3ea9f0').grid(row=0, column=3, padx=5, pady=5) # start button which initates the sort

# Row[1]   
sizeEntry = Scale(UI_frame, from_=3, to=50, resolution=1, orient=HORIZONTAL, label="Data Size") # size scale
sizeEntry.grid(row=1, column=0, padx=5, pady=5) 

minEntry = Scale(UI_frame, from_=1, to=10, resolution=1, orient=HORIZONTAL, label="Minimum Value") # Minimum value scale
minEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W) 

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Maximum Value") # Maximum value scale
maxEntry.grid(row=1, column=2, padx=5, pady=5) 

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5) # Generate array button
root.mainloop() #infinite loop used to run the application - waits for events from the user and exits loop when closed. 