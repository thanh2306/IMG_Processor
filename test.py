from Morphological import *
from rgb_to_bianry import convert_to_binary
from edge_detetion import edge_detection
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import cv2
import numpy as np
import threading 
from PIL import ImageTk,Image

root = tk.Tk() 
root.geometry("600x600")
root.title("Xử lí ảnh")
image_label = Label(root)


CURRENT_IMAGE = None
CURRENT_KERNEL = None

# kernel_1 = None
# kernel_2 = None

#Funtion


def open_file():
    global file_path
    file_path = filedialog.askopenfilename()
    global image
    if file_path:
        image = cv2.imread(file_path)
        image1 = Image.open(file_path)
        image1.thumbnail(((root.winfo_width()/1.5),
        (root.winfo_height()/1.5)))
        my_image = ImageTk.PhotoImage(image1)

        image_label.configure(image=my_image)
        image_label.image = my_image

def select():

    global CURRENT_KERNEL
    input_m = int(m.get())
    input_n = int(n.get())

    shape = (input_m,input_n)

    if my_combo.get() == "MORPH_RECT":
        CURRENT_KERNEL = cv2.getStructuringElement(cv2.MORPH_RECT,ksize=shape)
    if my_combo.get() == "MORPH_ELIPSE":
        CURRENT_KERNEL = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,ksize=shape)
    if my_combo.get() == "MORPH_CROSS":
       CURRENT_KERNEL = cv2.getStructuringElement(cv2.MORPH_CROSS,ksize=shape)



def binary_image():
    global CURRENT_IMAGE
    CURRENT_IMAGE =  convert_to_binary(pathname=file_path)

def Erosion():
    global CURRENT_IMAGE
    CURRENT_IMAGE = erosion(img=image,kernel=CURRENT_KERNEL)

def Dilation():
    global CURRENT_IMAGE
    CURRENT_IMAGE = dilation(img=image,kernel=CURRENT_KERNEL)

def Opening():
    global CURRENT_IMAGE
    CURRENT_IMAGE = opening(img=image,kernel=CURRENT_KERNEL)



# Closing
def Closing():
    global CURRENT_IMAGE
    CURRENT_IMAGE = closing(img=image,kernel=CURRENT_KERNEL)


# def Hitmis():
#     global CURRENT_IMAGE
#     kernel_1 = cv2.getStructuringElement(cv2.MORPH_RECT,ksize=(3,3))
#     kernel_2 = cv2.getStructuringElement(cv2.MORPH_CROSS,ksize=(3,3))
#     CURRENT_IMAGE = hitmiss(pathname=file_path,kernel_hit=kernel_1,kernel_miss=kernel_2)




def open_hit_miss():

    def select_options1():
        global kernel_1
        input_m = int(m_option1.get())
        input_n = int(n_option1.get())

        shape = (input_m,input_n)

        if combobox1.get() == "MORPH_RECT":
            kernel_1= cv2.getStructuringElement(cv2.MORPH_RECT,ksize=shape)
            print('chọn thành công')
        if combobox1.get() == "MORPH_ELIPSE":
            kernel_1= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,ksize=shape)
            print('chọn thành công')
        if combobox1.get() == "MORPH_CROSS":
            kernel_1 = cv2.getStructuringElement(cv2.MORPH_CROSS,ksize=shape)
            print('chọn thành công')

    def select_options2():
        global kernel_2
        input_m = int(m_option2.get())
        input_n = int(m_option2.get())

        shape = (input_m,input_n)

        if combobox2.get() == "MORPH_RECT":
            kernel_2 = cv2.getStructuringElement(cv2.MORPH_RECT,ksize=shape)
            print('chọn thành công')
        if combobox2.get() == "MORPH_ELIPSE":
            kernel_2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,ksize=shape)
            print('chọn thành công')
        if combobox2.get() == "MORPH_CROSS":
            kernel_2= cv2.getStructuringElement(cv2.MORPH_CROSS,ksize=shape)
            print('chọn thành công')


    def Hitmis():
        global CURRENT_IMAGE
        CURRENT_IMAGE = hitmiss(pathname=file_path,kernel_hit=kernel_1,kernel_miss=kernel_2)


    m_option2 = Entry(root,font=("Helvetica", 10))
    m_option2.place(x=350,y=450)
    n_option1 = Entry(root,font=("Helvetica", 10))
    n_option1.place(x=350,y=480)




    m_option1 = Entry(root,font=("Helvetica", 10))
    m_option1.place(x=100,y=450)
    n_option1 = Entry(root,font=("Helvetica", 10))
    n_option1.place(x=100,y=480)
    e = Entry(root, font=("Helvetica", 18))


    btn1=Button(root,text='Select',border=0,fg='white',bg='black',command=select_options2)
    btn1.place(x=500,y=420)
    Label(root,text='Kernel 2',font=('Arial',12,'bold')).place(x=350,y=400)
    options2 = ["MORPH_RECT","MORPH_ELIPSE","MORPH_CROSS"]
    combobox2 = ttk.Combobox(root,values=options2)
    combobox2.place(x=350,y=420)


    btn2= Button(root,text='Select',border=0,fg='white',bg='black',command=select_options1)
    btn2.place(x=250,y=420)
    Label(root,text='Kernel 1',font=('Arial',12,'bold')).place(x=100,y=400)
    options1 = ["MORPH_RECT","MORPH_ELIPSE","MORPH_CROSS"]
    combobox1 = ttk.Combobox(root,values=options1)
    combobox1.place(x=100,y=420)

    btn3= Button(root,text='Hit or Miss run',font=('Arial',12,'bold'),border=0,foreground='white',background='blue',command=Hitmis)
    btn3.place(x=260,y=500)




def save():
    file = filedialog.asksaveasfilename(filetypes=(('image', '*.jpg'), ('All', '*.*')),defaultextension='*.jpg')
    cv2.imwrite(file,CURRENT_IMAGE)


#Entry
m = Entry(root,font=("Helvetica", 10))
m.place(x=250,y=25)
n = Entry(root,font=("Helvetica", 10))
n.place(x=380,y=25)
e = Entry(root, font=("Helvetica", 18))

#label
name_combobox = Label(root,text='Shape',font=('Arial',12,'bold')).place(x=100,y=0)
name_M = Label(root,text='Iput M',font=('Arial',12,'bold')).place(x=250,y=0)
name_N = Label(root,text='Iput N',font=('Arial',12,'bold')).place(x=380,y=0)

#combo box :
options = ["MORPH_RECT","MORPH_ELIPSE","MORPH_CROSS"]
my_combo = ttk.Combobox(root,values=options)
my_combo.current(0)
my_combo.place(x=100,y=25)


my_button = Button(root, text="Select", command=select,border=0,background='black',foreground='white').place(x=530,y=25)

#Menu
menubar = Menu(root)

file = Menu(menubar)
menubar.add_cascade(label='File',menu=file)
file.add_command(label='Open',command=open_file)
file.add_command(label='Save',command=save)
file.add_command(label='Exit',command=root.destroy)


morphological = Menu(menubar)
menubar.add_cascade(label='Morphological',menu=morphological)
morphological.add_command(label='Convert to Binary Image',command=binary_image)
morphological.add_command(label='Erosion',command=Erosion)
morphological.add_command(label='Dilation',command=Dilation)
morphological.add_command(label='Opening',command=Opening)
morphological.add_command(label='Closing',command=Closing)
morphological.add_command(label='Hit or Miss',command=open_hit_miss)







image_label.place(x=100,y=50)
root.config(menu=menubar)
root.mainloop()










