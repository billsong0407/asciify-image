from PIL import Image

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

def run(path):
    image = None
    image = transform(path)
    print(image)
    f = open('img.txt','w')
    f.write(image)
    f.close()

if __name__ == "__main__":
    pass
    img = Image.open("person.jpg")
    image = transform(img)
    print(image)
    f = open('img.txt','w')
    f.write(image)
    f.close()
