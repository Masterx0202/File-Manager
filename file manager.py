import os
import tkinter
from tkinter import filedialog
import shutil

print("choose source and destination Folder")

# choose source folder
tkinter.Tk().withdraw()
folsrc = filedialog.askdirectory()

# choose destination folder
dstfr = filedialog.askdirectory()

# Create directories if they don't exist
for folder_name in ["pictures", "videos", "other files"]:
    folder_path = os.path.join(dstfr, folder_name)
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)

countmp4 = 0
countjpg = 0

for file in os.listdir(folsrc):
    # Get file extension and name
    idkext = os.path.splitext(file)
    ext = idkext[1]
    nme = idkext[0]

    # Determine file type
    if ext == ".jpg" or ext == ".png":
        typ = "pictures"
    elif ext == ".mp4":
        typ = "videos"
    else:
        typ = "other files"

    src = os.path.join(folsrc, file)
    dst = os.path.join(dstfr, typ)

    # Rename and move file
    if ext == ".jpg" or ext == ".png":
        new_filename = f"{countjpg}{ext}"
        while os.path.exists(os.path.join(dst, new_filename)):
            countjpg += 1
            new_filename = f"{countjpg}{ext}"
        os.rename(src, os.path.join(dst, new_filename))
        countjpg += 1
    elif ext == ".mp4":
        new_filename = f"{countmp4}{ext}"
        while os.path.exists(os.path.join(dst, new_filename)):
            countmp4 += 1
            new_filename = f"{countmp4}{ext}"
        os.rename(src, os.path.join(dst, new_filename))
        countmp4 += 1
    else:
        print("There are other files in the folder")
        dst = os.path.join(dstfr, "other files")
        while os.path.exists(os.path.join(dst, file)):
            file = f"{nme}_{countmp4}{ext}"
            countmp4 += 1
        shutil.move(src, dst)
    print("moved:", file)

print("Process completed successfully.")
