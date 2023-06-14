import pyautogui
import time
import random
import tkinter as tk
from tkinter import *
import threading
from tkinter import ttk
import tkinter.messagebox as messagebox
from pynput import keyboard


root = tk.Tk()

root.geometry('450x325')
root.title('Random Mouse Clicker')

# frames
frame = tk.Frame(root)
frame.pack()

stop_event = threading.Event()

# # # # # # # # # # # # # # # # # # # Click Intervals Label Frame # # # # # # # # # # # # # # # # # # # 

clickInterval =tk.LabelFrame(frame, text="Click Interval")
clickInterval.grid(row= 0, column=0, padx=10, pady=5)

hours = tk.Label(clickInterval, text="Hours")
hours.grid(row=1, column=0)
minutes = tk.Label(clickInterval, text="Minutes")
minutes.grid(row=1, column=1)
seconds = tk.Label(clickInterval, text="Seconds")
seconds.grid(row=1, column=2)
milliseconds = tk.Label(clickInterval, text="Milliseconds")
milliseconds.grid(row=1, column=3)


# # # # # # # # Click Intervals Entries # # # # # # # 

hours_entry = tk.Entry(clickInterval, width=10)
minutes_entry = tk.Entry(clickInterval, width=10)
seconds_entry = tk.Entry(clickInterval, width=10)
milliseconds_entry = tk.Entry(clickInterval, width=10)


hours_entry.grid(row=0, column=0)
minutes_entry.grid(row=0, column=1)
seconds_entry.grid(row=0, column=2)
milliseconds_entry.grid(row=0, column=3)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # Options Label Frame # # # # # # # # # # # # # # # # # # # # #

options = tk.LabelFrame(frame, text="Options")
options.grid(row=1, column=0, sticky="news", padx=10, pady=10)

var1 = tk.IntVar()
chk = tk.Checkbutton(options, text="Location", variable=var1)
chk.grid(row=0, column=0, sticky='w', pady=3, columnspan=2)  # Use columnspan to span over two columns

var3 = tk.IntVar()
chk3 = tk.Checkbutton(options, text="Location +/-", variable=var3)
chk3.grid(row=0, column=1, sticky='w', pady=3, columnspan=2)

locationX = tk.Label(options, text="X")
locationY = tk.Label(options, text="Y")
locationX.grid(row=2, column=0)
locationY.grid(row=2, column=1)


# # # # # # # # # # # Location Entries # # # # # # # # # # 

locationXentry = tk.Entry(options, width=10)
locationYentry = tk.Entry(options, width=10)
locationXentry.grid(row=1, column=0)  # Adjust these to row=2
locationYentry.grid(row=1, column=1)  # Adjust these to row=2

var2 = tk.IntVar()
chk2 = tk.Checkbutton(options, text="Random Interval +/-", variable=var2)
chk2.grid(row=0, column=3, sticky='w', pady=3, columnspan=2)  # Use columnspan to span over two columns

random_interval = tk.Entry(options, width=4)
random_interval.grid(row=0, column=5)

locationX1 = tk.Label(options, text="X")
locationY1 = tk.Label(options, text="Y")
locationX1.grid(row=2, column=4)  # Adjust these to row=1
locationY1.grid(row=2, column=5)  # Adjust these to row=1

locationXentry1 = tk.Label(options, bd=0, width=5, height=1)
locationYentry1 = tk.Label(options, bd=0, width=5, height=1)
locationXentry1.grid(row=1, column=4)  # Adjust these to row=2
locationYentry1.grid(row=1, column=5)  # Adjust these to row=2

# number entry

clickNumberEntry = tk.Entry(options, width=11)
clickNumberEntry.grid(row=1, column=3, sticky='w') 
clickNumberLabel = tk.Label(options, width=4, text='Clicks')
clickNumberLabel.grid(row=2, column=3) 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # Info Label Frame # # # # # # # # # # # # # # # # # # # 

info = tk.LabelFrame(frame, text="Info")
info.grid(row=2, column=0, sticky="news", padx=10, pady=10)

clicksCompletedLabel = tk.Label(info, text="Clicks Completed")
clicksCompletedLabel.grid(row=1, column=0)

clicksCompletedLabel2 = tk.Label(info, bd=0, width=7, height=1, anchor=W)
clicksCompletedLabel2.grid(row=1, column=1)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Live update clicks completed
clicks_completed_count = 0

def clicks_completed():
        global clicks_completed_count     
        clicks_completed_count += 1
        clicksCompletedLabel2.config(text=str(clicks_completed_count - 1))

threading.Thread(target=clicks_completed, daemon=True).start()

# Live updating coordinates

def update_labels():
    while True:
        currentMouseX, currentMouseY = pyautogui.position()  # Get the XY position of the mouse.
        locationXentry1.config(text=str(currentMouseX))  # use the config() method to update the label's text
        locationYentry1.config(text=str(currentMouseY))  # similar for Y
        time.sleep(0.1)  # Add a slight delay to decrease console output frequency

# create a separate thread to run the update_labels function as soon as the program starts
threading.Thread(target=update_labels, daemon=True).start()


