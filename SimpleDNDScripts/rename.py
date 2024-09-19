import os

# Define the path to your specific folder
folder_path = os.path.expanduser("~/Downloads/Lost Mine of Phandelver")

# Iterate over all files in the specified folder
for filename in os.listdir(folder_path):
    # Separate the base name and extension
    basename, ext = os.path.splitext(filename)
    
    # Check if the extension is .jpg
    if ext.lower() == '.jpg' and len(basename) > 2:
        # Generate the new file name by keeping only the last two digits
        new_filename = basename[-2:] + ext
        
        # Construct the old and new file paths
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f'Renamed: {filename} -> {new_filename}')
    else:
        print(f'Skipped: {filename} (not a .jpg file or name too short)')
