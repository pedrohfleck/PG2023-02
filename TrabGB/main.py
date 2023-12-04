from tkinter import *
from PIL import ImageTk, Image 
from tkinter import filedialog
from Overlay import overlay
from Filters import apply_all
import cv2

def select_image():
    global panel, path, img_array, filters_dict
    path = filedialog.askopenfilename()
    
    if len(path) > 0:
        image = cv2.imread(path)
        img_array = image
        filters_dict = apply_all(image)	
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        
        if panel is None:
            panel = Label(image=image)
            panel.image = image
            panel.pack(side="left", expand="yes", padx=10, pady=10)
        else:
            panel.configure(image=image)
            panel.image = image

def use_camera():
    global panel, img_array, filtr, filters_dict

    ret, cam = cap.read()
    img_array = cam
    filters_dict = apply_all(img_array)
    cam = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)
    cam = Image.fromarray(cam)
    cam = ImageTk.PhotoImage(cam)
    if panel is None:
        panel = Label(image=cam)
        panel.image = cam
        panel.pack(side="left", fill='both', expand="yes", padx=10, pady=10)
    else:
        panel.configure(image=cam)
        panel.image = cam

def check_filter():
    if filtr != None:
        image = apply_filter()
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        panel.configure(image=image)
        panel.image = image

def apply_filter():
    global filters_dict, filtr
    
    return cv2.cvtColor(filters_dict[filtr], cv2.COLOR_BGR2RGB)

def set_filter(filter_name):
    global filtr
    filtr = filter_name
    
    check_filter()

def apply_sticker():
    global sticker, sticker_x, sticker_y

    if sticker != None and sticker_x != None and sticker_y != None:
        sticker_img = cv2.imread("stickers/" + sticker + ".png", cv2.IMREAD_UNCHANGED)
        dim = (int(sticker_img.shape[1] * 10 / 100), int(sticker_img.shape[0] * 10 / 100))
        sticker_img = cv2.resize(sticker_img, dim, cv2.INTER_AREA)
        image = overlay(img_array, sticker_img, sticker_x, sticker_y)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        panel.configure(image=image)
        panel.image = image
        sticker = None

def set_sticker(sticker_name):
    global sticker
    sticker = sticker_name

def get_origin(eventorigin):
    global sticker_x,sticker_y,sticker

    if sticker != None:
        sticker_x = eventorigin.x
        sticker_y = eventorigin.y

        apply_sticker()

root = Tk()
root.bind("<Button 1>",get_origin)

cap = cv2.VideoCapture(0)
    
panel = None
path = None
img_array = None
filtr = None
sticker = None
sticker_x = None
sticker_y = None
filters_dict = None

btn = Button(root, text="Selecione uma imagem", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

btn = Button(root, text="Preto e Branco", command= lambda: set_filter("BlackAndWhite"))
btn.pack(side="right", fill="both", padx="10", pady="10")
btn = Button(root, text="Colorida", command= lambda: set_filter("Colored"))
btn.pack(side="right", fill="both", padx="10", pady="10")
btn = Button(root, text="Negativo", command= lambda: set_filter("Negative"))
btn.pack(side="right", fill="both", padx="10", pady="10")
btn = Button(root, text="Binary", command= lambda: set_filter("Binary"))
btn.pack(side="right", fill="both", padx="10", pady="10")
btn = Button(root, text="Canny", command= lambda: set_filter("Canny"))
btn.pack(side="right", fill="both", padx="10", pady="10")
btn = Button(root, text="Vignette", command= lambda: set_filter("Vignette"))
btn.pack(side="right", fill="both", padx="10", pady="10")
btn = Button(root, text="ColorRamp", command= lambda: set_filter("ColorRamp"))
btn.pack(side="right", fill="both", padx="10", pady="10")
btn = Button(root, text="MotionBlur", command= lambda: set_filter("MotionBlur"))
btn.pack(side="right", fill="both", padx="10", pady="10")

btn = Button(root, text="Oculos", command= lambda: set_sticker("oculos"))
btn.pack(side="left", fill="both", padx="10", pady="10")
btn = Button(root, text="Chapeu", command= lambda: set_sticker("beachhat"))
btn.pack(side="left", fill="both", padx="10", pady="10")
btn = Button(root, text="Laço", command= lambda: set_sticker("laco"))
btn.pack(side="left", fill="both", padx="10", pady="10")
btn = Button(root, text="Gravata", command= lambda: set_sticker("bowtie"))
btn.pack(side="left", fill="both", padx="10", pady="10")
btn = Button(root, text="Orelhas", command= lambda: set_sticker("bunnyears"))
btn.pack(side="left", fill="both", padx="10", pady="10")
btn = Button(root, text="Cartola", command= lambda: set_sticker("hat"))
btn.pack(side="left", fill="both", padx="10", pady="10")
btn = Button(root, text="Criança", command= lambda: set_sticker("kid"))
btn.pack(side="left", fill="both", padx="10", pady="10")
btn = Button(root, text="Curtida", command= lambda: set_sticker("like"))
btn.pack(side="left", fill="both", padx="10", pady="10")

btn = Button(root, text="Camera", command=use_camera)
btn.pack(side="top", fill="both", expand="yes", padx="10", pady="10")

root.mainloop()