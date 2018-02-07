import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(27, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    
def forward(tframe):
    #init()
    gpio.output(27, True)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(tframe)
    gpio.cleanup()

def backward(tframe):
    #init()
    gpio.output(27, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(tframe)
    gpio.cleanup()
    
def left(tframe):
    #init()
    gpio.output(27, False)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(tframe)
    gpio.cleanup()
    
def right(tframe):
    #init()
    gpio.output(27, True)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, False)
    time.sleep(tframe)
    gpio.cleanup()
    
def pivot_left(tframe):
    #init()
    gpio.output(27, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(tframe)
    gpio.cleanup()
    
def pivot_right(tframe):
    #init()
    gpio.output(27, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(tframe)
    gpio.cleanup()

def key_input(event):
    init()
    print 'Key', event.char
    key_press = event.char
    sleep_time = 0.030
    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        backward(sleep_time)
    elif key_press.lower() == 'a':
        left(sleep_time)
    elif key_press.lower() == 'd':
        right(sleep_time)
    elif key_press.lower() == 'q':
        pivot_left(sleep_time)
    elif key_press.lower() == 'e':
        pivot_right(sleep_time)
    else:
        gpio.cleanup()
        
command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
    
