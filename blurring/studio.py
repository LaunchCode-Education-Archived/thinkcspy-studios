import image
import sys
import random

# You can increase this to buy yourself some time, if you're getting a "timeout error"
sys.setExecutionLimit(30000)

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for i in range(1, img.getWidth() - 1):
    for j in range(1, img.getHeight() - 1):
        # pick a random neighbor
        nx = random.randint(i-1, i+1)
        ny = random.randint(j-1, j+1)
        
        # set this pixel to neighbor's color
        neighbor_color = img.getPixel(nx, ny)
        newimg.setPixel(i,j, neighbor_color)
        

newimg.draw(win)
win.exitonclick()



