import tkinter
c = tkinter.Canvas(width = 1000, height = 1000)

def my_triangle(x1, y1, x2, y2, x3, y3, l):
	if l == 1:
		canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill = "blue")
	my_triangle(x1, y1, (x1 + x2)/2, (y1 + y2)/2, (x1 + x3)/2, (y1 + y3)/2, l - 1)
	my_triangle((x1 + x2)/2, (y1 + y2)/2, x2, y2, (x2 + x3)/2, (y2 + y3)/2, l - 1)
	my_triangle((x1 + x3)/2, (y1 + y3)/2,(x2 + x3)/2, (y2 + y3)/2, x3, y3, l - 1)
x1 = 0
y1 = 875
x2 = 500
y2 = 0
x3 = 1000
y3 = 875
l = int(input())
c.pack()
my_triangle(x1, y1, x2, y2, x3, y3, l)
c.mainloop()
