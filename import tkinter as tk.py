import tkinter as tk
import random

# Datos del juego
historias = [
    {
        'descripcion': "Mario fue encontrado muerto en el Bosque de los Colomos. Encuentra a su asesino.",
        'personas': ['Orlando', 'Marifer', 'Mau', 'Leo', 'Antonio'],
        'objetos': ['Piedra', 'Cuchillo', 'Veneno', 'Cuerda', 'Navaja'],
        'lugares': ['Claro del bosque', 'Lago', 'Sendero', 'Cabaña abandonada', 'Mirador'],
        'asesino': 'Marifer',
        'objeto_asesino': 'Cuchillo',
        'lugar_asesinato': 'Lago',
        'pistas': {
            'Orlando': 'Orlando fue visto cerca del lago antes del asesinato.',
            'Marifer': 'Marifer fue vista entrando al claro poco antes del asesinato.',
            'Mau': 'Mau estaba en el mirador hablando por teléfono.',
            'Leo': 'Leo estaba solo en la cabaña abandonada, cerca del lugar del crimen.',
            'Antonio': 'Antonio estaba en el sendero corriendo.',
            'Piedra': 'No parece que se haya usado una piedra para el asesinato.',
            'Cuchillo': 'Se encontraron heridas de cuchillo en el cuerpo de Mario.',
            'Veneno': 'Mario no muestra signos de envenenamiento.',
            'Cuerda': 'No hay marcas de estrangulamiento en el cuerpo.',
            'Navaja': 'La navaja no tiene rastros de sangre.',
            'Claro del bosque': 'El claro muestra signos de una pelea.',
            'Lago': 'El lago estaba tranquilo, no se reportó actividad sospechosa.',
            'Sendero': 'El sendero estaba vacío en el momento del crimen.',
            'Cabaña abandonada': 'La cabaña estaba cerrada y sin actividad.',
            'Mirador': 'El mirador estaba vacío salvo por Mau que hablaba por teléfono.'
        }
    },
    {
        'descripcion': "La escritora Ana fue hallada sin vida . Encuentra al culpable.",
        'personas': ['Carlos', 'Lucía', 'Pedro', 'Sofía', 'Diego'],
        'objetos': ['Tijeras', 'Veneno', 'Libros', 'Laptop', 'Cuchillo'],
        'lugares': ['Estudio', 'Cocina', 'Salón', 'Baño', 'Terraza'],
        'asesino': 'Carlos',
        'objeto_asesino': 'Tijeras',
        'lugar_asesinato': 'Estudio',
        'pistas': {
            'Carlos': 'Carlos fue el último en ver a Ana antes de su muerte.',
            'Lucía': 'Lucía estaba en la terraza leyendo.',
            'Pedro': 'Pedro estaba en la cocina cocinando.',
            'Sofía': 'Sofía se encontraba en el salón, mirando televisión.',
            'Diego': 'Diego estaba en el baño cuando ocurrió el crimen.',
            'Tijeras': 'Las tijeras estaban manchadas de sangre.',
            'Veneno': 'Ana no tenía signos de envenenamiento.',
            'Libros': 'Los libros estaban en su lugar, no se usaron como arma.',
            'Laptop': 'La laptop estaba intacta, sin signos de lucha.',
            'Cuchillo': 'No se encontró un cuchillo cerca del cuerpo.',
            'Estudio': 'El estudio estaba desordenado y había un conflicto.',
            'Cocina': 'La cocina no mostraba signos de pelea.',
            'Salón': 'El salón estaba tranquilo durante el crimen.',
            'Baño': 'El baño estaba cerrado.',
            'Terraza': 'La terraza estaba vacía, pero Lucía fue vista allí.'
        }
    },
    {
        'descripcion': "El empresario Miguel fue encontrado muerto . Resuelve el misterio.",
        'personas': ['Andrés', 'Verónica', 'Ricardo', 'Claudia', 'Samuel'],
        'objetos': ['Pistola', 'Bolsas de dinero', 'Botella', 'Portafolios', 'Cuchillo'],
        'lugares': ['Oficina', 'Pasillo', 'Recepción', 'Baño', 'Terraza'],
        'asesino': 'Verónica',
        'objeto_asesino': 'Pistola',
        'lugar_asesinato': 'Oficina',
        'pistas': {
            'Andrés': 'Andrés tenía una disputa con Miguel, pero no estuvo en la oficina.',
            'Verónica': 'Verónica fue vista saliendo de la oficina rápidamente.',
            'Ricardo': 'Ricardo estaba en el pasillo hablando con un cliente.',
            'Claudia': 'Claudia estaba en la recepción atendiendo llamadas.',
            'Samuel': 'Samuel estaba en el baño durante el asesinato.',
            'Pistola': 'La pistola fue encontrada junto al cuerpo.',
            'Bolsas de dinero': 'Las bolsas estaban intactas, no se robaron.',
            'Botella': 'No hay indicios de envenenamiento.',
            'Portafolios': 'El portafolios estaba en su escritorio sin daños.',
            'Cuchillo': 'No se utilizó un cuchillo para el asesinato.',
            'Oficina': 'La oficina tenía signos de lucha y confusión.',
            'Pasillo': 'El pasillo no mostró actividad sospechosa.',
            'Recepción': 'La recepción estaba tranquila.',
            'Baño': 'El baño no fue utilizado durante el crimen.',
            'Terraza': 'La terraza estaba cerrada y sin testigos.'
        }
    },
    {
        'descripcion': "La joven Laura fue hallada muerto . Descubre quién la asesinó.",
        'personas': ['Jorge', 'Clara', 'Fernando', 'Beatriz', 'Tomás'],
        'objetos': ['Botella', 'Cuchillo', 'Cinta', 'Lápiz', 'Veneno'],
        'lugares': ['Sala', 'Cocina', 'Jardín', 'Baño', 'Terraza'],
        'asesino': 'Clara',
        'objeto_asesino': 'Botella',
        'lugar_asesinato': 'Sala',
        'pistas': {
            'Jorge': 'Jorge estaba en la cocina preparando bebidas.',
            'Clara': 'Clara estaba en la sala con Laura antes de que todo ocurriera.',
            'Fernando': 'Fernando fue visto en el jardín hablando con amigos.',
            'Beatriz': 'Beatriz se encontraba en el baño retocándose.',
            'Tomás': 'Tomás estaba en la terraza tocando música.',
            'Botella': 'La botella estaba rota junto al cuerpo.',
            'Cuchillo': 'No se usó un cuchillo en el asesinato.',
            'Cinta': 'La cinta no fue encontrada en la escena.',
            'Lápiz': 'El lápiz no tiene relación con el caso.',
            'Veneno': 'No hay signos de veneno en el cuerpo.',
            'Sala': 'La sala estaba desordenada, indicando una pelea.',
            'Cocina': 'La cocina estaba tranquila y en orden.',
            'Jardín': 'El jardín tenía a muchos invitados disfrutando.',
            'Baño': 'El baño estaba ocupado por Beatriz.',
            'Terraza': 'La terraza estaba llena de música y diversión.'
        }
    },
    {
        'descripcion': "El detective Smith fue asesinado . Encuentra al culpable.",
        'personas': ['Mark', 'Eva', 'John', 'Sara', 'Rick'],
        'objetos': ['Cuchillo', 'Pistola', 'Soga', 'Botella', 'Revólver'],
        'lugares': ['Oficina', 'Cafetería', 'Parque', 'Estación', 'Calle'],
        'asesino': 'Eva',
        'objeto_asesino': 'Pistola',
        'lugar_asesinato': 'Oficina',
        'pistas': {
            'Mark': 'Mark estaba en la cafetería al momento del crimen.',
            'Eva': 'Eva salió de la oficina con una actitud sospechosa.',
            'John': 'John estaba en el parque observando.',
            'Sara': 'Sara estaba en la estación de policía.',
            'Rick': 'Rick estaba en la calle hablando por teléfono.',
            'Cuchillo': 'No se usó un cuchillo en el asesinato.',
            'Pistola': 'La pistola fue encontrada en la escena.',
            'Soga': 'No se encontró ninguna soga.',
            'Botella': 'La botella no tenía relevancia en el caso.',
            'Revólver': 'El revólver no se usó en el asesinato.',
            'Oficina': 'La oficina estaba desordenada y con signos de lucha.',
            'Cafetería': 'La cafetería no mostró actividad sospechosa.',
            'Parque': 'El parque estaba lleno de gente.',
            'Estación': 'La estación estaba vigilada.',
            'Calle': 'La calle estaba vacía.'
        }
    }
]

