# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os


# This function is responsible for checking the files names in specific folder if they starts with "deep".
def get_files():
    # getting the folder path from the user.
    path = input("please enter the file path: ")
    # check the files in the folder.
    arr = [file for file in os.listdir(path) if file.startswith("deep")]
    return arr


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    files = get_files()
    print(files)
