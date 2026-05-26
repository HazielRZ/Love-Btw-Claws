################################################################################
## Inicialización
################################################################################

## La sentencia 'init offset' da preferencia a las sentencias de inicialización
## de este archivo respecto a otros archivos.
init offset = -2

## Llamando 'gui.init' se resetean los estilos a los valores por defecto y se
## establecen la anchura y altura del juego.
init python:
    gui.init(1920, 1080)

## Habilitar comprobaciones de propiedades no válidas o inestables en pantallas
## o transformaciones.
define config.check_conflicting_properties = True


################################################################################
## Variables de configuración de la interfaz.
################################################################################

## Colores #####################################################################
##
## Los colores del texto de la interfaz — Paleta "Ocean Breeze"

## El color enfatizado usado en la interfaz (Ámbar cálido).
define gui.accent_color = '#FF8C42'

## El color del botón de texto cuando no está seleccionado ni enfocado (Azul cielo suave).
define gui.idle_color = '#B8D8E8'

## El color 'small' se usa para el texto pequeño, que necesita destacar más (Cian suave).
define gui.idle_small_color = '#8BB8CC'

## El color usado en botones y barras que ganan foco (Coral suave).
define gui.hover_color = '#FF6B6B'

## El color del botón de texto seleccionado pero no enfocado (Dorado naranja).
define gui.selected_color = '#FFB347'

## El color de los botones de texto que no pueden ser seleccionados.
define gui.insensitive_color = '#4A5568'

## Colores de la parte vacía de las barras (Océano profundo).
define gui.muted_color = '#1B3A4B'
define gui.hover_muted_color = '#2E86AB'

## Colores del texto del diálogo y menú (Claro para fondos oscuros).
define gui.text_color = '#EAEEF2'
define gui.interface_text_color = '#D0D8E0'


## Tipos y tamaños de letra ####################################################

## El tipo de letra del texto del juego
define gui.text_font = "DejaVuSans.ttf"

## El tipo de letra de los nombres de personajes
define gui.name_text_font = "DejaVuSans.ttf"

## El tipo de letra del texto externo al juego.
define gui.interface_text_font = "DejaVuSans.ttf"

## El tamaño normal del texto del diálogo.
define gui.text_size = 33

## El tamaño de los nombres de los personajes
define gui.name_text_size = 45

## El tamaño del texto en la interfaz.
define gui.interface_text_size = 33

## El tamaño de etiquetas en la interfaz.
define gui.label_text_size = 36

## El tamaño del texto en las notificaciones.
define gui.notify_text_size = 24

## El tamaño del título del juego.
define gui.title_text_size = 75


## Menú principal y menús del juego ############################################

## Imágenes del menú principal y menús del juego.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Diálogo #####################################################################
##
## Estas variables controlan cómo se muestra el diálogo en la pantalla, una
## línea cada vez.

## Altura de la caja de texto que contiene el diálogo.
define gui.textbox_height = 278

## Colocación vertical de la caja de texto en la pantalla. 0.0 para la parte
## superior, 0.5 para el centro y 1.0 para la parte inferior.
define gui.textbox_yalign = 1.0

## Colocación del nombre del personaje hablante, relativa a la caja de texto.
define gui.name_xpos = 360
define gui.name_ypos = 0

## La alineación horizontal del nombre del personaje.
define gui.name_xalign = 0.0

## La anchura, altura y bordes de la caja que contiene el nombre del personaje.
define gui.namebox_width = None
define gui.namebox_height = None

## Los bordes de la caja que contiene el nombre del personaje.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Si es 'True', el fondo de la caja del nombre será en mosaico.
define gui.namebox_tile = False

## Colocación del diálogo relativa a la caja de texto.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## La anchura máxima del texto del diálogo, en píxels.
define gui.dialogue_width = 1116

## La alineación horizontal del texto del diálogo.
define gui.dialogue_text_xalign = 0.0


## Botones #####################################################################
##
## Estas variables, junto con las imágenes de 'gui/button', controlan el aspecto
## de los botones.

