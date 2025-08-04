import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import sys

# ------------------- RUTA SEGURA PARA IMÁGENES -------------------

def ruta_recurso(nombre_archivo):
    """Devuelve la ruta del archivo, compatible con PyInstaller"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, 'resources', nombre_archivo)

# ------------------- VALIDACIÓN DEL AUTÓMATA -------------------

def validar_cadena(cadena):
    estado = 'A'
    for simbolo in cadena:
        if estado == 'A':
            if simbolo == 'a':
                estado = 'B'
            elif simbolo in ['b', 'c']:
                estado = 'C'
            else:
                return False
        elif estado == 'B':
            if simbolo == 'a':
                estado = 'B'
            elif simbolo in ['b', 'c']:
                estado = 'C'
            else:
                return False
        elif estado == 'C':
            if simbolo in ['b', 'c']:
                estado = 'C'
            elif simbolo == 'a':
                estado = 'B'
            elif simbolo == 'z':
                estado = 'D'
            else:
                return False
        elif estado == 'D':
            return False
    return estado == 'D'

# ------------------- FUNCIÓN BOTÓN -------------------

def verificar():
    cadena = entrada.get()
    if validar_cadena(cadena):
        messagebox.showinfo("Resultado", "✅ Cadena ACEPTADA por el autómata.")
    else:
        messagebox.showwarning("Resultado", "❌ Cadena NO aceptada.")

# ------------------- INTERFAZ GRÁFICA -------------------

ventana = tk.Tk()
ventana.title("Validador de Cadenas - Autómata")
ventana.geometry("500x550")
ventana.configure(bg="#f0f0f0")

# Imagen del autómata
ruta_imagen = ruta_recurso("automata.png")
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((400, 160), Image.Resampling.LANCZOS)
imagen_tk = ImageTk.PhotoImage(imagen)

etiqueta_imagen = tk.Label(ventana, image=imagen_tk, bg="#f0f0f0")
etiqueta_imagen.image = imagen_tk  # Importante: evitar que la imagen se borre
etiqueta_imagen.pack(pady=20)

# Título
titulo = tk.Label(ventana, text="Simulador de Autómata Finito Determinista", font=("Arial", 14, "bold"), bg="#f0f0f0")
titulo.pack(pady=5)

# Entrada de texto
etiqueta = tk.Label(ventana, text="Ingrese una cadena (por ejemplo: abz):", font=("Arial", 11), bg="#f0f0f0")
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana, width=40, font=("Arial", 11))
entrada.pack(pady=5)

# Botón
boton = tk.Button(ventana, text="Validar cadena", command=verificar, font=("Arial", 11), bg="#4CAF50", fg="white", padx=10, pady=5)
boton.pack(pady=15)

# Pie
pie = tk.Label(ventana, text="Hecho por FREDY BATZ · 2025", font=("Arial", 9), bg="#f0f0f0", fg="gray")
pie.pack(side="bottom", pady=10)

ventana.mainloop()
