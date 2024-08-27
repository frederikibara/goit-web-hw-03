import os
import shutil
import sys
from threading import Thread
from pathlib import Path

def copy_file(file_path, dest_dir):
    """
    Copies file to appropriate subdirectory of the target directory by file extension.
    """
    extension = file_path.suffix.lstrip('.').lower()
    target_dir = dest_dir / extension
    
    if not target_dir.exists():
        target_dir.mkdir(parents=True, exist_ok=True)

    shutil.copy(file_path, target_dir / file_path.name)

def process_subdirectory(sub_dir, dest_dir):
    """
    Process all files in a subdirectory.
    """
    threads = []
    for file in os.listdir(sub_dir):
        file_path = sub_dir / file
        if file_path.is_file():
            t = Thread(target=copy_file, args=(file_path, dest_dir))
            t.start()
            threads.append(t)
    
    for t in threads:
        t.join()

def process_directory(src_dir, dest_dir):
    """
    Recursively processes a directory, 
    copying files to the appropriate subdirectories in the target directory.
    """
    
    threads = []  
    for root, dirs, files in os.walk(src_dir):
        root_path = Path(root)
     
        for dir in dirs:
            dir_path = root_path / dir
            trd = Thread(target=process_subdirectory, args=(dir_path, dest_dir))
            trd.start()
            threads.append(trd)

        for file in files:
            file_path = root_path / file
            trd = Thread(target=copy_file, args=(file_path, dest_dir))
            trd.start()
            threads.append(trd)
    
    for trd in threads:
        trd.join()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(" 1) Using console \n 2) Write a command : cd junk_directory_handler \n 3) Run : python dir_handler.py <source_dir> <destination_dir>" )
        sys.exit(1)

    src_directory = Path(sys.argv[1])
    dest_directory = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('sorted')

    if not src_directory.is_dir():
        print(f"source dir {src_directory} does not exist or not a directory.")
        sys.exit(1)

    if dest_directory.exists() and not dest_directory.is_dir():
        print(f"destination dir {dest_directory} is not a directory.")
        sys.exit(1)

    print(f"Scanning directory... {src_directory}...")
    process_directory(src_directory, dest_directory)
    print("FINISHED")
