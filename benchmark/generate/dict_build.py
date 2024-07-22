import os
import shutil

def organize_images(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    for filename in os.listdir(source_dir):

        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):

            key = filename.split(',')[0]
            folder_path = os.path.join(target_dir, key)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            source_path = os.path.join(source_dir, filename)
            target_path = os.path.join(folder_path, filename)
            shutil.move(source_path, target_path)
    print("finished")

def dir_build(source_directory, target_directory):
    organize_images(source_directory, target_directory)

