import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

# Nombre del archivo JSON
archivo_db = 'personajes_demon_slayer.json'

# Cargar personajes desde el archivo JSON
def cargar_personajes():
    if os.path.exists(archivo_db):
        with open(archivo_db, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return [
            {"nombre": "Tanjiro Kamado", "es_cazador": True, "es_pilar": False, "es_demonio": False, "usa_aliento": True, "es_hombre": True, "es_heroe": True, "esta_vivo": True},
            {"nombre": "Nezuko Kamado", "es_cazador": False, "es_pilar": False, "es_demonio": True, "usa_aliento": False, "es_hombre": False, "es_heroe": True, "esta_vivo": True},
            {"nombre": "Giyu Tomioka", "es_cazador": True, "es_pilar": True, "es_demonio": False, "usa_aliento": True, "es_hombre": True, "es_heroe": True, "esta_vivo": True},
            {"nombre": "Kyojuro Rengoku", "es_cazador": True, "es_pilar": True, "es_demonio": False, "usa_aliento": True, "es_hombre": True, "es_heroe": True, "esta_vivo": False},
            {"nombre": "Muzan Kibutsuji", "es_cazador": False, "es_pilar": False, "es_demonio": True, "usa_aliento": False, "es_hombre": True, "es_heroe": False, "esta_vivo": True},
            {"nombre": "Shinobu Kocho", "es_cazador": True, "es_pilar": True, "es_demonio": False, "usa_aliento": True, "es_hombre": False, "es_heroe": True, "esta_vivo": True},
            {"nombre": "Akaza", "es_cazador": False, "es_pilar": False, "es_demonio": True, "usa_aliento": False, "es_hombre": True, "es_heroe": False, "esta_vivo": True}
        ]

# Guardar personajes en el archivo JSON
def guardar_personajes(personajes):
    with open(archivo_db, 'w', encoding='utf-8') as file:
        json.dump(personajes, file, ensure_ascii=False, indent=4)

# Clase del juego
class AkinatorDemonSlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina el personaje de Demon Slayer")
        self.root.geometry("800x500")  # Tamaño de la ventana aumentado
        self.root.config(bg="#FAD02E")  # Color de fondo amarillo claro

        self.personajes = cargar_personajes()
        self.preguntas = [
            ("es_cazador", "¿Es un cazador de demonios?"),
            ("es_pilar", "¿Es un pilar?"),
            ("es_demonio", "¿Es un demonio?"),
            ("usa_aliento", "¿Usa técnica de aliento?"),
            ("es_hombre", "¿Es hombre?"),
            ("es_heroe", "¿Es un héroe?"),
            ("esta_vivo", "¿Está vivo?")
        ]
        self.posibles = self.personajes.copy()
        self.current_question = 0

        self.label = tk.Label(root, text="¡Bienvenido a adivina el personaje de Demon Slayer!", bg="#FAD02E", font=("Helvetica", 20))
        self.label.pack(pady=20)

        self.button_yes = tk.Button(root, text="Iniciar", command=self.iniciar_juego, width=20, height=3, bg="#FFD700", font=("Helvetica", 16))
        self.button_yes.pack(pady=5)

        self.button_no = tk.Button(root, text="Salir", command=root.quit, width=20, height=3, bg="#FFD700", font=("Helvetica", 16))
        self.button_no.pack(pady=5)

        self.frame_respuestas = tk.Frame(root, bg="#FAD02E")
        self.frame_respuestas.pack(pady=20)

    def iniciar_juego(self):
        self.label.config(text="Responde a las preguntas usando los botones.")
        self.posibles = self.personajes.copy()
        self.current_question = 0
        self.mostrar_respuestas(False)
        self.preguntar()

    def mostrar_respuestas(self, mostrar):
        for widget in self.frame_respuestas.winfo_children():
            widget.destroy()

        if mostrar:
            self.button_yes.pack_forget()
            self.button_no.pack_forget()

            tk.Button(self.frame_respuestas, text="Sí", command=lambda: self.responder("sí"), width=10, height=2, font=("Helvetica", 16), bg="#98FB98").pack(side=tk.LEFT, padx=10)
            tk.Button(self.frame_respuestas, text="No", command=lambda: self.responder("no"), width=10, height=2, font=("Helvetica", 16), bg="#FF7F7F").pack(side=tk.LEFT, padx=10)
            tk.Button(self.frame_respuestas, text="Salir", command=self.root.quit, width=10, height=2, font=("Helvetica", 16), bg="#FFB6C1").pack(side=tk.LEFT, padx=10)

    def preguntar(self):
        if self.current_question < len(self.preguntas):
            atributo, pregunta = self.preguntas[self.current_question]
            self.label.config(text=pregunta)
            self.mostrar_respuestas(True)
        else:
            self.fin_juego(None)

    def responder(self, respuesta):
        atributo, pregunta = self.preguntas[self.current_question]
        
        if respuesta == "no":
            self.posibles = [p for p in self.posibles if not p[atributo]]
        else:
            self.posibles = [p for p in self.posibles if p[atributo]]

        self.current_question += 1
        if len(self.posibles) == 1:
            self.fin_juego(self.posibles[0]["nombre"])
        elif len(self.posibles) == 0:
            self.fin_juego(None)
        else:
            self.preguntar()

    def fin_juego(self, resultado):
        self.mostrar_respuestas(False)
        if resultado:
            confirmacion = messagebox.askyesno("Confirmación", f"¿Tu personaje es {resultado}?", parent=self.root)
            if confirmacion:
                self.label.config(text=f"¡Adiviné! Tu personaje es {resultado}!")
                self.root.after(2000, self.iniciar_juego)
            else:
                self.label.config(text="No pude adivinar. ¿Quieres añadir un nuevo personaje?")
                tk.Button(self.frame_respuestas, text="Sí", command=self.agregar_personaje, bg="#98FB98", width=10, height=2, font=("Helvetica", 16)).pack(side=tk.LEFT, padx=5)
                tk.Button(self.frame_respuestas, text="No", command=self.iniciar_juego, bg="#FF7F7F", width=10, height=2, font=("Helvetica", 16)).pack(side=tk.LEFT, padx=5)
        else:
            self.label.config(text="No pude adivinar. ¿Quieres añadir un nuevo personaje?")
            tk.Button(self.frame_respuestas, text="Sí", command=self.agregar_personaje, bg="#98FB98", width=10, height=2, font=("Helvetica", 16)).pack(side=tk.LEFT, padx=5)
            tk.Button(self.frame_respuestas, text="No", command=self.iniciar_juego, bg="#FF7F7F", width=10, height=2, font=("Helvetica", 16)).pack(side=tk.LEFT, padx=5)

    def agregar_personaje(self):
        nombre = simpledialog.askstring("Nombre del personaje", "¿Cuál es el nombre del personaje?", parent=self.root)
        if nombre:
            es_cazador = simpledialog.askstring("Atributo", "¿Es un cazador de demonios? (si/no)", parent=self.root).strip().lower() == 'si'
            es_pilar = simpledialog.askstring("Atributo", "¿Es un pilar? (si/no)", parent=self.root).strip().lower() == 'si'
            es_demonio = simpledialog.askstring("Atributo", "¿Es un demonio? (si/no)", parent=self.root).strip().lower() == 'si'
            usa_aliento = simpledialog.askstring("Atributo", "¿Usa técnica de aliento? (si/no)", parent=self.root).strip().lower() == 'si'
            es_hombre = simpledialog.askstring("Atributo", "¿Es hombre? (si/no)", parent=self.root).strip().lower() == 'si'
            es_heroe = simpledialog.askstring("Atributo", "¿Es un héroe? (si/no)", parent=self.root).strip().lower() == 'si'
            esta_vivo = simpledialog.askstring("Atributo", "¿Está vivo? (si/no)", parent=self.root).strip().lower() == 'si'

            self.personajes.append({
                "nombre": nombre,
                "es_cazador": es_cazador,
                "es_pilar": es_pilar,
                "es_demonio": es_demonio,
                "usa_aliento": usa_aliento,
                "es_hombre": es_hombre,
                "es_heroe": es_heroe,
                "esta_vivo": esta_vivo,
            })
            guardar_personajes(self.personajes)
            self.label.config(text=f"{nombre} agregado a la base de datos!")
            self.root.after(2000, self.iniciar_juego)

if __name__ == "__main__":
    root = tk.Tk()
    juego = AkinatorDemonSlayer(root)
    root.mainloop()

