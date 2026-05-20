# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")
define n = Character("Narrador")
default a = 3

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

    n "Hola Yorch"



    menu:
        "Yorch es Gay":
            call label_with_params(5)
        "Nomas le gustan los femboys":
            jump label_without_params
    jump start

label label_with_params(a):
label label_without_params:
    e "a = [a]" # displays 5 or 3 depending on what path was taken

    e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    # Finaliza el juego:

    return