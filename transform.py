from PIL import Image
import sys

# Global constants
ASCII_CHARS = ['.',',',':',';','+','*','?','%','S','#','@']
ASCII_CHARS = ASCII_CHARS[::-1]
newWidth = 100
intensity = 25

def resizeImage(image):
    (origWidth, origHeight) = image.size
    aspect_ratio = float(origHeight) / float(origWidth)
    newHeight = int(aspect_ratio * newWidth)
    dimension = (newWidth, newHeight)
    newImage = image.resize(dimension)
    return newImage

def replacePixel(image):
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value // intensity] for pixel_value in initial_pixels]
    return ''.join(new_pixels)

def transform(image):
    image = resizeImage(image)
    image = image.convert('L')
    pixels = replacePixel(image)
    pixelsNum = len(pixels)
    newImage = [pixels[index:index+newWidth] for index in range(0, pixelsNum, newWidth)]
    return '\n'.join(newImage)

if __name__ == "__main__":
    filename = sys.argv[1]
    img = Image.open(filename)
    image = transform(img)
    f = open('output.txt','w')
    f.write(image)
    f.close()
