def deneme(x_positive,y_positive,x_negative,y_negative,x_y_pos):
    deneme=turtle.Turtle();deneme.color("red");deneme.penup()
    deneme.goto(x_y_pos.pos())
    deneme.forward(abs(x_positive));deneme.left(90);deneme.forward(abs(y_positive)); deneme.pendown()
    deneme.left(90);deneme.forward(abs(x_positive) + abs(x_negative))
    deneme.left(90);deneme.forward(abs(y_positive) + abs(y_negative))
    deneme.left(90);deneme.forward(abs(x_positive) + abs(x_negative))
    deneme.left(90);deneme.forward(abs(y_positive) + abs(y_negative));deneme.hideturtle()