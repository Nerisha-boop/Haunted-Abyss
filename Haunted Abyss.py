import turtle
import random

# Set up the screen
win = turtle.Screen()
win.setup(width=800, height=600)

# Draw the sky
sky = turtle.Turtle()
sky.speed(0)
sky.hideturtle()
sky.penup()
sky.goto(-400, -300)
sky.color("#333333")  # Dark grayish color
sky.begin_fill()
for _ in range(2):
    sky.forward(800)
    sky.right(90)
    sky.forward(600)
    sky.right(90)
sky.end_fill()  # End filling after the loop

# Draw clouds
clouds = turtle.Turtle()
clouds.speed(0)
clouds.hideturtle()
clouds.penup()

for _ in range(10):
    x = random.randint(-350, 350)
    y = random.randint(50, 250)
    clouds.goto(x, y)
    clouds.pendown()
    clouds.color("#CCCCCC")  # Light gray color
    clouds.begin_fill()
    clouds.circle(20)
    clouds.end_fill()

    clouds.penup()
    clouds.goto(x + 20, y + 10)
    clouds.pendown()
    clouds.begin_fill()
    clouds.circle(15)
    clouds.end_fill()

    clouds.penup()
    clouds.goto(x - 20, y + 10)
    clouds.pendown()
    clouds.begin_fill()
    clouds.circle(15)
    clouds.end_fill()

# Draw the stem
stem = turtle.Turtle()
stem.speed(1)
stem.color("green")
stem.penup()
stem.goto(0, -200)
stem.pendown()
stem.width(5)
stem.forward(200)

# Draw thorns
thorn = turtle.Turtle()
thorn.speed(1)
thorn.color("gray")
thorn.penup()
thorn.goto(-10, -150)
thorn.pendown()
thorn.begin_fill()
thorn.forward(20)
thorn.left(120)
thorn.forward(20)
thorn.end_fill()

thorn.penup()
thorn.goto(10, -150)
thorn.pendown()
thorn.begin_fill()
thorn.forward(20)
thorn.left(120)
thorn.forward(20)
thorn.end_fill()

# Draw wilted rose
rose = turtle.Turtle()
rose.speed(1)
rose.color("#8B0A1A")  # Burgundy color
rose.penup()
rose.goto(0, 0)
rose.pendown()

# Draw rose petals
rose.begin_fill()  # Begin fill for the petals
for i in range(2):
    rose.circle(50, 90)  # Draw semi-circle
    rose.left(30)  # Turn left
rose.end_fill()  # End filling the rose petals

# Add some details to rose
rose.penup()
rose.goto(-25, 25)
rose.pendown()
rose.color("black")
rose.begin_fill()
rose.circle(10)  # Draw small circle
rose.end_fill()

# Draw drooping petals
drooping_petal = turtle.Turtle()
drooping_petal.speed(1)
drooping_petal.color("#8B0A1A")  # Burgundy color
drooping_petal.penup()
drooping_petal.goto(-50, -50)
drooping_petal.pendown()
drooping_petal.circle(30, 180)  # Draw semi-circle

drooping_petal.penup()
drooping_petal.goto(50, -50)
drooping_petal.pendown()
drooping_petal.circle(30, 180)  # Draw another semi-circle

# Draw rose's center
center = turtle.Turtle()  # Correct instantiation of turtle
center.speed(1)
center.color("black")  # Set drawing color to black
center.penup()  # Correct method call
center.goto(0, 30)
center.pendown()
center.begin_fill()
center.circle(20)  # Draw a small circle
center.end_fill()

# Draw rose's texture
texture = turtle.Turtle()  # Create a turtle instance for the texture
texture.speed(1)  # Set drawing speed
texture.color("#8B0A1A")  # Set drawing color to burgundy
texture.penup()  # Lift the pen
texture.goto(-40, 40)  # Move to the starting position
texture.pendown()  # Start drawing
texture.width(2)  # Set line width
texture.forward(80)  # Draw a line

# Finish up
texture.hideturtle()  # Hide the texture turtle after drawing

# Keep the window open until closed by the user
win.mainloop()