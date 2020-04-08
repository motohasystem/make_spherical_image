from PIL import Image, ImageDraw
import sys

def make_spherical(filename):
    img = Image.open(filename)
    width, height = img.size

    new_height = int(width / 2)
    result = Image.new('RGBA', (width, new_height), (0, 0, 0))
    result.paste(img, (0, new_height - height))
    
    blur = Image.new('RGBA', result.size)
    
    draw = ImageDraw.Draw(blur)
    bottom = width*0.14

    start = 0
    for i in range(255):
        end = i
        draw.rectangle((0, bottom+start, width, bottom+end), fill=(255, 255, 255, 255-i))
        start = end
    
    draw.rectangle((0, 0, width, bottom), fill=(255, 255, 255, 255))
    result = Image.alpha_composite(result,blur)
    
    return result



filename = sys.argv[1]

result = make_spherical(filename)
(body, ext) = filename.split('.')

result = result.convert('RGB')
img_w10k = result.resize((10000, 5000))
img_w5000 = result.resize((5000, 2500))
img_w2500 = result.resize((2500, 1250))

img_w10k.save(body + '_w10k.jpg', quality=60)
img_w5000.save(body + '_w5k.jpg', quality=60)
img_w2500.save(body + '_w2500.jpg', quality=60)
