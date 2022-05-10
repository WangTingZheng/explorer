from explorer.file import *
from pick import pick


def menu(path, suffix_list):
    if path[0] == ".":
        path = path[1:]
        path = os.getcwd().replace("\\", "/") + path
    if path:
        list_temp = []
        list = []
        folder = []
        for i in os.listdir(path):  # get a file and folder
            list_temp.append(i)

        for b in list_temp:  # get folder
            if isFolder(path + b) is True:
                folder.append(b)

        if len(suffix_list) == 0:
            list = list_temp
        else:
            for b in folder:  # get the folder which have the file we want
                if have_py_in_folder(path + b + "/", suffix_list) is True:
                    list.append(b)
            for a in list_temp:  # get file we want
                if isSuffix(a, suffix_list):
                    list.append(a)
        title = "Please choose a python file(press SPACE to mark, ENTER to continue): "
        options = list
        options.append(">back<")
        options.append(">quit<")
        selected = pick(options, title, multiselect=True, min_selection_count=1)
        selected_deal(selected, list, suffix_list, path)
    else:
        print("The path is invaild!")


def selected_deal(selected, list, suffix_list, path):
    selected_name = selected[0][0]
    selected_numb = selected[0][1]
    if selected_numb == len(list) - 1:
        quit()
    elif selected_numb == len(list) - 2:
        if get_upper_level(path) is False:
            menu(path, suffix_list)
        else:
            menu(get_upper_level(path), suffix_list)
    else:
        if isFolder(path + selected_name) is True:
            menu(path + selected_name + "/", suffix_list)
        else:
            shell = "python " + path + "/" + selected_name
            os.system(shell)
