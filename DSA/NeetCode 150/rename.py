import os

# Specify the suffixes to remove
suffixes = ["-Easy", "-Medium", "-Hard"]

# Get all files in the current directory
files = os.listdir(".")

for file_name in files:
    # Check if the file name ends with any of the specified suffixes
    for suffix in suffixes:
        if file_name.endswith(suffix):
            # Determine the new file name by removing the suffix
            new_name = file_name[: -len(suffix)]
            # Rename the file
            os.rename(file_name, new_name)
            print(f"Renamed: {file_name} -> {new_name}")
            break
