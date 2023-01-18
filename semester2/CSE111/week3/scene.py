# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_grid(canvas, scene_width,scene_height,50)
    draw_sky(canvas, scene_width,scene_height)
    draw_cloud(canvas,scene_width,scene_height)
    draw_ground(canvas,scene_width,scene_height)
    draw_bird(canvas,scene_width,scene_height)
    draw_sun(canvas,scene_width,scene_height)
    draw_water_wells(canvas,scene_width,scene_height)
    
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.

def draw_bird(canvas,scene_width, scene_height):
    #first bird
    draw_arc(canvas,scene_width-690,scene_height-200,scene_width-650,scene_height-180, start=0,extent=180,width=1.4)
    draw_arc(canvas,scene_width-650,scene_height-200,scene_width-610,scene_height-180, start=0,extent=180,width=1.4)

    #second bird
    draw_arc(canvas,scene_width-580,scene_height-200,scene_width-565,scene_height-190, start=0,extent=180)
    draw_arc(canvas,scene_width-565,scene_height-200,scene_width-550,scene_height-190, start=0,extent=180)

    #third bird
    draw_arc(canvas,scene_width-750,scene_height-200,scene_width-735,scene_height-190, start=0,extent=180)
    draw_arc(canvas,scene_width-735,scene_height-200,scene_width-720,scene_height-190, start=0,extent=180)


def draw_grid(canvas,scene_width, scene_height,interval):
    #draw vertical lines
    label_y=15
    for x in range(0,scene_width,interval):
        draw_line(canvas,x,0,x,scene_height)
        draw_text(canvas,x,label_y,f"{x}")


    #draw horizontal lines
    label_x=15
    for y in range(interval,scene_height,interval):
        draw_line(canvas,0,y,scene_width,y)
        draw_text(canvas,label_x,y,f"{y}")



def draw_sun(canvas,scene_width,scene_height):
    draw_oval(canvas,scene_width-50,scene_height-30,scene_width-150,scene_height-130,width=0, fill="goldenrod1" )   


def draw_water_wells(canvas,scene_width,scene_height):
    draw_rectangle(canvas,scene_width-450,scene_height-400,scene_width-300,scene_height-440,width=0, fill="tan4")
    draw_oval(canvas,scene_width-450,scene_height-390,scene_width-300,scene_height-410,width=0, fill="lightBlue" ) 
    

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="sky blue")



def draw_cloud(canvas,scene_width,scene_height):

    draw_oval(canvas,scene_width-750,scene_height-30,scene_width-550,scene_height-130,width=0, fill="white" )
    draw_oval(canvas,scene_width-740,scene_height-25,scene_width-670,scene_height-125,width=0, fill="white" )
    draw_oval(canvas,scene_width-710,scene_height-10,scene_width-600,scene_height-150,width=0, fill="white" )
    draw_oval(canvas,scene_width-650,scene_height-10,scene_width-570,scene_height-150,width=0, fill="white" )

   
def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,scene_width, scene_height / 3, width=0, fill="green4")

    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,tree_bottom, tree_height)


    # Draw second pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,tree_bottom, tree_height)

    # Draw third pine tree.
    tree_center_x = 250
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,tree_bottom, tree_height)

def draw_pine_tree(canvas, center_x, bottom, height):

    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """

    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,trunk_left, trunk_top, trunk_right, bottom,outline="tan4", width=0.5, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=0.5, fill="dark green")





 


# Call the main function so that
# this program will start executing.
main()