# Funciones del juego
def iniciar_juego():
    global caso
    caso = random.choice(historias)
    texto_descripcion.set(caso['descripcion'])
    # Actualizamos los menús desplegables con las nuevas opciones del caso
    menu_personas.set(caso['personas'][0])
    menu_objetos.set(caso['objetos'][0])
    menu_lugares.set(caso['lugares'][0])
    opciones_personas['menu'].delete(0, 'end')
    opciones_objetos['menu'].delete(0, 'end')
    opciones_lugares['menu'].delete(0, 'end')

    for persona in caso['personas']:
        opciones_personas['menu'].add_command(label=persona, command=tk._setit(menu_personas, persona))
    for objeto in caso['objetos']:
        opciones_objetos['menu'].add_command(label=objeto, command=tk._setit(menu_objetos, objeto))
    for lugar in caso['lugares']:
        opciones_lugares['menu'].add_command(label=lugar, command=tk._setit(menu_lugares, lugar))
    
    frame_inicio.pack_forget()
    frame_juego.pack(padx=20, pady=20, fill="both", expand=True)

def elegir_opcion():
    eleccion_persona = menu_personas.get()
    eleccion_objeto = menu_objetos.get()
    eleccion_lugar = menu_lugares.get()

    if (eleccion_persona == caso['asesino'] and 
        eleccion_objeto == caso['objeto_asesino'] and 
        eleccion_lugar == caso['lugar_asesinato']):
        resultado.set(f"¡Felicidades! Has encontrado al asesino: {caso['asesino']}, "
                      f"el arma: {caso['objeto_asesino']} y el lugar: {caso['lugar_asesinato']}.")
    else:
        pista_persona = caso['pistas'].get(eleccion_persona, "Sin pistas.")
        pista_objeto = caso['pistas'].get(eleccion_objeto, "Sin pistas.")
        pista_lugar = caso['pistas'].get(eleccion_lugar, "Sin pistas.")
        
        resultado.set(f"Pista sobre la persona: {pista_persona}\n"
                      f"Pista sobre el objeto: {pista_objeto}\n"
                      f"Pista sobre el lugar: {pista_lugar}")

