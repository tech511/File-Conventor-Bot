import os

def convert_mp3(input_file, output):

    cmd = f'ffmpeg -i "{input_file}" -vn -ab 192k "{output}"'

    os.system(cmd)
