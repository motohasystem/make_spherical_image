from PIL import Image, ImageDraw
import sys

def make_spherical(filename):
    img = Image.open(filename)
    width, height = img.size

    new_height = int(width / 2)
    result = Image.new(img.mode, (width, new_height), (0, 0, 0))
    result.paste(img, (0, new_height - height))
    
    draw = ImageDraw.Draw(result)
    color_white = (255, 255, 255)
    draw.rectangle((0, 0, width, width*0.14), fill=color_white, outline=color_white)
    
    return result


filename = sys.argv[1]

result = make_spherical(filename)
(body, ext) = filename.split('.')

img_w10k = result.resize((10000, 5000))
img_w5000 = result.resize((5000, 2500))
img_w2500 = result.resize((2500, 1250))

img_w10k.save(body + '_w10k.jpg', quality=60)
img_w5000.save(body + '_w5k.jpg', quality=60)
img_w2500.save(body + '_w2500.jpg', quality=60)
