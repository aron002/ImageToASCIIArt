import PIL
import requests
from PIL import Image
from io import BytesIO

LARGE_SCALE = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '

SMALL_SCALE = ' .:-=+*#%@'[::-1]

SCALE = LARGE_SCALE

def image_to_text(image_to_transform, image_type):
    if image_type == '1':
        image_to_convert = Image.open(image_to_transform)
    elif image_type == '2':
        response = requests.get(image_to_transform)
        image_to_transform = response.content
        image_to_convert = Image.open(BytesIO(image_to_transform))
    else:
        return
    image = image_to_convert.convert('L')
    text = ''
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.getpixel((x,y))
            key = SCALE[round(pixel/(255/(len(SCALE)-1)))]
            text += key
        text += '\n'
    return text

if __name__ == '__main__':
    print('1: Path')
    print('2: Link')
    while (image_type := input()) not in ['1','2']:
        pass
    npt = input(['Path', 'Link'][int(image_type)-1] + ': ')
    try:
        picture = image_to_text(npt, image_type)
    except:
        picture = 'Could not find the image :( \nTry adding .jpg or .png'
        
    file = open('image.txt', 'w')
    file.write(picture)
    file.close()

            
                
    
    
                
            
            
            
            
