x=0
y=00
def setup():
    size(900,900)
def draw():
    global x, y
    background(255)
    fill(0)
    ellipse(y,x,200,300)
    x=x+10
    y=y+10

    if x==900:
        x=0
    if y==900:
        y=0
    
    
    
    
