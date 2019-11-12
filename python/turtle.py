import turtle

my_turtle=turtle.Turtle()
my_turtle.speed(10)
def square():
    
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.color('red')

    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    
for i in range(100):
    square()
    my_turtle.right(100)
    my_turtle.circle(5)
    
    














