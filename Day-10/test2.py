import os

def list_of_files(folder):

    try:
      files=os.listdir(folder)
      return files, None
    except FileNotFoundError:
      return None, "File not found"
    except PermissionError:
      return None, "Access Denied"
    
def main():
    folders=input("Please enter the list of folders").split()

    for folder in folders:
        files, error_message = list_of_files(folder)
        if files:
            for file in files:
                print(file)

        else:
            print(f"Error {folder}: {error_message}")


if __name__ == "__main__":
    main()