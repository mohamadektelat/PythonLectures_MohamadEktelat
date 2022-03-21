# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# This function responsible for joining a number of lists into one list with the specific separator.
# This function gets an unknown number of lists and a separator(if not the default sep is -).
def join(*args, sep='-'):
    if len(args) == 0:
        return []
    merged_list = []
    for arg in args:
        merged_list = merged_list + arg
        merged_list.append(sep)
    return merged_list[:-1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
