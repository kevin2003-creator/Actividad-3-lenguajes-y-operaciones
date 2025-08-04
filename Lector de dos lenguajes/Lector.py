import customtkinter as ctk
from tkinter import simpledialog

# Configurar apariencia
ctk.set_appearance_mode("dark")  # Opcional: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # Puedes cambiar a "green", "dark-blue", etc.

ALFABETO1 = {'λ', '0', '1'}
ALFABETO2 = {'λ', 'a', 'b'}

def limpiar(palabra):
    return palabra.replace('λ', '')

class LenguajeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Lenguajes Formales - GUI Profesional")
        self.geometry("1000x600")

        self.lenguaje1 = set()
        self.lenguaje2 = set()

        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.crear_widgets()

    def crear_widgets(self):
        # Sección Lenguaje 1
        self.label1 = ctk.CTkLabel(self, text="Lenguaje 1 (Σ1 = {λ, 0, 1})", font=("Arial", 16))
        self.label1.grid(row=0, column=0, pady=10)
        self.entry1 = ctk.CTkEntry(self)
        self.entry1.grid(row=1, column=0, pady=5)
        ctk.CTkButton(self, text="Agregar", command=lambda: self.agregar(1)).grid(row=2, column=0, pady=2)
        ctk.CTkButton(self, text="Eliminar", command=lambda: self.eliminar(1)).grid(row=3, column=0, pady=2)
        ctk.CTkButton(self, text="Mostrar", command=lambda: self.mostrar(1)).grid(row=4, column=0, pady=2)

        # Sección Lenguaje 2
        self.label2 = ctk.CTkLabel(self, text="Lenguaje 2 (Σ2 = {λ, a, b})", font=("Arial", 16))
        self.label2.grid(row=0, column=1, pady=10)
        self.entry2 = ctk.CTkEntry(self)
        self.entry2.grid(row=1, column=1, pady=5)
        ctk.CTkButton(self, text="Agregar", command=lambda: self.agregar(2)).grid(row=2, column=1, pady=2)
        ctk.CTkButton(self, text="Eliminar", command=lambda: self.eliminar(2)).grid(row=3, column=1, pady=2)
        ctk.CTkButton(self, text="Mostrar", command=lambda: self.mostrar(2)).grid(row=4, column=1, pady=2)

        # Sección de operaciones
        self.op_label = ctk.CTkLabel(self, text="Operaciones", font=("Arial", 16, "bold"))
        self.op_label.grid(row=0, column=2, pady=10)
        ctk.CTkButton(self, text="Concatenación", command=self.concatenacion).grid(row=1, column=2, pady=2)
        ctk.CTkButton(self, text="Potencia", command=self.potencia).grid(row=2, column=2, pady=2)
        ctk.CTkButton(self, text="Inversa", command=self.inversa).grid(row=3, column=2, pady=2)
        ctk.CTkButton(self, text="Unión", command=self.union).grid(row=4, column=2, pady=2)
        ctk.CTkButton(self, text="Intersección", command=self.interseccion).grid(row=5, column=2, pady=2)
        ctk.CTkButton(self, text="Diferencia", command=self.diferencia).grid(row=6, column=2, pady=2)

        # Área de resultados
        self.resultado = ctk.CTkTextbox(self, width=900, height=200, font=("Consolas", 13))
        self.resultado.grid(row=7, column=0, columnspan=3, pady=20, padx=20)

    def validar_palabra(self, palabra, lenguaje):
        alfabeto = ALFABETO1 if lenguaje == 1 else ALFABETO2
        return all(c in alfabeto for c in palabra)

    def agregar(self, lenguaje):
        entrada = self.entry1.get() if lenguaje == 1 else self.entry2.get()
        palabra = limpiar(entrada)
        if self.validar_palabra(entrada, lenguaje):
            if lenguaje == 1:
                self.lenguaje1.add(palabra)
            else:
                self.lenguaje2.add(palabra)
            self.mostrar_resultado(f"Palabra '{entrada}' agregada al lenguaje {lenguaje}.")
        else:
            self.mostrar_resultado("Error: Caracteres inválidos en la palabra.")

    def eliminar(self, lenguaje):
        entrada = self.entry1.get() if lenguaje == 1 else self.entry2.get()
        palabra = limpiar(entrada)
        target = self.lenguaje1 if lenguaje == 1 else self.lenguaje2
        if palabra in target:
            target.remove(palabra)
            self.mostrar_resultado(f"Palabra '{entrada}' eliminada del lenguaje {lenguaje}.")
        else:
            self.mostrar_resultado("La palabra no está en el lenguaje.")

    def mostrar(self, lenguaje):
        datos = self.lenguaje1 if lenguaje == 1 else self.lenguaje2
        self.mostrar_resultado(f"Lenguaje {lenguaje}: {datos if datos else 'Vacío'}")

    def concatenacion(self):
        resultado = {x + y for x in self.lenguaje1 for y in self.lenguaje2}
        self.mostrar_resultado(f"Concatenación: {resultado}")

    def potencia(self):
        lenguaje_num = simpledialog.askinteger("Potencia", "¿Lenguaje (1 o 2)?")
        exp = simpledialog.askinteger("Potencia", "¿A qué potencia elevar? (≥0)")
        lenguaje = self.lenguaje1 if lenguaje_num == 1 else self.lenguaje2

        if exp is None or exp < 0:
            self.mostrar_resultado("Potencia inválida.")
            return

        if exp == 0:
            resultado = {""}
        else:
            resultado = lenguaje.copy()
            for _ in range(exp - 1):
                resultado = {x + y for x in resultado for y in lenguaje}

        self.mostrar_resultado(f"Lenguaje {lenguaje_num} ^ {exp} = {resultado}")

    def inversa(self):
        lenguaje_num = simpledialog.askinteger("Inversa", "¿Lenguaje (1 o 2)?")
        lenguaje = self.lenguaje1 if lenguaje_num == 1 else self.lenguaje2
        resultado = {palabra[::-1] for palabra in lenguaje}
        self.mostrar_resultado(f"Inversa del lenguaje {lenguaje_num}: {resultado}")

    def union(self):
        resultado = self.lenguaje1.union(self.lenguaje2)
        self.mostrar_resultado(f"Unión: {resultado}")

    def interseccion(self):
        resultado = self.lenguaje1.intersection(self.lenguaje2)
        self.mostrar_resultado(f"Intersección: {resultado}")

    def diferencia(self):
        resultado = self.lenguaje1.difference(self.lenguaje2)
        self.mostrar_resultado(f"Diferencia (L1 - L2): {resultado}")

    def mostrar_resultado(self, texto):
        self.resultado.delete("1.0", "end")
        self.resultado.insert("1.0", texto)

if __name__ == "__main__":
    app = LenguajeApp()
    app.mainloop()

