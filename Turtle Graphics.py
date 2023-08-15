import turtle

# Set up the screen
window = turtle.Screen()
window.title("Turtle Graphics Example")
window.bgcolor("white")

# Create a turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")

# Draw a square
for _ in range(4):
    my_turtle.forward(100)  # Move forward by 100 units
    my_turtle.right(90)     # Turn right by 90 degrees

# Draw a circle
my_turtle.color("red")
my_turtle.circle(50)  # Draw a circle with radius 50 units

# Draw a triangle
my_turtle.color("green")
for _ in range(3):
    my_turtle.forward(150)
    my_turtle.left(120)

# Close the window on click
window.exitonclick()
