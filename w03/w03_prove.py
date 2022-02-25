# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    canvas = start_drawing("Grid", scene_width, scene_height)
    
    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    #draw_grid(canvas, scene_width, scene_height, 50)
  
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)

# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")
    draw_cloud(canvas, scene_width, scene_height)



######################################################################################################
def draw_cloud(canvas, scene_width, scene_height):
    
    half_height = round(scene_height * 3)
    min_diam = 30
    max_diam = 100

    # Draw 30 ovals, each with
    # a random location and diameter.
    for i in range(15):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(200, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + (diameter + 90), y + diameter,
                outline="azure3", fill="azure3")

    for i in range(15):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(200, half_height)
        diameter = random.randint (min_diam, max_diam)
        draw_oval(canvas, x, y, x + (diameter + 100), y + diameter,
                outline="azure2", fill="azure2")
    
    
######################################################################################################

def draw_ground(canvas, scene_width, scene_height):
    
    #barn location specs
    barn_center_x = 550
    barn_bottom = 90
    barn_height = 500
    
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan3")

    draw_grass(canvas, scene_height, scene_width, 10)

    draw_barn(canvas, barn_center_x, barn_bottom, barn_height)
    
    
    
    
    

def draw_barn(canvas, barn_center_x, barn_bottom, barn_height):
    
    #main body of the barn specs
    barn_width = barn_height / 2
    barn_height = barn_height / 2
    barn_left = barn_center_x - barn_width / 2
    barn_right = barn_center_x + barn_width / 2
    barn_top = barn_bottom + barn_height

    #roof of barn specs
    height = 400
    skirt_width = barn_height / 1.8
    skirt_height = (height - 350) - (barn_height - 200)
    skirt_left = barn_center_x - skirt_width * 1.2
    skirt_right = barn_center_x + skirt_width * 1.2
    skirt_top = barn_bottom + height
    
    #barn door specs
    
    door_center_x = 450
    door_bottom = 95
    door_width = 525
    door_height = 275
    

    #barn window specs
    window_center_x = 640
    window_bottom = 200
    window_width = 575
    window_height = 285


   
    #barn body
    draw_rectangle(canvas, barn_left, barn_top, barn_right, barn_bottom, outline="gray20", width=1, fill="indianred2")
    #roof
    draw_polygon (canvas, barn_center_x, skirt_top,
        skirt_right, (barn_top - 50), skirt_left, barn_top, outline="gray20", width=2, fill="gray65")
    #door
    draw_rectangle(canvas, door_center_x, door_bottom, door_width, door_height,
        outline="gray20", width=1, fill="burlywood4")
    #window
    draw_rectangle(canvas, window_center_x, window_bottom, window_width, window_height,
        outline="gray20", width=1, fill="honeydew")

    #little barn body
    draw_rectangle(canvas, barn_left / 3, barn_top /3, barn_right / 3, barn_bottom / 3, outline="gray20", width=1, fill="plum")
    #little roof
    draw_polygon (canvas, barn_center_x / 3, skirt_top / 3,
        skirt_right / 3, (barn_top - 50) / 3, skirt_left / 3, barn_top / 3, outline="gray20", width=2, fill="gray65")
    #little door
    draw_rectangle(canvas, door_center_x / 3, door_bottom / 3, door_width / 3, door_height / 3,
        outline="gray20", width=1, fill="burlywood4")

    #little window
    draw_rectangle(canvas, (window_center_x / 3), (window_bottom / 3), (window_width / 3), (window_height / 3),
        outline="gray20", width=1, fill="honeydew")



min_width = 2
max_width = 10
min_height = 15
max_height = 30

def draw_grass(canvas, height, width, interval):
    y = 0
    increase = 0
    while (increase <= 170):
        y = y + increase
        increase = increase + 15
    
        for i in range(250):
            x = random.randint(interval, width)
            grass_width = random.randint(min_width, max_width)
            grass_height = random.randint(min_height, max_height + increase)
            draw_line(canvas, x, increase, x + grass_width, grass_height, fill="springGreen1")

        for i in range(250):
            x = random.randint(interval, width)
            y = random.randint(interval, height)
            grass_width = random.randint(min_width, max_width)
            grass_height = random.randint(min_height, max_height+ increase)
            draw_line(canvas, x, increase, x + grass_width, grass_height, fill="springGreen4")

    

    

         




# Call the main function so that
# this program will start executing.
main()