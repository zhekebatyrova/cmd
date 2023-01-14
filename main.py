import os
import sys
import datetime

# args = [main.py]
# args[0] = "."
# args = [.]

# args = [main.py, abc, efg]
# args = args[1:]
# args = [abc, efg]

args = sys.argv


def directory():
    for path in args:
        if path[len(path) - 1] != "/":
            path += "/"

        print("folder contents", os.path.abspath(path))

        if not os.path.exists(path):
            print("file not found")
            continue

        for directory in os.listdir(path):
            fullPath = path + directory
            creationDate = datetime.datetime.fromtimestamp(os.path.getmtime(fullPath)).strftime("%Y-%m-%d  %H:%M")

            if not os.path.isdir(fullPath):
                print(creationDate, "\t     ", os.path.getsize(fullPath), "\t", directory)
                continue

            print(creationDate, "\t<DIR>", os.path.getsize(fullPath), "\t", directory)


def make_directory():
    for arg in args[1:]:
        if os.path.exists(arg):
            print("file '" + arg + "' already exists")
            continue

        os.makedirs(arg)
        print("created '" + arg + "' directory")


def rename_directory(from_name, to_name):
    if not os.path.exists(from_name):
        print("file '" + from_name + "' does not exists")
    else:
        os.rename(from_name, to_name)
        print("file '" + from_name + "' renamed to '" + to_name + "'")


def remove_directory(directory):
    try:
        os.rmdir(directory)
        print("file '" + directory + "' removed")
    except FileNotFoundError:
        print("file '" + directory + "' does not exists")
    except PermissionError:
        print("You do not have permission to delete this file.")


def remove_file(filename):
    try:
        os.remove(filename)
        print("file '" + filename + "' removed")
    except FileNotFoundError:
        print("file '" + filename + "'does not exists")
    except PermissionError:
        print("You do not have permission to delete this file.")


def change_directory(directory):
    try:
        os.chdir(directory)
        print(f"Current working directory: {os.getcwd()}")
    except FileNotFoundError:
        print(f"{directory} is not a valid directory")


def cat(file):
    try:
        with open(file, "r") as txt_file:
            print(txt_file.read())
    except IOError:
        print(f"An error occurred while opening {file}")


if len(args) == 1:
    args[0] = "."
    directory()
else:
    args = args[1:]

    command = args[0]
    if command == "mkdir" and len(args) >= 2:
        make_directory()
    elif command == "rename" and len(args) == 3:
        rename_directory(args[1], args[2])
    elif command == "rmdir" and len(args) >= 2:
        remove_directory(args[1])
    elif command == "rm" and len(args) >= 2:
        remove_file(args[1])
    elif command == "cd" and len(args) == 2:
        change_directory(args[1])
    elif command == "cat" and len(args) == 2:
        cat(args[1])
    else:
        directory()