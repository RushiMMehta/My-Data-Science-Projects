from pathlib import Path
import os

def readfolder():
    path= Path('')#gives path of current folder
    items = list(path.rglob('*'))  # Get all items in the current directory
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readfolder()
        name = input("Enter the name of the file to create: ")
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as file:
                data = input("Enter the data to write in the file: ")
                file.write(data)
            print(f"File : '{name}' created successfully.")
        else:
            print(f"File : '{name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")


def readfile():
    try:
        readfolder()
        name = input("Enter the name of the file to read: ")
        p = Path(name)
        if p.exists():
            with open(p, 'r') as file:
                data = file.read()
                print(f"Content of '{name}':\n{data}")
        else:
            print(f"File : '{name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def updatefile():
    try:
        readfolder()
        name = input("Enter the name of the file to update: ")
        p = Path(name)
        if p.exists():
            with open(p, 'a') as file:
                data = input("Enter the data to append in the file: ")
                file.write('\n' + data)
            print(f"File : '{name}' updated successfully.")
        else:
            print(f"File : '{name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def deletefile():
    try:
        readfolder()
        name = input("Enter the name of the file to delete: ")
        p = Path(name)
        if p.exists():
            os.remove(p)
            print(f"File : '{name}' deleted successfully.")
        else:
            print(f"File : '{name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deletion a file")
choice = input("Enter your choice: ")   

if choice == '1':
    createfile()
elif choice == '2':
    readfile()
elif choice == '3':
    updatefile()
else:
    deletefile()
print("Thank you for using the file management system.")