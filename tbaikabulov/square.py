import tkinter
WIDTH=1200
HEIGHT=1200
c = tkinter.Canvas(width=WIDTH-2, height=HEIGHT-2)
def square(n,x1,y1,R,fill):
    if n==0:
        c.create_rectangle(x1-R,y1-R,x1+R,y1+R,fill=fill)
    else:
        square(n-1,x1-R/2,y1-R/2,R/3,fill)
        square(n-1,x1-R/2,y1,R/3,fill)
        square(n-1,x1-R/2,y1+R/2,R/3,fill)
        square(n-1,x1,y1-R/2,R/3,fill)
        square(n-1,x1,y1+R/2,R/3,fill)
        square(n-1,x1+R/2,y1-R/2,R/3,fill)
        square(n-1,x1+R/2,y1,R/3,fill)
        square(n-1,x1+R/2,y1+R/2,R/3,fill)
square(5,WIDTH/2,HEIGHT/2,243*3,'black')  
c.pack()
c.focus_set()
c.mainloop()
