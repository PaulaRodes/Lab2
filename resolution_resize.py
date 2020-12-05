from PIL import Image
import os

path = '/Users/Paula/PycharmProjects/pythonProject/foto'


def resize(width, height):
    for item in os.listdir(path):
        im = Image.open(item)
        f, e = os.path.splitext(item)
        imresize = im.resize((width,height), Image.ANTIALIAS)
        imresize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize(200,300)





