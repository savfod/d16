import turtle

def draw_levi(length,d):
	if d==0:
		turtle.forward(length)
	else:
		draw_levi(length/4,d-1)
		turtle.left(90)
		draw_levi(length/4,d-1)
		turtle.right(90)
		draw_levi(length/4,d-1)
		turtle.right(90)
		draw_levi(length/2,d-1)
		turtle.left(90)
		draw_levi(length/4,d-1)
		turtle.left(90)
		draw_levi(length/4,d-1)
		turtle.right(90)
		draw_levi(length/4,d-1)
length1=int(input())
d1=int(input())
turtle.speed('fastest')
draw_levi(length1, d1)
input()
