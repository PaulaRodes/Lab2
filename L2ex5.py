import os
from PIL import Image


def rename (path, name):
    files = os.listdir(path)
    input = name
    for index, file in enumerate(files):
        # rename each file in the list
        os.rename(os.path.join(path, file), os.path.join(path, input.join([str(index), '.mp4'])))


def resize(width, height, path):
    for item in os.listdir(path):
        im = Image.open(item)
        f, e = os.path.splitext(item)
        imresize = im.resize((width,height), Image.ANTIALIAS)
        imresize.save(f + 'image', 'JPEG', quality=90)


path1 = '/Users/Paula/PycharmProjects/pythonProject/vids'
path2 = '/Users/Paula/PycharmProjects/pythonProject/foto'
name1 = 'video'
rename(path1, name1)
resize(300, 400, path2)