## La anchura y altura del botón, en píxels. Si es 'None', Ren'Py calcula el
## tamaño.
define gui.button_width = None
define gui.button_height = None

## Los bordes de cada lado del botón.
define gui.button_borders = Borders(6, 6, 6, 6)

## Si es 'True', la imagen de fondo será en mosaico.
define gui.button_tile = False

## Tipo de letra del botón.
define gui.button_text_font = gui.interface_text_font

## Tamaño de letra del botón.
define gui.button_text_size = gui.interface_text_size

## El color del texto del botón en varios estados.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## La alineación horizontal del texto del botón.
define gui.button_text_xalign = 0.0

## Personalizaciones de botones específicos:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color


## Botones de opción ###########################################################
##
## Los botones de opción se utilizan en los menús del juego.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#B8D8E8'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#4A556880'


## Botones de partidas #########################################################
##
## El botón de hueco de partida es un botón especial.

define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## La anchura y altura de las miniaturas de las partidas guardadas.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## Número de columnas y filas de la cuadrícula de partidas guardadas.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Posicionamiento y espacios ##################################################

## Posición del lado izquierdo de los botones de navegación.
define gui.navigation_xpos = 60

## Posición vertical del indicador de salto.
define gui.skip_ypos = 15

## Posición vertical de la pantalla de notificación.
define gui.notify_ypos = 68

## Espacio entre opciones de menú.
define gui.choice_spacing = 33

## Botones en la sección de navegación del menú principal y el menú del juego.
define gui.navigation_spacing = 6

## Controla el espacio entre preferencias.
define gui.pref_spacing = 15

## Controla el espacio entre botones de preferencia.
define gui.pref_button_spacing = 0

## Espacio entre botones de página.
define gui.page_spacing = 0

## Espacio entre huecos de guardado.
define gui.slot_spacing = 15

## Posición del texto del menú principal.
define gui.main_menu_text_xalign = 1.0


## Marcos ######################################################################

## Marcos genéricos
define gui.frame_borders = Borders(6, 6, 6, 6)

## Marco usado en la pantalla de confirmación.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## Marco usado en la pantalla de salto.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## Marco usado en la pantalla de notificación.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## ¿El fondo del marco debe ser en mosaico?
define gui.frame_tile = False


## Barras, barras de desplazamiento y deslizadores #############################

## Altura de las barras horizontales. Anchura de las barras verticales.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## Mosaico de barras.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Bordes horizontales.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Bordes verticales.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## Ocultar barras de desplazamiento no desplegables.
define gui.unscrollable = "hide"


## Historial ###################################################################

## Número de bloques de historial de diálogo que Ren'Py conserva.
define config.history_length = 250

## Altura de una entrada de la pantalla de historial.
define gui.history_height = 210

## Espacio adicional para añadir entre las entradas de la pantalla de historial.
define gui.history_spacing = 0

## Posición, anchura y alineación de la etiqueta con el nombre del personaje.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## Posición, anchura y alineación del texto del diálogo.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## Modo-NVL ####################################################################

## Bordes del fondo de la ventana del modo NVL.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## Máximo número de entradas en modo NVL.
define gui.nvl_list_length = 6

## Altura de una entrada en modo NVL.
define gui.nvl_height = 173

## Espacio entre entradas en modo NVL.
define gui.nvl_spacing = 15

## Posición, anchura y alineación de la etiqueta del personaje.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## Posición, anchura y alineación del texto del diálogo.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## Posición del texto 'nvl_thought'.
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## Posición de los botones de menú NVL.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Localización ################################################################

define gui.language = "unicode"


################################################################################
## Dispositivos Móviles
################################################################################

init python:

    ## Esto aumenta el tamaño de los botones rápidos para facilitar su acceso
    ## en tablets y teléfonos.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## Esto cambia el tamaño y espaciado de varios elementos de la GUI para
    ## asegurar que sean fácilmente visibles en los teléfonos.
    @gui.variant
    def small():

        ## Tamaños de letra.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Ajusta la colocación de la caja de texto.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Cambia el tamaño y espaciado de varios elementos.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## Distribución de botones de archivo.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## Modo-NVL
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
