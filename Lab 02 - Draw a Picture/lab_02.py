# Import the "arcade" library
import arcade

# Open up a window.
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Mi Dibujo")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

# Dibuja el césped
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

# Dibuja una nube
def dibujar_nube(x_centro,y_centro,radio,color=arcade.color.WHITE):
    """int,int,float,object->None
    OBJ:Dibuja una nube si le das las coordenadas de un punto
    """
    # Derecha de la nube
    arcade.draw_circle_filled(x_centro, y_centro, radio, color)
    arcade.draw_circle_filled(x_centro-20, y_centro-20, radio, color)
    arcade.draw_circle_filled(x_centro-40, y_centro-40, radio, color)
    # Medio de la nube
    arcade.draw_circle_filled(x_centro-30, y_centro+10, radio, color)
    arcade.draw_circle_filled(x_centro-50, y_centro-10, radio, color)
    arcade.draw_circle_filled(x_centro-70, y_centro-30, radio, color)
    # Izquierda de la nube
    arcade.draw_circle_filled(x_centro-60, y_centro+20, radio, color)
    arcade.draw_circle_filled(x_centro-80, y_centro, radio, color)
    arcade.draw_circle_filled(x_centro-100, y_centro-20, radio, color)

dibujar_nube(670,490,20)
dibujar_nube(300,530,30)

# Dibujar el sol
arcade.draw_circle_filled(0,600,100,arcade.color.YELLOW)
# Dibujar los rayos del sol
arcade.draw_rectangle_filled(0,600,10,300,arcade.color.YELLOW,290)
arcade.draw_rectangle_filled(0,600,10,300,arcade.color.YELLOW,275)
arcade.draw_rectangle_filled(0,600,10,300,arcade.color.YELLOW,330)
arcade.draw_rectangle_filled(0,600,10,300,arcade.color.YELLOW,350)
arcade.draw_rectangle_filled(0,600,10,300,arcade.color.YELLOW,310)

# Dibujar Stickman

# Pierna izquierda
arcade.draw_rectangle_filled(100,200,20,80,arcade.color.BLACK,20)
# Pierna derecha
arcade.draw_rectangle_filled(130,200,20,80,arcade.color.BLACK,340)
# Cuerpo
arcade.draw_rectangle_filled(115,270,20,100,arcade.color.BLACK)
# Cabeza
arcade.draw_circle_outline(125,360,40,arcade.color.BLACK,10)
# Boca
arcade.draw_arc_outline(150,365,60,80,arcade.color.BLACK,200,250,20)
# Ojo
arcade.draw_circle_filled(140,365,5,arcade.color.BLACK)
# Brazo Izquierdo
arcade.draw_rectangle_filled(97,300,20,80,arcade.color.BLACK,150)
# Brazo derecho
arcade.draw_rectangle_filled(133,300,20,80,arcade.color.BLACK,-145)

# Dibujar coche Tesla
arcade.draw_rectangle_filled(550,270,250,80,arcade.color.GRAY)
arcade.draw_triangle_filled(425,310,675,310,550,365,arcade.color.GRAY_BLUE)

# Ventanas
arcade.draw_polygon_filled([[455,315],[610,320],[590,335],[550,350]],arcade.color.BLACK_OLIVE)
arcade.draw_polygon_outline([[455,315],[610,320],[590,335],[550,350]],arcade.color.BLACK,5)
arcade.draw_rectangle_filled(550,332,5,33,arcade.color.BLACK)

# Marca tesla
arcade.draw_text("Tesla Cybertruck",550,250,arcade.color.BLACK)
# Función ruedas
def dibujar_rueda(x_centro,y_centro,radio,color=arcade.color.GRAY):
    """int,int,float,object->None
    OBJ: Dibujar una rueda
    """
    # Rueda
    arcade.draw_circle_filled(x_centro, y_centro, radio, color)
    # Neumático
    arcade.draw_circle_outline(x_centro, y_centro, radio,arcade.color.BLACK, 5)
    # Eje
    arcade.draw_circle_filled(x_centro,y_centro,3,arcade.color.BLACK)
    # Radios
    for radios in range(4):
        arcade.draw_rectangle_filled(x_centro, y_centro, 2, radio*2, arcade.color.BLACK,radios*45)

# Rueda izquierda
dibujar_rueda(480,200,40)
# Rueda derecha
dibujar_rueda(620,200,40)

# Avión de papel
# Forma del avión
arcade.draw_polygon_outline([[370,530],[400,480],[420,500],[430,470],[440,510],[460,520]],arcade.color.WHITE)
# Linea que va al medio de un ala
arcade.draw_polygon_outline([[370,530],[420,500]],arcade.color.WHITE)
# Linea que va al medio de otro ala
arcade.draw_polygon_outline([[370,530],[440,510]],arcade.color.WHITE)
# Linea que va al punto medio de la línea entre los puntos 2 y 3 (Sacado matemáticamente; M=(A+B)/2
arcade.draw_polygon_outline([[430,470],[410,490]],arcade.color.WHITE)


# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()