#python 3.11

import os

cnt = 0
downloads_folder = 'C:/Users/Moz/Downloads/'
music_folder = 'C:/Users/Moz/Music/'
for _, _, filenames in os.walk(downloads_folder):
    for filename in filenames:
        if filename.endswith('.mp3'):
            for char in filename[-12:-4]:
                if char in ('1','2','3','4','5','6','7','8','9','0'):
                    cnt += 1
            else:
                if cnt >= 8:
                    new_filename = filename[:-13]+filename[-4:]
                    new_filename = new_filename.replace("_", " ")
                    os.replace(downloads_folder + filename, music_folder + new_filename)
                    os.exit()
            os.replace(downloads_folder + filename, music_folder + filename)

