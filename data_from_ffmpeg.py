import os

#  we get 3 relevant data from the video using ffmpeg
# print the format
os.system("ffprobe -i bbb_original.mp4 -v quiet -print_format json -show_format")
# print the streams
os.system("ffprobe -i bbb_original.mp4 -v quiet -print_format json -show_streams")
# print the duration
os.system("ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 bbb_original.mp4")

