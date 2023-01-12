#!/usr/bin/python3
""" THIS SCRIPT ADDS ALL ARGUMENTS TO A PYTHON LIST.
    AND SAVE THEN TO A FILE
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """ Adds all arguments to a list and save to a file """
    num = len(sys.argv)
    file_name = "add_item.json"
    try:
        my_list = load_from_json_file(file_name)
        for i in range(1, num):
            my_list.append(sys.argv[i])
        save_to_json_file(my_list, file_name)
    except FileNotFoundError:
        my_list = []
        if num == 1:
            save_to_json_file(my_list, file_name)
        else:
            for i in range(1, num):
                my_list.append(sys.argv[i])
            save_to_json_file(my_list, file_name)


if __name__ == '__main__':
    main()
