from PIL import Image, ImageEnhance, ImageFilter
import os
import sys

try:
	#This opens an image
    chairs = Image.open("chairs.jpg")
    stores = Image.open("stores.jpg")
    output = "newImage.png"
    
    #This brightens up the photo and shows it in a new window
    enh = ImageEnhance.Contrast(chairs)
    enh.enhance(0.8).show("20% more contrast")

    #makes chair image black and white
    chairs.convert(mode = 'L').save('B&W.jpg')


    #Blurs picture (look at text in blur.jpg)
    stores.filter(ImageFilter.GaussianBlur(radius = 2)).save('blur.jpg')

    #This will save the photo as a new filename
    chairs.save(output)

except IOError:
    print("Unable to load image")
    sys.exit(1)

for files in os.listdir('.'):
	#This converts a file image to a png from jpg
	if files.endswith('.jpg'):
		images = Image.open(files)
		fname, fext = os.path.splitext(files)
		images.save('filesFromPillows/{}.png'.format(fname))
		sizeHalf = (300,300)

#This opens the picture in a blank window    
chairs.show()