#from tkinter import *
import os
import serial
import sys
def right():
	#os.system("echo 'Forward!'")
	ser.write(b'1')
def left():
	#os.system("echo 'Backward!'")
	ser.write(b'0')
serialport = "/dev/ttyACM0"
ser = serial.Serial(serialport, 9600)
#b = Button(text="<", command=right)
#c = Button(text=">", command=left)
#b.pack()
#c.pack()
#mainloop()
