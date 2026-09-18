import os
import shutil

source_folder = "images"
destination_folder = "jpg_files"

os.makedirs(destination_folder, exist_ok=True)

files = os.listdir(source_folder)

for file in files:
    print("Found:", file)

    if file.lower().endswith((".jpg", ".jpeg")):
        shutil.move(
            os.path.join(source_folder, file),
            os.path.join(destination_folder, file)
        )
        print(file, "moved successfully!")

print("All JPG files are moved.")

