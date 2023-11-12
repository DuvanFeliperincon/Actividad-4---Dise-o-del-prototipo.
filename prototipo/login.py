import os
import customtkinter as ctk
from PIL import Image, ImageTk

# Asignar la ruta del directorio que contiene el archivo de script actual en Python
script_dir = os.path.dirname(os.path.abspath(__file__))

# Definir el modo claro y el color para la interfas
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# Definir la nueva instancia y sus propiedades
class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("emergente")
        self.center_window(600, 600)

        # Construir la ruta a la imagen en la carpeta 'imagenes'
        imagen = os.path.join(script_dir, "imagenes", "logo1.png")

        # Cargar la imagen
        imagen_original = Image.open(imagen)

        # Escalar la imagen
        self.escalar_imagen = imagen_original.resize((600, 600))

        # Convertir a tkinter
        self.imagen_tk = ImageTk.PhotoImage(self.escalar_imagen)

        # Mostrar la imagen
        imagen_label = ctk.CTkLabel(self, image=self.imagen_tk, text="")
        imagen_label.pack(padx=10, pady=10)

        # Definir anchura, altura y posición de la interface 
    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.geometry(f"{width}x{height}+{x}+{y}")

# Crear la ventana principal
mainwindow = ctk.CTk()
mainwindow.geometry("400x500")
mainwindow.title("login")
mainwindow.config(bg='#90d05e')

# Declarar variables de color y fuentes
C_verde = '#90d05e'
C_azul = '#8fc8c7'
C_azul2 = '#1B52FF'
fuente1 = "Roboto", 12
fuente2 = "Roboto", 18, "bold"
fuente3 = "Roboto", 11

# Titulo login
text = ctk.CTkLabel(mainwindow, text=("Login"), font=(fuente2, 23), fg_color = C_verde)
text.pack(padx=10, pady=10)

# Cargar la imagen desde un archivo
imagen = "imagenes/Capa1.png"  # Reemplaza con la ruta a tu imagen
imagen_original = Image.open(imagen)

# Convertir la imagen a un objeto PhotoImage de Tkinter
imagen_tk = ImageTk.PhotoImage(imagen_original)

# Crear un widget de CTkLabel para mostrar la imagen
imagen_label = ctk.CTkLabel(mainwindow, fg_color = C_verde, text = (' '), image=imagen_tk)
imagen_label.pack()

# Titulo 'ingrese su usuario'
texto_usuario = ctk.CTkLabel(mainwindow, text=("Ingrese su usuario "), font=(fuente1, 20), fg_color = C_verde)
texto_usuario.pack(padx=10, pady=1)

# Crear el campo de entrada para el usuario
usuario = ctk.CTkEntry(mainwindow, placeholder_text="Usuario", width=300, font=(fuente1), border_color= C_azul, border_width= 4)
usuario.pack(padx=10, pady=10)

# Titulo 'ingrese su contraseña'
texto_contraseña = ctk.CTkLabel(mainwindow, text=("Ingrese su contraseña"), font=(fuente1, 20), fg_color = C_verde)
texto_contraseña.pack(padx=10, pady=1)

# Crear el campo de entrada para la contraseña
contreseña = ctk.CTkEntry(mainwindow, placeholder_text="Contraseña", width=300, font=(fuente1), show="*", border_color= C_azul, border_width= 4)
contreseña.pack(padx=10, pady=10)

# Crear el campo de entrada para el checkbox
checkbox = ctk.CTkCheckBox(mainwindow, text="¿Mantener sesion?", font=(fuente1))
checkbox.pack(padx=10, pady=10)

# Funcion para la nueva instancia
def open_toplevel():
    toplevel_window = ToplevelWindow(mainwindow)

# Boton de login
button = ctk.CTkButton(mainwindow, text=("Login"), cursor="hand2", font=(fuente1, 15),fg_color = C_azul2 , command=open_toplevel, )
button.pack(padx=10, pady=10)

# inicio del loop
mainwindow.mainloop()
