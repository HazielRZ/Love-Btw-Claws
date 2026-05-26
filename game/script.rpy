# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define m = Character("Maru-chan")
define mt = Character("Maru-chan", what_prefix="({i}", what_suffix="{/i})", color="#faa046") #pensando
define n = Character("Narrador")
default a = 3
define p = Character("[mc]", color="#faa046")
define pt = Character("[mc]", what_prefix="({i}", what_suffix="{/i})", color="#faa046") #pensando
define p1 = Character("[mcl]", color="#faa046") #hablando normal
define mc_ka = Character("Both", color="#fd6b5e") #mc pensando
define ch_ka = Character("Both", color="#817ab9") #chica pensando
default mc = "Yorch"

# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene station

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show eileen happy at left
    show uma-musume-fine-motion at right

    # Presenta las líneas del diálogo.

    $ mc = renpy.input("Cual es tu nombre? (Yorch)", length=15)
    $ mc = mc.strip() or "Yorch"
    $ persistent.mc = mc
    p "Hola, mi nombre es [mc], se preguntaran que hago aqui, pues mi abuelo se petateo un gran hombre sin duda "
    p "Y me dejo su restaurante a la orilla de la playa 'Mariscos sin nombre 2 ' y ahora sera mi responsabilidad"
    p "No tenia las mas minimas ganas de seguir con su negocio pero sus deudas por las  apuestas de caballos ascienden a los 3 Millones de sheintavos"
    p "Nunca logramos hacerlo entender que los caballitos de mar no competian en Nakayama y que su caballo favorito Gentildonna habia muerto hace 201 anios en el 2025"
    p "Bueno parece que ya llegamos a Nueva Veracru, me apurare antes de que aparezcan los mayates."
    scene station2with dissolve
    show maru-chan at truecenter
    mt "Jaibas, voy tarde para llegar a la escuela"
    p "Parece que tengo que caminar 5km desde esta estacion"
    "Chocas con una chica"

    "Que haces?"

    menu:
        "Ayudarla a recoger tus cosas y disculparte.":
            jump si
        "Solo me gustan los femboys y no le ayudo.":
            jump fm

label si:
     "Le ayudas a recoger sus cosas."
     m "lo siento iba distraida"
    jump xd

label fm:
    n "Un fanatico de los autos con palanca."
    jump xd

label xd:
    # Finaliza el juego:
    return
