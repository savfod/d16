
import turtle
turtle.speed("fastest")


def draw_levi(length, d):
    if d == 0:
        turtle.forward(length)
    else:
        draw_levi(length/2 , d-1)
        turtle.left(90)
        draw_levi(length/2 , d-1)
        turtle.left(90)
        draw_levi(length/2 , d-1)
        turtle.right(135)
        draw_levi(length , d-1)
        turtle.left(135)
        draw_levi(length/2 , d-1)
        turtle.right(135)
        draw_levi(length , d-1)
        turtle.left(135)
        draw_levi(length/2 , d-1)
        turtle.right(135)
        draw_levi(length , d-1)
        turtle.right(90)
        draw_levi(length , d-1)
        turtle.right(135)
        draw_levi(length/2 , d-1)
        turtle.left(135)
        draw_levi(length , d-1)
        turtle.right(135)
        draw_levi(length/2 , d-1)
        turtle.left(135)
        
        draw_levi(length , d-1)
        turtle.right(135)
        draw_levi(length/2 , d-1)
        turtle.left(90)
        draw_levi(length/2 , d-1)
        turtle.left(90)
        draw_levi(length/2 , d-1)
        draw_levi(length, d-1)
        


draw_levi(200, 4)
input()
