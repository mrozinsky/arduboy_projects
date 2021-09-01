from PIL import Image
from os import path


def convert_all_sprites():
    print("Converting all sprites")


def convert_one_row(row_index):
    global im, imWidth, imHeight
    print("Converting one row")


def convert_one_column(column_index):
    global im, imWidth, imHeight
    print("Converting one column")


def convert_one_sprite(x, y):
    x_start = x * sprite_x
    x_end = x_start + spriteWidth
    y_start = y * sprite_y
    y_end = y_start + spriteHeight
    for i in range(x_start, x_end):
        for j in range(0, x_end):
            print("X: " + str(i) + " , Y: " + str(j))
    print("Converting one sprite")


filename = input("Enter the filename of the sprite sheet:\n")

if filename == "": # If the user does not enter anything, the default image will be loaded
    filename = "run_sprite_sheet.bmp"

exists = path.exists(filename)

if exists is True:
    im = Image.open(filename)
    imWidth, imHeight = im.size

    if imHeight % 8 == 0:  # Height check -> height must be a multiple of 8
        spriteWidth = int(input("Enter sprite width:\n"))
        while True: # do while loop
            spriteHeight = int(input("Enter sprite height: (sprite height must be a multiple of 8)\n"))
            if spriteHeight % 8 == 0:
                break

        numberOfColumns = imWidth / spriteWidth
        numberOfRows = imHeight / spriteHeight

        print("\n****************************************")
        print("0 - Convert all sprites in sprite sheet")
        print("1 - Convert one row")
        print("2 - Convert one column")
        print("3 - Convert one sprite")
        conversion_type = input("Select conversion type:")
        print("TEST")

        if str(conversion_type) == "0":
            convert_all_sprites()

        if str(conversion_type) == "1":
            row_index = "Enter row index:"
            convert_one_row(row_index)

        if str(conversion_type) == "2":
            column_index = "Enter column index:"
            convert_one_column(column_index)

        if str(conversion_type) == "3":
            sprite_x = int(input("Enter sprite column index (0.." + str(int(numberOfColumns-1)) + "):"))
            sprite_y = int(input("Enter sprite row index (0.." + str(int(numberOfRows-1)) + "):"))
            convert_one_sprite(sprite_x, sprite_y)

        print("Sprite sheet width: " + str(imWidth))
        print("Sprite sheet height: " + str(imHeight))
        print("Number of rows: " + str(numberOfRows))
        print("Number of columns: " + str(numberOfColumns))
    else:
        print("ERROR: The image height is not a multiple of 8!")
else:
    print("ERROR: The file with the specified name does not exist!")

# nonWhitePixels = []
#
# for i in range(1, imageSizeW):
#     for j in range(1, imageSizeH):
#         pixVal = im.getpixel((i, j))
#         if pixVal != (255, 255, 255):
#             nonWhitePixels.append([i, j])
#
# print(nonWhitePixels)
