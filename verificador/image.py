from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.title("imagen")
ventana.geometry('500x500')
#Creamos Variable para la imagen
try:
    
    image = Image.open("./Img/carne.jpg")
    image = image.resize((300,300))
    test = ImageTk.PhotoImage(image)
    lbl_codigo = Label(ventana, image=test)
except:
    lbl_codigo = Label(ventana, text="imagen no disponible")

#labels
lbl_codigo.pack(pady=20)

ventana.mainloop()