import os
import shutil
import sys

def copy_files(source_dir, dest_dir):
    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate over items in the source directory
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)

        # If it's a directory, recursively copy its contents
        if os.path.isdir(item_path):
            copy_files(item_path, dest_dir)

        # If it's a file, copy it to the destination directory
        elif os.path.isfile(item_path):
            # Get the file extension
            _, extension = os.path.splitext(item)
            # Create subdirectory based on file extension
            sub_dir = os.path.join(dest_dir, extension[1:])
            if not os.path.exists(sub_dir):
                os.makedirs(sub_dir)
            # Copy file to the corresponding subdirectory
            shutil.copy2(item_path, sub_dir)

def main():
    # Parsing command line arguments
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [<destination_directory>]")
        sys.exit(1)
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    try:
        # Recursively copy files
        copy_files(source_dir, dest_dir)
        print("Files copied successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
