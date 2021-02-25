# Import the "arcade" library
import arcade

# Open up a window.
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

# Dibuja el césped
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

# Dibuja una nube
arcade.draw_circle_filled(650,450,20,arcade.color.WHITE)
arcade.draw_circle_filled(670,470,20,arcade.color.WHITE)
arcade.draw_circle_filled(630,430,20,arcade.color.WHITE)


arcade.draw_circle_filled(670,450,20,arcade.color.WHITE)
arcade.draw_circle_filled(630,450,20,arcade.color.WHITE)

arcade.draw_circle_filled(610,510,20,arcade.color.WHITE)
arcade.draw_circle_filled(590,510,20,arcade.color.WHITE)
arcade.draw_circle_filled(570,510,20,arcade.color.WHITE)

arcade.draw_circle_filled(610,510,20,arcade.color.WHITE)
arcade.draw_circle_filled(590,490,20,arcade.color.WHITE)
arcade.draw_circle_filled(570,470,20,arcade.color.WHITE)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()