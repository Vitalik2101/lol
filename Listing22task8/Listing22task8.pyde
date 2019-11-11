def setup() :
 size(500, 500)
 smooth()
 background(255)
 noStroke()
 noLoop()
 

def draw() :  
  for  i in range (0,10):
      for c in range (0,5):
       fill(i*20)
       rect(i*40+50,(2*c-1)*40+75, 35, 35)
       fill(180-i*20)
       rect(i*40+50,2*c*40+75,35,35)
