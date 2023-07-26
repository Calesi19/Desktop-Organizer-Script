import os
import shlex
import getpass


# Script to clean up the desktop by moving files into folders

# Get the current user name
user = getpass.getuser()

# Get desktop directory
desktop_directory = f"/Users/{user}/Desktop"
print(desktop_directory)

# Get all files in the desktop directory
files = os.listdir(desktop_directory)


# Check if Screenshot folder exists in desktop directory
if "Screenshots" not in files:
    # Create a folder called Screenshots
    os.mkdir(f"{desktop_directory}/Screenshots")
    print("Screenshots folder created")

# Check if PDFs folder exists in desktop directory
if "PDFs" not in files:
    # Create a folder called PDFs
    os.mkdir(f"{desktop_directory}/PDFs")
    print("PDFs folder created")

# Check if Images folder exists in desktop directory
if "Images" not in files:
    # Create a folder called Images
    os.mkdir(f"{desktop_directory}/Images")
    print("Images folder created")

# Check if Files folder exists in desktop directory
if "Files" not in files:
    # Create a folder called Files
    os.mkdir(f"{desktop_directory}/Files")
    print("Files folder created")




# Loop through all files in the desktop directory. 
for file in files:
    
    file = shlex.quote(file)


    # If "screenshot" in the file name, move it to the Screenshots folder
    if "screenshot" in file.lower():
        
        # Move the file to the Screenshots folder
        cmd = "mv " + os.path.join(desktop_directory, file) + " " + os.path.join(desktop_directory, "Screenshots", file)
        os.system(cmd)

        print(f"{file} moved to Screenshots folder")
        

        # Go to the next file
        continue
    
    # If ".pdf" in the file name, move it to the PDFs folder
    if ".pdf" in file.lower():
        
        # Move the file to the PDFs folder
        cmd = "mv " + os.path.join(desktop_directory, file) + " " + os.path.join(desktop_directory, "PDFs", file)
        os.system(cmd)

        print(f"{file} moved to PDFs folder")

        # Go to the next file
        continue

    # If ".png" or ".jpg" or ".jpeg" in the file name, move it to the Images folder
    if ".png" in file.lower() or ".jpg" in file.lower() or ".jpeg" in file.lower() or ".gif" in file.lower():
        # Move the file to the Images folder
        cmd = "mv " + os.path.join(desktop_directory, file) + " " + os.path.join(desktop_directory, "Images", file)
        os.system(cmd)

        print(f"{file} moved to Images folder")

        # Go to the next file
        continue

    
    # If file.lower is not "screenshots" or "pdfs" or "images" or "files", move it to the Files folder
    if file.lower() != "screenshots" and file.lower() != "pdfs" and file.lower() != "images" and file.lower() != "files":

        # Move all remaining files to the "Files" folder
        cmd = "mv " + os.path.join(desktop_directory, file) + " " + os.path.join(desktop_directory, "Files", file)
        print(f"{file} moved to Files folder")
        
        continue    


# Get all files in the desktop directory

files = os.listdir(desktop_directory)

# if files is not empty, print the remaining files
if files:
    print("Remaining files:")
    count = 1
    for file in files:
        if file.lower() != "screenshot" and file.lower() != "pdfs" and file.lower() != "images" and file.lower() != "files":
            print(f"{count}. {file}")
            count += 1
else:
    print("No remaining files")
