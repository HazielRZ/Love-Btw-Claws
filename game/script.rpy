# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")
define n = Character("Narrador")
default a = 3
define p = Character("[mc]", color="#faa046")
define pt = Character("[mc]", what_prefix="({i}", what_suffix="{/i})", color="#faa046")
define p1 = Character("[mcl]", color="#faa046")
define mc_ka = Character("Both", color="#fd6b5e")
define ch_ka = Character("Both", color="#817ab9")
default mc = "Yorch"

# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene black

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show eileen happy at left
    show uma-musume-fine-motion at right

    # Presenta las líneas del diálogo.

    e "Has creado un nuevo juego Ren'Py."
    $ mc = renpy.input("Cual es tu nombre? (Yorch)", length=15)
    $ mc = mc.strip() or "Yorch"
    $ persistent.mc = mc
    p "Mi nombre es [mc]. y soy el encantador de femboys"
    scene black with fade
    scene playa with dissolve
    show ejemplocrab
    n "Hola [mc]"
    "Yorch es gay?"

    menu:
        "Si y mucho.":
            jump si
        "Solo le gustan los femboys.":
            jump fm

label si:
    n "Ya sabiamos."
    jump xd

label fm:
    n "Y el mejor de ellos."
    jump xd

label xd:
    # Finaliza el juego:
    return
