import image
import sys

# Set the timeout to a larger number if timeout is occuring.
sys.getExecutionLimit(30000)

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for i in range(0, img.getWidth()):
    for j in range(0, img.getHeight()):
        old_p = img.getPixel(i, j)
        # TODO: Complete the inner part of this loop to blur the image.
        # new_p = image.Pixel(255, old_p.getBlue(), old_p.getGreen())
        # newimg.setPixel(i, j, new_p)

newimg.draw(win)
win.exitonclick()


