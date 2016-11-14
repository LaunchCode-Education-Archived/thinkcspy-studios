import image

img = image.Image("luther.jpg")
win = imge.ImageWin()

# You can increase this to buy yourself some time, if you're getting a "timeout error"
sys.setExecutionLimit(30000)

for x in range(img.getWidth()):
    for y in range(img.getHeight()):
        p = img.getPixel(x, y)
        red = p.getRed()
        green = p.getGreen()
        blue = p.getBlue()
        new_p = image.Pixel(255, green, blue)
        img.setPixel(x, y, new_p)
        
img.draw(win)
win.exitonclick()
    
