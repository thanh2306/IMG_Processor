
from Morphological import *
from rgb_to_bianry import convert_to_binary
from edge_detetion import edge_detection
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
import threading 


N = 0
M = 0

root = Tk()
root.title("Xử lí ảnh")
root.geometry("500x500")



#menu

# my_menu = Menu(root)
# root.config(menu=my_menu)



# # def our_command():

# #     window = Tk()
# #     window.title("ma trận")
# #     window.geometry("200x80")
    
# #     #funtion
# #     def get_data():
# #         global M
# #         global N
# #         M = int(entry_M.get())
# #         N = int(entry_N.get())
# #     #display
# #     labe1 = Label(window,text='Kích thước M')
# #     labe2 = Label(window,text='Kích thước N')
# #     entry_M = Entry(window,width=10,font=('Times_New_Roman', 10))
# #     entry_N = Entry(window,width=10,font=('Times_New_Roman', 10))

# #     btnEnter = Button(window,text="Enter",command=get_data)

# #     entry_M.grid(row=0,column=1)
# #     entry_N.grid(row=1,column=1)
# #     labe1.grid(row=0,column=0)
# #     labe2.grid(row=1,column=0)
# #     btnEnter.grid(row=3,column=1)
# #     window.mainloop


# # #create a menu iteam
# # file_menu = Menu(my_menu)
# # my_menu.add_cascade(label='Mask',menu=file_menu)
# # file_menu.add_command(label="Mask 3x3",command=our_command)

# hàm xử lí





def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        return file_path



def binary_image():
    path = open_file()
    img_binary = convert_to_binary(path)
    def save():
        file = filedialog.asksaveasfilename(filetypes=(('image', '*.jpg'), ('All', '*.*')),defaultextension='*.jpg')
        cv2.imwrite(file,img_binary)
    button = Button(main_frame, text='Save binary image', font=('Times_New_Roman', 10),bg='blue',foreground='white',command=save)
    button.place(x=0, y=0)


def Erosion():
#  lọc co
    path = open_file()
    img= erosion(path)
    def save1():
        file = filedialog.asksaveasfilename(filetypes=(('image', '*.jpg'), ('All', '*.*')),defaultextension='*.jpg')
        cv2.imwrite(file,img)
    button1 = Button(main_frame, text='Save erosion image', font=('Times_New_Roman', 10),bg='blue',foreground='white',command=save1)
    button1.place(x=0, y=30)


# Dilation
def Dilation():
    path = open_file()
    img = dilation(path)
    def save2():
        file = filedialog.asksaveasfilename(filetypes=(('image', '*.jpg'), ('All', '*.*')),defaultextension='*.jpg')
        cv2.imwrite(file,img)
    button2 = Button(main_frame, text='Save dilation image', font=('Times_New_Roman', 10),bg='blue',foreground='white',command=save2)
    button2.place(x=0, y=60)



# Opening
def Opening():
    path = open_file()
    img = opening(path)
    def save3():
        file = filedialog.asksaveasfilename(filetypes=(('image', '*.jpg'), ('All', '*.*')),defaultextension='*.jpg')
        cv2.imwrite(file,img)
    button3 = Button(main_frame, text='Save opening image', font=('Times_New_Roman', 10),bg='blue',foreground='white',command=save3)
    button3.place(x=0, y=60)


# Closing
def Closing():
    path = open_file()
    img = closing(path)
    def save4():
        file = filedialog.asksaveasfilename(filetypes=(('image', '*.jpg'), ('All', '*.*')),defaultextension='*.jpg')
        cv2.imwrite(file,img)
    button4 = Button(main_frame, text='Save closing image', font=('Times_New_Roman', 10),bg='blue',foreground='white',command=save4)
    button4.place(x=0, y=90)



# Hit-Miss
def Hitmiss():
    path = open_file()
    img = hitmiss(pathname=path)
    def save5():
        file = filedialog.asksaveasfilename(filetypes=(('image', '*.jpg'), ('All', '*.*')),defaultextension='*.jpg')
        cv2.imwrite(file,img)
    button5 = Button(main_frame, text='Save hitmiss image', font=('Times_New_Roman', 10),bg='blue',foreground='white',command=save5)
    button5.place(x=0, y=120)


#edge_detection

def Edge_detection():
    path = open_file()
    edge_detection(path)


def Sobel():
    path = open_file()
    sobel(path)



# label



#frame

options_frame = Frame(root,bg='#c3c3c3')
options_frame.pack(side=tk.LEFT)
options_frame.configure(width=140,height=500)
options_frame.pack_propagate(False)



main_frame = tk.Frame(root,highlightbackground='black',highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.configure(width=355,height=500)
main_frame.pack_propagate(False)



# button 
erosion1 = Button(options_frame, width=19,text="Erosion",command=Erosion)
dilation1= Button(options_frame, width=19,text="Dilation",command=Dilation)
opening1= Button(options_frame, width=19,text="Opening",command=Opening)
closing1= Button(options_frame, width=19,text="Closing",command=Closing)
hitmiss1= Button(options_frame, width=19,text="Hitmiss",command=Hitmiss)
binary_image1= Button(options_frame, width=19,text="Convert to binary image",command=binary_image)
edge_detection1= Button(options_frame, width=19,text="Ede Detection",command=Edge_detection)
sobel1 = Button(options_frame, width=19,text="sobel",command=Sobel)


binary_image1.place(x=0,y=0)
erosion1.place(x=0,y=25)
dilation1.place(x=0,y=50)
opening1.place(x=0,y=75)
closing1.place(x=0,y=100)
hitmiss1.place(x=0,y=125)
edge_detection1.place(x=0,y=150)
sobel1.place(x=0,y=175)

 

root.mainloop()



 



