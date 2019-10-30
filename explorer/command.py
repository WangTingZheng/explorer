import argparse
from explorer.menu import *
from explorer.apart import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("list")
    args = parser.parse_args()
    list = args.list
    list = apart(list, "/")
    if len(list) == 1 and list[0] == "none":
        menu(args.path, [])
    else:
        menu(args.path, list)
