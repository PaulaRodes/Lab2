import os


#  we define the path to the videos
path = '/Users/Paula/PycharmProjects/pythonProject/vids'
#  and put the videos in a list
files = os.listdir(path)
#  run the list
input = 'video'
for index, file in enumerate(files):
    # rename each file in the list
    os.rename(os.path.join(path, file), os.path.join(path, input.join([str(index), '.mp4'])))

