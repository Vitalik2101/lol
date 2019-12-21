add_library('sound')
pointSize = 12
def setup():
    global x 
    size(900,700)
    background(255)
    noStroke()
    theme = SoundFile(this, "muzlome_Rx_Beats_Trap_Remix_-_Merry_Christmas_Happy_New_Year_67555469.mp3")
    theme.loop()
    x = loadImage("lol.jpg")
    imageMode (CENTER)
    image(x, width/2, height/2)


def draw():
  global pointSize
  for i in range(500):
    loc = int(random(x.width*x.height))

    fill(color(x.pixels[loc]), 100)
    ellipse((loc%x.width),(loc/x.width),pointSize,pointSize)
