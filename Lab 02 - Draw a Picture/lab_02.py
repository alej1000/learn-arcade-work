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


# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()