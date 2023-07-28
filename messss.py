import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a square
for _ in range(4):
    t.forward(100)
    t.left(90)

# Keep the window open until closed manually
turtle.done()