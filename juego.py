import random
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.font import Font
from tkinter import font
import sys
import os

# Creamos una variable digitos que va a contener los numeros que vamos a usar el juego
digitos = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

# Creamos una variable llamada codigo y le asigna un valor inicial de una cadena vacía. 
# Esto lo hacemos para inicializar una variable de tipo cadena antes de asignarle un 
# valor específico más adelante en el código.
codigo = ''

# Creamos una funcion que genera un numero aleatorio de 4 digitos, usamos la funcion Choice
# del modulo Random
def generar_codigo():
    global codigo
    codigo = ''
    for i in range(4):
        candidato = random.choice(digitos)
        while candidato in codigo:
            candidato = random.choice(digitos)
        codigo += candidato

def verificar_jugada(event=None):
    jugada = entry.get()
    aciertos = 0
    coincidencias = 0

    for i in range(4):
        if jugada[i] == codigo[i]:
            aciertos += 1
        elif jugada[i] in codigo:
            coincidencias += 1
    if aciertos == 4:
        messagebox.showinfo("¡Ganador!", "¡Felicidades! Has acertado el número.")
        reiniciar_juego()
    else:
        resultado_label.config(text=f"Aciertos: {aciertos} - Coincidencias: {coincidencias}")
        entry.delete(0, tk.END)
        entry.focus()        

def reiniciar_juego():
    generar_codigo()
    resultado_label.config(text="")
    entry.delete(0, tk.END)

# Crear la ventana
window = tk.Tk()
window.title("Adivina el Número")
window.configure(bg="#1f5bce")
bold_font =font.Font(family="Arial", size=13, weight="bold")

# Cargar la imagen de fondo
temp_dir = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.abspath(".")

# Construir la ruta del archivo de imagen
image_path = os.path.join(temp_dir, "fondo2.jpg")

# Cargar la imagen de fondo
background_image = ImageTk.PhotoImage(Image.open(image_path))

#Crear un Label para mostrar la imagen de fondo
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Generar el código inicial
generar_codigo()

# Etiquetas
info_label = tk.Label(window,    
    text="Adivine un número de 4 cifras sin que se repitan",
    font=bold_font,
    bg="black",
    fg="white",
    relief="ridge",
    borderwidth=4,
    width=40,
    height=2,
)
info_label.place(relx=0.15, rely=0.05)

resultado_label = tk.Label(window,
    text="",
    bg="lightgray",
)
resultado_label.place(relx=0.35, rely=0.2, relwidth=0.3, relheight=0.05)

# Entrada de texto
entry_font = Font(family="Arial", size=28)  
entry = tk.Entry(window,
    bg="white",
    fg="black",
    relief="ridge",
    borderwidth=4,
    font=entry_font,
    highlightbackground="black",
)
entry.place(
    relx=0.425,
    rely=0.35,
    relheight=0.15,
    relwidth=0.17,
)

# Botones
verificar_button = tk.Button(window, 
    text="Verificar",
    #font=("Arial, 9"),
    bg="#ea674c",
    fg="black",
    relief="ridge",
    borderwidth=4,
    command=verificar_jugada,
    font=bold_font
)
verificar_button.place(
    relx=0.445,
    rely=0.55,
    relheight=0.075,
    relwidth=0.13,
)   

reiniciar_button = tk.Button(window, 
    text="Reiniciar el juego",
    font=bold_font,
    bg="green",
    fg="black",
    relief="ridge",
    borderwidth=4,
    command=reiniciar_juego
)
reiniciar_button.place(
   relx=0.375,
   rely=0.85,
   relwidth=0.25,
   relheight=0.1,
)

window.bind('<Return>', verificar_jugada)

# Ejecutar la ventana
window.geometry("600x400")
window.mainloop()
