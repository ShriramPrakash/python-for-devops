import os

folders = input("Please provide the list of folders:" ).split()
print(folders)

for folder in folders:
    try:
        print(f"Name of the folder:{folder}")
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Enter a valid folder name")
        continue
    except  PermissionError:
        print("You dont have the permission")
        continue
    for file in files:
        print(file)
    
