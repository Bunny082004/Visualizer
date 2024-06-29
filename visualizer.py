from tkinter import *
from tkinter import ttk
import random
import time

# Global variables
array = []
canvas_height = 400
canvas_width = 600
bar_width = 5
bar_gap = 2

def draw_bars(canvas, array, color_array):
    canvas.delete("all")
    canvas_height = int(canvas.cget("height"))
    canvas_width = int(canvas.cget("width"))
    bar_width = canvas_width / len(array)
    for i, val in enumerate(array):
        x0 = i * bar_width
        y0 = canvas_height - val
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
    root.update_idletasks()

def bubble_sort(canvas, array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            draw_bars(canvas, array, ["red" if x == j or x == j+1 else "white" for x in range(len(array))])
            time.sleep(0.01)

def merge_sort(canvas, array, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(canvas, array, start, mid)
        merge_sort(canvas, array, mid, end)
        merge(canvas, array, start, mid, end)
        draw_bars(canvas, array, ["green" if start <= x < end else "white" for x in range(len(array))])
        time.sleep(0.1)

def merge(canvas, array, start, mid, end):
    left = array[start:mid]
    right = array[mid:end]
    k = start
    i = j = 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            array[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            array[k] = right[j]
            j = j + 1
            k = k + 1

def partition(canvas, array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
        draw_bars(canvas, array, ["blue" if x == i or x == j else "white" for x in range(len(array))])
        time.sleep(0.01)
    array[i+1], array[high] = array[high], array[i+1]
    return i + 1

def quick_sort(canvas, array, low, high):
    if low < high:
        pi = partition(canvas, array, low, high)
        quick_sort(canvas, array, low, pi-1)
        quick_sort(canvas, array, pi+1, high)
        draw_bars(canvas, array, ["purple" if x == pi else "white" for x in range(len(array))])
        time.sleep(0.1)

def start_sorting():
    global array
    algo = algo_menu.get()
    if algo == "Bubble Sort":
        bubble_sort(canvas, array)
    elif algo == "Merge Sort":
        merge_sort(canvas, array, 0, len(array))
    elif algo == "Quick Sort":
        quick_sort(canvas, array, 0, len(array) - 1)
    draw_bars(canvas, array, ["white" for _ in range(len(array))])

def generate_array():
    global array
    array = [random.randint(10, canvas_height) for _ in range(50)]
    draw_bars(canvas, array, ["white" for _ in range(len(array))])

# GUI setup
root = Tk()

root.title("Sorting Visualizer")
root.geometry("800x700")
root.config(bg='#85929E')
root.resizable(False,False)
frame = Frame(root)
frame = Frame(root, width=400) 
frame.pack(side=TOP, pady=10)
img=PhotoImage(file="hotelnext.png")
Label(frame,image=img,bg='#85929E',).place(x=-900,y=0)
algo_menu = ttk.Combobox(frame, values=["Bubble Sort", "Merge Sort", "Quick Sort"])
algo_menu.grid(row=0, column=0, padx=10)
algo_menu.current(0)
sort_button = Button(frame,text="Start Sorting",bg='#CED7D7',fg='#17202A',font=('bold',30), command=start_sorting)
sort_button.grid(row=0, column=1, padx=10)
generate_button = Button(frame, text="Generate Array",bg='#CED7D7',fg='#17202A',font=('bold',30), command=generate_array)
generate_button.grid(row=0, column=2, padx=10)
canvas = Canvas(root, width=canvas_width, height=canvas_height,bg="black")
canvas.place(x=100,y=250)

root.mainloop()
