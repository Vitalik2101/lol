
def setup():
    size(500, 500)
    smooth()
    background(50)
    strokeWeight(2)
    noLoop()

cx = 250
cy = 250
cRadius = 200

def draw():
    i = 2*PI
    k = 0
    global cx, cy, cRadius
    while i > 0:
        i = i - 2*PI/250
        k += 1
        stroke(k)
        x1 = cos(i+PI/2)*cRadius + cx
        y1 = sin(i+PI/2)*cRadius + cy
        line(cx , cy , x1 , y1)
        
        line(cx , cy , cx , cy)
        

def keyPressed():
    if key== "s": saveFrame(" myProcessing .png")
    
