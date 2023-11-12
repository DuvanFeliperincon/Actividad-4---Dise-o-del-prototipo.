import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random


# Funciones para los botones del menú lateral
def mostrar_vista_productos():
    label_central.config(text="Vista de Productos")
    # Agregar aquí la lógica para mostrar la vista de productos

def mostrar_vista_caducar():
    label_central.config(text="Productos Prontos A Caducar")
    # Agregar aquí la lógica para mostrar la vista de productos a caducar

def mostrar_vista_presupuesto():
    label_central.config(text="Presupuesto")
    # Agregar aquí la lógica para mostrar la vista de presupuesto

def mostrar_seguimiento():
    label_central.config(text="Seguimiento de Usuarios")
    # Agregar aquí la lógica para mostrar la vista de seguimiento de usuarios

def mostrar_importacion():
    label_central.config(text="Importación de Imágenes")
    # Agregar aquí la lógica para mostrar la vista de importación de imágenes

# Función para generar texto aleatorio
def texto_aleatorio():
    palabras = ["Nombre producto: uvas", "Precio: $5000", "Entrega: 1/01/2023", "Vencimiento: 20/06/2023"]
    return " ".join(random.choice(palabras) for _ in range(1))

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Mi Aplicación")
ventana.geometry("1000x600")  # Aumentamos el ancho de la ventana

# Header con un círculo para la imagen y fondo verde (RGB)
header = ttk.Frame(ventana, style="Header.TFrame")
header.pack(fill="x")

# Menú lateral con fondo azul (RGB)
menu_lateral = ttk.Frame(ventana, style="Menu.TFrame", width=150)  # Aumentamos el ancho del menú
menu_lateral.pack(side="left", fill="y")

# Crear un título para el menú
menu_title = ttk.Label(menu_lateral, text="Menu", style="MenuTitle.TLabel")
menu_title.pack()

# Crear un marco para los botones
button_frame = ttk.Frame(menu_lateral, style="MenuButtonFrame.TFrame")
button_frame.pack(fill="both", expand=True)

# Distribución uniforme de botones en el marco
button_productos = ttk.Button(button_frame, text="Home", command=mostrar_vista_productos)
button_productos.grid(row=0, column=0, sticky="ew", padx=10, pady=5)

button_caducar = ttk.Button(button_frame, text="Vista de Productos", command=mostrar_vista_caducar)
button_caducar.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

button_presupuesto = ttk.Button(button_frame, text="Vista de Productos a Caducar", command=mostrar_vista_presupuesto)
button_presupuesto.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

# Agregar más botones según tus necesidades
button_seguimiento = ttk.Button(button_frame, text="Seguimiento Usuarios", command=mostrar_seguimiento)
button_seguimiento.grid(row=3, column=0, sticky="ew", padx=10, pady=5)

button_importacion = ttk.Button(button_frame, text="Importación Imágenes", command=mostrar_importacion)
button_importacion.grid(row=4, column=0, sticky="ew", padx=10, pady=5)

# Crear un marco para la imagen a la derecha del header
image_frame = ttk.Frame(header, style="ImageFrame.TFrame")
image_frame.pack(side="right", padx=10)

# Cargar una imagen para el círculo (reemplaza "imagen.png" con tu imagen)
imagen = Image.open("assets/fondo.png")
imagen = imagen.resize((50, 50))  # Ajusta el tamaño
imagen = ImageTk.PhotoImage(imagen)

# Crear un label para la imagen dentro del marco
circle_label = ttk.Label(image_frame, image=imagen, style="Image.TLabel")
circle_label.grid()

# Sección central
seccion_central = ttk.Frame(ventana)
seccion_central.pack(fill="both", expand=True)

# Crear tres cuadros con texto aleatorio y fondo amarillo
for i in range(4):
    cuadro = tk.Frame(seccion_central, bg="yellow", height=100, width=100)
    cuadro.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")
    texto = texto_aleatorio()
    label_cuadro = tk.Label(cuadro, text=texto, font=("Arial", 12), bg="yellow")
    label_cuadro.pack(fill="both", expand=True)

# Configurar que los cuadros ocupen todo el ancho de la sección central
seccion_central.grid_columnconfigure(0, weight=1)
seccion_central.grid_columnconfigure(1, weight=1)
seccion_central.grid_columnconfigure(2, weight=1)

# Pie de página con fondo verde (RGB)
pie_pagina = ttk.Frame(ventana, style="Footer.TFrame")
pie_pagina.pack(fill="x")

# Etiqueta en el pie de página
label_pie = ttk.Label(pie_pagina, text="Copyright 2023")
label_pie.pack()

# Establecer estilos para los marcos y botones
style = ttk.Style()
style.configure("Header.TFrame", background="#90D05E")  # Fondo verde RGB
style.configure("Menu.TFrame", background="#8FC8C7")    # Fondo azul RGB
style.configure("Footer.TFrame", background="#90D05E")  # Fondo verde RGB
style.configure("TButton", width=20)  # Ajusta el ancho de los botones

# Estilo para el marco del círculo
style.configure("ImageFrame.TFrame", background="#90D05E")  # Fondo verde RGB
style.configure("Image.TLabel", anchor="center")

# Estilo para el título del menú
style.configure("MenuTitle.TLabel", background="#8FC8C7", font=("Arial", 12, "bold"))

# Estilo para el marco de los botones del menú
style.configure("MenuButtonFrame.TFrame", background="#8FC8C7")

# Iniciar el bucle principal de la ventana
ventana.mainloop()