def start():

    # global clicks_completed_count
    # clicks_completed_count = 1
    
    
    l = locationXentry.get()
    l2 = locationYentry.get()
    r1 = random_interval.get()
    click_number = clickNumberEntry.get()


    # If fields are not blank, convert to integer
    l = int(l) if l else None
    l2 = int(l2) if l2 else None
    l3 = l4 = 0
    if r1 is None or r1 == '':
        r1 = 0
    else:
        r1 = int(r1)    

    if click_number is None or click_number == '':
        click_number = 0
    else:
        click_number = int(click_number)    


    print(click_number)
    if click_number != 0: 
        while click_number > 0 and not stop_event.is_set():
            click_number -= 1
            # execute clicks specified   
            if l is not None or 0 and l2 is not None or 0:
                l3 = l + random.uniform(0, 10)
                l4 = l2 + random.uniform(0, 10)

            # Location only checked
            if var1.get() == 1 and var2.get() == 0 and var3.get() == 0:
                if hours_entry.get() != '':
                    x = float(hours_entry.get()) * 3600
                    time.sleep(x)
                    pyautogui.click(l, l2)
                elif minutes_entry.get() != '':
                    x = float(minutes_entry.get()) * 60
                    time.sleep(x)
                    pyautogui.click(l, l2)
                elif seconds_entry.get() != '':
                    x = float(seconds_entry.get())
                    time.sleep(x)
                    pyautogui.click(l, l2)
                elif milliseconds_entry.get() != '':
                    x = float(milliseconds_entry.get()) * .001
                    time.sleep(x)
                    pyautogui.click(l, l2)

            # Location & Location +/- checked
            elif var1.get() == 1 and var3.get() == 1 and var2.get() == 0:
                if hours_entry.get() != '':
                    x = float(hours_entry.get()) * 3600
                    time.sleep(x)
                    pyautogui.click(l3, l4)
                elif minutes_entry.get() != '':
                    x = float(minutes_entry.get()) * 60
                    time.sleep(x)
                    pyautogui.click(l3, l4)
                elif seconds_entry.get() != '':
                    x = float(seconds_entry.get())
                    time.sleep(x)
                    pyautogui.click(l3, l4)
                elif milliseconds_entry.get() != '':
                    x = float(milliseconds_entry.get()) * .001
                    time.sleep(x)
                    pyautogui.click(l3, l4)

            # Location & Location +/- & Random Interval Checked
            elif var1.get() == 1 and var3.get() == 1 and var2.get() == 1:
                if hours_entry.get() != '':
                    x = float(hours_entry.get()) * 3600
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click(l3, l4)
                elif minutes_entry.get() != '':
                    x = float(minutes_entry.get()) * 60
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click(l3, l4)
                elif seconds_entry.get() != '':
                    x = float(seconds_entry.get())
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click(l3, l4)
                elif milliseconds_entry.get() != '':
                    x = float(milliseconds_entry.get()) * .001
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click(l3, l4)
                
            # Location checked and Random Interval
            elif var1.get() == 1 and var2.get() == 1 and var3.get() == 0:
                if hours_entry.get() != '':
                    x = float(hours_entry.get()) * 3600
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click(l, l2)
                elif minutes_entry.get() != '':
                    x = float(minutes_entry.get()) * 60
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click(l, l2)
                elif seconds_entry.get() != '':
                    x = float(seconds_entry.get())
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click(l, l2)
                elif milliseconds_entry.get() != '':
                    x = float(milliseconds_entry.get()) * .001
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click(l, l2)

            elif var2.get() == 1 and var1.get() == 0 and var3.get() == 0:
                if hours_entry.get() != '':
                    x = float(hours_entry.get()) * 3600
                    y = random.uniform(0,r1 * .3600) * 3600
                    time.sleep(x + y)
                    pyautogui.click()
                elif minutes_entry.get() != '':
                    x = float(minutes_entry.get()) * 60
                    y = random.uniform(0,r1 * 60) * 60
                    time.sleep(x + y)
                    pyautogui.click()
                elif seconds_entry.get() != '':
                    x = float(seconds_entry.get())
                    y = random.uniform(0,r1)
                    time.sleep(x + y)
                    pyautogui.click()
                elif milliseconds_entry.get() != '':
                    x = float(milliseconds_entry.get()) * .001
                    y = random.uniform(0,r1 * .001)
                    time.sleep(x + y)
                    pyautogui.click()
            
            elif var1.get() == 0 and var2.get() == 0 and var3.get() == 0:
                if hours_entry.get() != '':
                    x = float(hours_entry.get()) * 3600
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click()
                elif minutes_entry.get() != '':
                    x = float(minutes_entry.get()) * 60
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click()
                elif seconds_entry.get() != '':
                    x = float(seconds_entry.get())
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click()
                elif milliseconds_entry.get() != '':
                    x = float(milliseconds_entry.get()) * .001
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click()

            clicks_completed()

    else:

        while not stop_event.is_set():
            
            # If l and l2 are not None, compute l3 and l4
            if l is not None or 0 and l2 is not None or 0:
                l3 = l + random.uniform(0, 10)
                l4 = l2 + random.uniform(0, 10)

            # Location only checked
            if var1.get() == 1 and var2.get() == 0 and var3.get() == 0:
                if hours_entry.get() != '':
                    x = float(hours_entry.get()) * 3600
                    time.sleep(x)
                    pyautogui.click(l, l2)
                elif minutes_entry.get() != '':
                    x = float(minutes_entry.get()) * 60
                    time.sleep(x)
                    pyautogui.click(l, l2)
                elif seconds_entry.get() != '':
                    x = float(seconds_entry.get())
                    time.sleep(x)
                    pyautogui.click(l, l2)
                elif milliseconds_entry.get() != '':
                    x = float(milliseconds_entry.get()) * .001
                    time.sleep(x)
                    pyautogui.click(l, l2)

            # Location & Location +/- checked
            elif var1.get() == 1 and var3.get() == 1 and var2.get() == 0:
                if hours_entry.get() != '':
                    x = float(hours_entry.get()) * 3600
                    time.sleep(x)
                    pyautogui.click(l3, l4)
                elif minutes_entry.get() != '':
                    x = float(minutes_entry.get()) * 60
                    time.sleep(x)
                    pyautogui.click(l3, l4)
                elif seconds_entry.get() != '':
                    x = float(seconds_entry.get())
                    time.sleep(x)
                    pyautogui.click(l3, l4)
                elif milliseconds_entry.get() != '':
                    x = float(milliseconds_entry.get()) * .001
                    time.sleep(x)
                    pyautogui.click(l3, l4)

            # Location & Location +/- & Random Interval Checked
            elif var1.get() == 1 and var3.get() == 1 and var2.get() == 1:
                if hours_entry.get() != '':
                    x = float(hours_entry.get()) * 3600
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click(l3, l4)
                elif minutes_entry.get() != '':
                    x = float(minutes_entry.get()) * 60
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click(l3, l4)
                elif seconds_entry.get() != '':
                    x = float(seconds_entry.get())
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click(l3, l4)
                elif milliseconds_entry.get() != '':
                    x = float(milliseconds_entry.get()) * .001
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click(l3, l4)
                
            # Location checked and Random Interval
            elif var1.get() == 1 and var2.get() == 1 and var3.get() == 0:
                if hours_entry.get() != '':
                    x = float(hours_entry.get()) * 3600
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click(l, l2)
                elif minutes_entry.get() != '':
                    x = float(minutes_entry.get()) * 60
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click(l, l2)
                elif seconds_entry.get() != '':
                    x = float(seconds_entry.get())
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click(l, l2)
                elif milliseconds_entry.get() != '':
                    x = float(milliseconds_entry.get()) * .001
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click(l, l2)

            elif var2.get() == 1 and var1.get() == 0 and var3.get() == 0:
                if hours_entry.get() != '':
                    x = float(hours_entry.get()) * 3600
                    y = random.uniform(0,r1 * .3600) * 3600
                    time.sleep(x + y)
                    pyautogui.click()
                elif minutes_entry.get() != '':
                    x = float(minutes_entry.get()) * 60
                    y = random.uniform(0,r1 * 60) * 60
                    time.sleep(x + y)
                    pyautogui.click()
                elif seconds_entry.get() != '':
                    x = float(seconds_entry.get())
                    y = random.uniform(0,r1)
                    time.sleep(x + y)
                    pyautogui.click()
                elif milliseconds_entry.get() != '':
                    x = float(milliseconds_entry.get()) * .001
                    y = random.uniform(0,r1 * .001)
                    time.sleep(x + y)
                    pyautogui.click()
            
            elif var1.get() == 0 and var2.get() == 0 and var3.get() == 0:
                if hours_entry.get() != '':
                    x = float(hours_entry.get()) * 3600
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click()
                elif minutes_entry.get() != '':
                    x = float(minutes_entry.get()) * 60
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click()
                elif seconds_entry.get() != '':
                    x = float(seconds_entry.get())
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click()
                elif milliseconds_entry.get() != '':
                    x = float(milliseconds_entry.get()) * .001
                    time.sleep(x + random.uniform(0,r1))
                    pyautogui.click()

            clicks_completed()


def reset_clicks_completed():
    global clicks_completed_count
    clicks_completed_count = 0


def stop():
    reset_clicks_completed()
    stop_event.set()

def start_thread():
    stop_event.clear()  # Reset the stop_event
    threading.Thread(target=start).start()

def stop_thread():
    threading.Thread(target=stop).start()

def on_key_press(key):
    if key == keyboard.Key.f8:
        start_thread()

def on_key_release(key):
    if key == keyboard.Key.f9:
        stop_thread()

listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
listener.start()

start_button = ttk.Button(root, text="Start (F8)", command=start_thread, style="BW.TButton")
start_button.pack(fill=tk.X, padx=30)

stop_button = ttk.Button(root, text="Stop (F9)", command=stop_thread, style="BW.TButton")
stop_button.pack(fill=tk.X, padx=30)

root.mainloop()
