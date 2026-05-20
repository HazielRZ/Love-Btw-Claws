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

    scene bg room

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
    n "Hola Yorch"

    menu:
        "Yorch es Gay":
            call label_with_params(5)
        "Nomas le gustan los femboys":
            call label_without_params

    e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    # Finaliza el juego:
    return

label label_with_params(a_param):
    e "a = [a_param]"
    return

label label_without_params:
    e "a = [a]"
    return
