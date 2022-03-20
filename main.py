# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os


def get_files():
    path = input("please enter the file path: ")
    arr = []
    for file in os.listdir(path):
        if file.startswith("deep"):
            arr.append(file)
    return arr


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    files = get_files()
    print(files)
