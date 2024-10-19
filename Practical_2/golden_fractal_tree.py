import turtle
import math

# Calculate the bounding box of the fractal tree
def calculate_bounding_box(x, y, direction, length):
    x_min = x_max = x
    y_min = y_max = y
    
    stack = [(x, y, direction, length)]
    
    while stack:
        x, y, direction, length = stack.pop()
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)
        
        if length >= 3:
            cx, cy = x + math.cos(math.radians(direction)) * length, y + math.sin(math.radians(direction)) * length
            stack.append((cx, cy, direction + 72, (2 - golden_ratio) * length))
            stack.append((cx, cy, direction - 72, (2 - golden_ratio) * length))
            stack.append((cx, cy, direction, (golden_ratio - 1) * length))
    
    return x_min, x_max, y_min, y_max

# Adjust the screen size based on the bounding box dimensions
def adjust_screen_size(x_min, x_max, y_min, y_max):
    screen_width = max(x_max - x_min, y_max - y_min) * 1.1
    screen_height = screen_width * 1.1
    screen.setup(screen_width, screen_height)

screen = turtle.Screen()
screen.title('Golden Fractal Tree - PythonTurtle.Academy')
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0,0)
golden_ratio = (1 + 5 ** 0.5) / 2

# Draw the golden fractal tree
def golden_fractal_tree(x, y, direction, length):
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(direction)
    turtle.down()
    turtle.pensize(math.log(length, 2) / 3)
    if length < 10:
        turtle.color('forest green')
    else:
        turtle.color('gray')
    turtle.fd(length)
    if length < 3:
        return
    cx, cy = turtle.xcor(), turtle.ycor()
    golden_fractal_tree(cx, cy, direction + 72, (2 - golden_ratio) * length)
    golden_fractal_tree(cx, cy, direction - 72, (2 - golden_ratio) * length)
    golden_fractal_tree(cx, cy, direction, (golden_ratio - 1) * length)

# Draw the fractal tree and adjust screen size
golden_fractal_tree(0, -400, 90, 300)
x_min, x_max, y_min, y_max = calculate_bounding_box(0, -400, 90, 300)
adjust_screen_size(x_min, x_max, y_min, y_max)
turtle.update()

# Prevent the window from closing automatically
screen.mainloop()
