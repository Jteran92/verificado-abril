from tkinter import *
import apiBuscar
from PIL import Image, ImageTk

codigo=''

def key_pressed(event):
    global codigo
    if event.keysym=='Return':

         #print(event.keys.ym)
         print('Buscando producto'+codigo)
         llamadaDatos(codigo)
         codigo = ''    
    else:
     codigo += event.keysym

def llamadaDatos(codigo):
    try:
        Kodigo = introduce_codigo.get()
        respuesta = apiBuscar.buscarProducto(codigo)
        #llamadaDatos= codigo
        if respuesta == 0:
            resultado_label.config(text="No se localizó el código del producto " + codigo)
        elif respuesta == -1:
            resultado_label.config(text='Error en la conexión')
        else:
            resultado_label.config(text='Nombre del Producto: ' + str(respuesta[0]) + "\n" + 'Precio del Producto: ' + str(respuesta[2]))
            if hasattr(llamadaDatos, 'imagen_label'):#La función hasattr(objeto, atributo) es una función incorporada de Python que se utiliza para verificar si un objeto tiene un atributo específico. Toma dos argumentos:
                llamadaDatos.imagen_label.destroy()  # Elimina el widget Label si existe
            
            img = Image.open("."+str(respuesta[3])) #llamamos la imagen. 
            img = img.resize((150, 150))  # Ajusta el tamaño de la imagen si es necesario
            img_tk = ImageTk.PhotoImage(img) #usamos la propiedad para poder cargar el pad de la imagen. 
            imagen_label = Label(ventana, image=img_tk) #colocamos un lable que nos de la imagen. 
            imagen_label.image = img_tk #mostramos la imagen en la ventana con tkner 
            imagen_label.pack()
            #Colocar la imagen
            ventana.update_idletasks()  # Actualizar la ventana antes de colocar la imagen
            y = (resultado_label.winfo_reqheight() + bottonBuscar.winfo_reqheight() + imagen_label.winfo_reqheight()) +60
            imagen_label.place(x=50,y=y)
            llamadaDatos.imagen_label = imagen_label#guardamos los datos de la imagen. 
           
    except Exception as e:
        resultado_label.config(text='Error: ' + str(e))

ventana = Tk()
ventana.title('Verificador')
ventana['bg'] = '#5d0551'
ventana.geometry('500x500')
kodigo = Label(ventana, text="Introduzca el código", font="BOLD")
kodigo.place(x=15, y=5)
introduce_codigo = Entry(ventana, font="BOLD")
introduce_codigo.place(x=-250, y=5)
bottonBuscar = Button(ventana, text="Buscar Código", font="BOLD", command=llamadaDatos)  # Asociar la función llamadaDatos al botón
bottonBuscar.place(x=-500, y=150)

resultado_label = Label(ventana, text="", font="BOLD")
resultado_label.place(x=10, y=200)

ventana.bind('<Key>', key_pressed)
ventana.mainloop()