# Interfaz gráfica
root = tk.Tk()
root.title("Asesinato en el Bosque de los Colomos")
root.geometry("900x700")

# Pantalla de inicio
frame_inicio = tk.Frame(root)
frame_inicio.pack(fill="both", expand=True)

label_bienvenida = tk.Label(frame_inicio, text="¡Bienvenido al juego del asesinato!", font=("Arial", 20))
label_bienvenida.pack(pady=40)

boton_iniciar = tk.Button(frame_inicio, text="Iniciar Juego", command=iniciar_juego, font=("Arial", 16), width=20)
boton_iniciar.pack()

# Pantalla del juego
frame_juego = tk.Frame(root)

texto_descripcion = tk.StringVar()
label_descripcion = tk.Label(frame_juego, textvariable=texto_descripcion, font=("Arial", 18), wraplength=700, justify="center")
label_descripcion.grid(row=0, column=0, columnspan=3, pady=20)

# Área de opciones
label_persona = tk.Label(frame_juego, text="Selecciona un sospechoso:", font=("Arial", 16))
label_persona.grid(row=1, column=0, pady=15, padx=10, sticky="e")

menu_personas = tk.StringVar(root)
menu_personas.set("Elige una persona")
opciones_personas = tk.OptionMenu(frame_juego, menu_personas, "")
opciones_personas.config(width=15, font=("Arial", 14))
opciones_personas.grid(row=1, column=1, pady=15, padx=10, sticky="w")

label_objeto = tk.Label(frame_juego, text="Selecciona el objeto:", font=("Arial", 16))
label_objeto.grid(row=2, column=0, pady=15, padx=10, sticky="e")

menu_objetos = tk.StringVar(root)
menu_objetos.set("Elige un objeto")
opciones_objetos = tk.OptionMenu(frame_juego, menu_objetos, "")
opciones_objetos.config(width=15, font=("Arial", 14))
opciones_objetos.grid(row=2, column=1, pady=15, padx=10, sticky="w")

label_lugar = tk.Label(frame_juego, text="Selecciona el lugar:", font=("Arial", 16))
label_lugar.grid(row=3, column=0, pady=15, padx=10, sticky="e")

menu_lugares = tk.StringVar(root)
menu_lugares.set("Elige un lugar")
opciones_lugares = tk.OptionMenu(frame_juego, menu_lugares, "")
opciones_lugares.config(width=15, font=("Arial", 14))
opciones_lugares.grid(row=3, column=1, pady=15, padx=10, sticky="w")

# Botón para confirmar elección
boton_elegir = tk.Button(frame_juego, text="Elegir", command=elegir_opcion, font=("Arial", 16), width=10)
boton_elegir.grid(row=4, column=0, columnspan=3, pady=30)

# Resultados
resultado = tk.StringVar()
label_resultado = tk.Label(frame_juego, textvariable=resultado, font=("Arial", 16), wraplength=700, justify="left")
label_resultado.grid(row=5, column=0, columnspan=3, pady=20)

# Ejecutar el programa
root.mainloop()
