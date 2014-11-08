import tkinter
import sys
import random
import math
import par
WIDTH=900
HEIGHT=1000
w,h=WIDTH,HEIGHT/2
FPS = 100
g=0.8
G=0
ko=15
n=1
HOLE_FILL='black'
FIELD_COLOR='lime green'
BORDER_COLOR='dark green'
class Ball:
    def __init__(self,x,y,vx,vy,m,R,fill):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.m=m
        self.fill=fill
        self.R=R
class spring:
    def __init__(self,l,k,B1,B2):
                self.l=l
                self.k=k
                self.B1=B1
                self.B2=B2    
class rope:
    def __init__(self,l,B1,B2):
            self.l=l
            self.B1=B1
            self.B2=B2
class spoke:
    def __init__(self,x1,y1,x2,y2,Balls):
                self.x1=x1
                self.y1=y1
                self.x2=x2
                self.y2=y2
                self.Balls=Balls
def mod(a,mod):
    k=a-int(a/mod)*a
    if k<0:
        k+=mod
    return k
def draw_field(canvas,game):
    canvas.delete(*canvas.find_all())
    canvas.create_rectangle(0,0,WIDTH, HEIGHT, fill=BORDER_COLOR)
    canvas.create_rectangle(5,5,WIDTH-5, HEIGHT-5, fill=FIELD_COLOR)
    for i in game:
        canvas.create_oval(i.x-i.R,i.y-i.R,i.x+i.R,i.y+i.R, fill=i.fill)
    for i in Spring:
        canvas.create_line(i.B1.x,i.B1.y,i.B2.x,i.B2.y,width=3,fill='dim gray')
    for i in Rope:
        if distance(i.B1.x,i.B1.y,i.B2.x,i.B2.y)>=i.l:
            canvas.create_line(i.B1.x,i.B1.y,i.B2.x,i.B2.y)
        else:
            if i.B2.x>i.B1.x:
                par.draw_rope(i.B1.x,i.B1.y,i.B2.x,i.B2.y, i.l,canvas)
            if  i.B1.x>i.B2.x:
                par.draw_rope(i.B2.x,i.B2.y,i.B1.x,i.B1.y, i.l,canvas)
    for i in Spoke:
        canvas.create_line(i.x1,i.y1,i.x2,i.y2, width=1)
def change(v0,m0,v1,m1):
    u0=(2*m1*v1+v0*(m0-m1))/(m0+m1)
    u1=(2*m0*v0+v1*(m1-m0))/(m0+m1)
    return(u0,u1)
def change2(vx,vy,ux,uy,cos,sin,m1,m2):
    ix=-(vy*cos-vx*sin)*sin+change(vy*sin+vx*cos,m1,uy*sin+ux*cos,m2)[0]*cos
    iy=(vy*cos-vx*sin)*cos+change(vy*sin+vx*cos,m1,uy*sin+ux*cos,m2)[0]*sin
    jx=-(uy*cos-ux*sin)*sin+change(vy*sin+vx*cos,m1,uy*sin+ux*cos,m2)[1]*cos
    jy=(uy*cos-ux*sin)*cos+change(vy*sin+vx*cos,m1,uy*sin+ux*cos,m2)[1]*sin
    return(ix,iy,jx,jy)  
