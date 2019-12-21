from PIL import ImageGrab, Image
import pytesseract

game_coords = [56, 315, 426, 655]

def grabImage():
    #Grab a screenshot of gameboard

    im = ImageGrab.grab(bbox=game_coords)
    im.save("gameboard.png")

    return im



def imageProcess():

    def createLine(row):

        # Used to combine a row into a single image, easier for pytessaract to read

        def get_concat_h(im1, im2):
            dst = Image.new('RGB', (im1.width + im2.width, im1.height))
            dst.paste(im1, (0, 0))
            dst.paste(im2, (im1.width, 0))
            return dst

        line = row[0]

        for j in range(1, 7):
            line = get_concat_h(line, row[j])

        return line

    im = Image.open("gameboard.png")

    # First letter frame is [3, 75, 45, 117]

    # Used to store board's letters and colored tile locations

    foundLetters = []

    for i in range(5):
        row = []
        for j in range(7):
            # Automates creating letters and sends them to createLine
            frame = [9 + (53 * j), 81 + (53 * i),
                     39 + (53 * j), 111 + (53 * i)]
            letterI = im.crop(box=frame).resize((60,80))

            row.append(letterI)

            # Used to save letter images, TODO deprecate soon or create class to toggle necessity
            #fileLoc = "images/letter_" + str(i + 1) + "_" + str(j + 1) + ".png"
            #letterI.save(fileLoc)

        line = createLine(row)

        # Pytesseract to create text
        foundLetters.append(pytesseract.image_to_string(line))

        # Save line for good measure
        line.save("images/line" + str(i + 1) + ".png")

        # Close all images in row
        for image in row:
            image.close()

        line.close()

    l = cleanLetters(foundLetters)

    im.close()
    return l

def cleanLetters(letters):

    n = len(letters)

    for i in range(n):
        word = letters[i].replace(" ", "")

        if len(word) != 7:
            if ("Qu" in word) or ("QU" in word):
                word = word.replace("QU", "Q")
                word = word.replace("Qu", "Q")

        letters[i] = word

    return letters

def tryClean(rowNum):
    n = rowNum + 1

    line = Image.open("images/line" + str(n) + ".png").convert("L")

    line.resize((line.width * 2, line.height * 2))
    line.save("images/line" + str(n) + ".png")
    letters = [pytesseract.image_to_string(line)]

    return cleanLetters(letters)

    line.close()