from Tkinter import *
initial = 0
finalx = 300
finaly = 300
xdimension = 600
ydimension = 600
checker1 = 0

scrn = curses.initscr()
curses.noecho()
curses.cbreak()
scrn.keypad(1)
scrn.nodelay(1)

root = Tk()

xspacing = 10
yspacing = 10

xlines = xdimension/xspacing
ylines = ydimension/yspacing

frame = Canvas(root, width=600,height=600)
counter = 0
points = []
polypoints = [finalx,finaly]
while counter < xlines:
    x = counter * xspacing
    y = counter * yspacing
    frame.create_line(x,0,x,ydimension,fill = 'light slate grey')
    frame.create_line(0,y,xdimension,y,fill = 'light slate grey')
    counter = counter + 1
pointscountery = 0
pointscounterx = 0
while pointscountery <ylines:
    while pointscounterx <xlines:
        xpoint = pointscounterx * xspacing
        ypoint = pointscountery * yspacing
        points.append(xpoint)
        points.append(ypoint)
        pointscounterx = pointscounterx + 1
    pointscountery = pointscountery + 1
    pointscounterx = 0

def callback(event):    
    global checker1
    if checker1 == 0:
        global finaly
        global finalx
        checker1 = 1
    comparey = finaly
    comparex = finalx
    coordx = event.x
    coordy = event.y
    xchecker = 0
    ychecker = 1
    bestx = 10
    besty = 10
    while xchecker < len(points):
        testx = points[xchecker]
        diffx = abs(points[xchecker] - coordx)
        if diffx < bestx:
            bestx = diffx
            finalx = testx
        xchecker = xchecker + 2
    while ychecker < len(points):
        testy = points[ychecker]
        diffy = abs(points[ychecker] - coordy)
        if diffy < besty:
            besty = diffy
            finaly = testy
            
        ychecker = ychecker + 2
    frame.create_line(comparex,comparey,finalx,finaly)
    polypoints.append(finalx)
    polypoints.append(finaly)
    print polypoints
    comparey = finaly
    comparex = finalx


    
    

frame.bind("<Button-1>", callback)
frame.pack()


root.mainloop()