def distance (x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
def  S(a,b,c):
    p=(a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5
def distancel(x1,y1,x2,y2,x,y):
    return S( ((x-x1)**2+(y-y1)**2)**0.5,((x2-x1)**2+(y2-y1)**2)**0.5,((x-x2)**2+(y-y2)**2)**0.5)/((x2-x1)**2+(y2-y1)**2)**0.5
def popp(A,k):
    for i in range(0,len(A)):
        if A[i]==k:
            A.pop(i)
            return A

def make_move(game):
    global Game
    global k
    global G
    global n
    global Tet
    n+=1
    a=random.random()-0.5
    b=random.random()-0.5
    for i in Game:
        i.vy+=g/ko
    for i in Rope:       
        while distance(i.B1.x+i.B1.vx,i.B1.y+i.B1.vy,i.B2.x+i.B2.vx,i.B2.y+i.B2.vy)>i.l:
            cos=(i.B2.x-i.B1.x)/distance(i.B1.x,i.B1.y,i.B2.x,i.B2.y)
            sin=(i.B2.y-i.B1.y)/distance(i.B1.x,i.B1.y,i.B2.x,i.B2.y)
            T=distance(i.B1.x+i.B1.vx,i.B1.y+i.B1.vy,i.B2.x+i.B2.vx,i.B2.y+i.B2.vy)/50
            i.B1.vx+=T*cos/i.B1.m/ko
            i.B1.vy+=T*sin/i.B1.m/ko
            i.B2.vx-=T*cos/i.B2.m/ko
            i.B2.vy-=T*sin/i.B2.m/ko        
    for i in game:
        if not i.R<i.x+i.vx<WIDTH-i.R:
            pass
            #i.x=mod(i.x,w)
            i.vx*=-1
        if not i.R<i.y+i.vy<HEIGHT-i.R:
            pass
            i.vy*=-1
            #i.y=mod(i.y,h)
    #print(distance(A.x,A.y,B.x,B.y))
    for i in Spring:
        T=(distance(i.B1.x,i.B1.y,i.B2.x,i.B2.y)-i.l)*i.k
        cos=(i.B2.x-i.B1.x)/distance(i.B1.x,i.B1.y,i.B2.x,i.B2.y)
        sin=(i.B2.y-i.B1.y)/distance(i.B1.x,i.B1.y,i.B2.x,i.B2.y)
        i.B1.vx+=T*cos/i.B1.m/ko
        i.B1.vy+=T*sin/i.B1.m/ko
        i.B2.vx-=T*cos/i.B2.m/ko
        i.B2.vy-=T*sin/i.B2.m/ko      
    for i in game:
        for j in game:
                if distance(i.x+i.vx,i.y+i.vy,j.x+j.vx,j.y+j.vy)<=(i.R+j.R) and i!=j:
                    k=distance(i.x,i.y,j.x,j.y)
                    change=change2(i.vx,i.vy,j.vx,j.vy,(j.x-i.x)/k,(j.y-i.y)/k,i.m,j.m)
                    i.vx,i.vy,j.vx,j.vy=change[0],change[1],change[2],change[3]                 
    for i in Spoke:
        for j in i.Balls:
            if (i.x1<j.x<i.x2 or i.x2<j.x<i.x1):
                cos=(i.x2-i.x1)/distance(i.x1,i.y1,i.x2,i.y2)
                sin=(i.y2-i.y1)/distance(i.x1,i.y1,i.x2,i.y2)
                ux=j.vx*cos*cos+j.vy*sin*cos
                uy=j.vy*sin*sin+j.vx*cos*sin
                j.vx,j.vy=ux,uy
            else:
                i.Balls=popp(i.Balls,j)
    for i in Game:
        for j in Game:
            if i!=j:
                d=distance(i.x,i.y,j.x,j.y)
                cos=(j.x-i.x)/d
                sin=(i.y-j.y)/d
                F=G*i.m*j.m/d**2/2
                if F>5:
                    F=5
                i.vx+=F*cos/i.m/ko
                i.vy-=F*sin/i.m/ko
                j.vx-=F*cos/j.m/ko
                j.vy+=F*sin/j.m/ko
    for i in game:
        i.x+=i.vx/ko
        i.y+=i.vy/ko
    #print(Game[0].x)
    E=sum([(i.vx**2+i.vy**2)*i.m/2+i.m*g*(HEIGHT-i.y) for i in Game])
    #print(E)
if __name__ == "__main__":
    c = tkinter.Canvas(width=WIDTH, height=HEIGHT)
    c.pack()
    c.focus_set()
def loop():
    global Game
    draw_field(c, Game)
    for i in range(ko):
        pass
        make_move(Game)
    c.after(1000// FPS, loop)
A=Ball(200,200,             0,0,1,20,'orange')
B=Ball(400,h/3,               1,0,1,20,'white')
C=Ball(w-200,200,                 -1/6,7,1,20,'red')
D=Ball(w/2,h/4,                 0,0,5,20,'orange')
E=Ball(w/2-70,h/2+50,                 0,3,3,20,'black')
F=Ball(w/2,h/2,                 -5,-6,2,6,'yellow')
I=Ball(w/2,h/2-200,                 5/2**0.5,0,1,6,'red')
H=Ball(w/2,h/2,                 -3/10,0,100,60,'yellow')
J=Ball(w/2,h/2,                 30,0,1,6,'blue')
Rope1=rope(distance(A.x,A.y,B.x,B.y),A,B)
Rope2=rope(200,D,C)
Rope3=rope(200*2**0.5/2,B,D)
Rope4=rope(distance(A.x,A.y,C.x,C.y),A,C)
Rope5=rope(distance(A.x,A.y,D.x,D.y),A,D)
Rope6=rope(distance(C.x,C.y,B.x,B.y),B,C)
Spoke1=spoke(100,300,300,100,[A])
Spoke2=spoke(w-100,300,w-300,100,[C])
Spoke3=spoke(300,h/2,850,h/2,[A,C])
Spoke4=spoke(h-100,300,h-300,100,[C])
Spring1=spring(200,1/10,A,B)
Spoke=[Spoke1,Spoke2]
Spring=[]
Rope=[Rope1,Rope6]
Game = [A,B,C]
loop()
c.mainloop()
