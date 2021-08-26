from PIL import Image
import os.path
from os import path

def convertAllSprites():
    print(imWidth)
    #global im, imWidth, imHeight
    print("Converting all sprites")

def convertOneRow():
    global im, imWidth, imHeight
    print("Converting one row")

def convertOneColumn():
    global im, imWidth, imHeight
    print("Converting one column")

def convertOneSprite():
    global im, imWidth, imHeight
    print("Converting one sprite")


filename = input("Enter the filename of the sprite sheet:\n")

if filename == "": # If the user does not enter anything, the default image will be loaded
    filename = "run_sprite_sheet.bmp"

exists = path.exists(filename)

if exists == True:
    im = Image.open(filename)
    imWidth, imHeight = im.size

    if imHeight % 8 == 0: # Height check -> height must be a multiple of 8
        spriteWidth = int(input("Enter sprite width:\n"))
        while True: # do while loop
            spriteHeight = int(input("Enter sprite height: (sprite height must be a multiple of 8)\n"))
            if spriteHeight % 8 == 0:
                break

        print("\n****************************************")
        print("0 - Convert all sprites in sprite sheet")
        print("1 - Convert one row")
        print("2 - Convert one column")
        print("3 - Convert one sprite")
        conversion_type = input("Select conversion type:")
        if isinstance(conversion_type, int):
            if conversion_type == 0:
                convertAllSprites()


        numberOfRows = imWidth / spriteWidth
        numberOfColumns = imHeight / spriteHeight

        print("Sprite sheet width: " + str(imWidth))
        print("Sprite sheet height: " + str(imHeight))
        print("Number of rows: " + str(numberOfRows))
        print("Number of columns: " + str(numberOfColumns))
    else:
        print("ERROR: The image height is not a multiple of 8!")
else:
    print("ERROR: The file with the specified name does not exist!")

#nonWhitePixels = []
#
#for i in range(1, imageSizeW):
#    for j in range(1, imageSizeH):
#        pixVal = im.getpixel((i, j))
#        if pixVal != (255, 255, 255):
#            nonWhitePixels.append([i, j])
#
#print(nonWhitePixels)
