#python code that draws the symbol of love using the turtle module

#imports turtle module
import turtle




#define function draw_love_symbol

def draw_love_symbol():

    turtle.speed(10)

    turtle.penup()

    turtle.goto(0, -100)

    turtle.pendown()


    # set color fill to red

    turtle.fillcolor("red")



    # Draw the heart shape

    # fills the love symbol shape with color red

    turtle.begin_fill()


    

    

    turtle.left(140)

    turtle.forward(224)

    turtle.circle(-112, 200)

    turtle.setheading(60)

    turtle.circle(-112, 200)

    turtle.forward(224)

    turtle.end_fill()


    # exits the turtle IDE once clicked on

    turtle.exitonclick()


#calls the draw_love_symbol

draw_love_symbol()