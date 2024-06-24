import shutil
import os

folder_track = r'C:\Users\Danik\Desktop\python\project3_1\picture'     # папка у  
folder_move = r'C:\Users\Danik\Desktop\python\project3_1\dist'         # папка куди буде переноситися файкли

formats = {
    "jpg": "jpg",
    "png": "png",
    "svg": "svg"
}

def sort_format():
    for root, dir, files in os.walk(folder_track):
        for filename in files:
            extension = os.path.splitext(filename)[1].lower()[1:]
            if extension in formats:
                source_file = os.path.join(root, filename)
                dest_folder = os.path.join(folder_move, formats[extension])
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                dest_file = os.path.join(dest_folder, filename)
                shutil.move(source_file, dest_file)

sort_format()