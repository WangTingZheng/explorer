import os

#suffix_list=[".py",".yml"]
#suffix_list=[]


def get_upper_level(path):
    folder=''
    tmp=[]
    for i in path:
        if i =='/':
            tmp.append(folder)
            folder=''
        else:
            folder+=i
    del tmp[len(tmp)-1]
    if len(tmp)!=0:
        paths=''
        for j in tmp:
            paths+=j+'/'
        return paths
    else:
        return False
# the file name is python soruce code ?
# name: a string like test.py
# return : true or false


def isCode(name,suffix):
    lens = len(name)
    code = name[lens-len(suffix):]
    if code == suffix:
        return True
    else:
        return False

def isSuffix(name,suffix_list):
    for i in suffix_list:
        if isCode(name,i) is True:
            return True
    return False

# the path is a folder?
# path : target path like ./
# return : Ture or False
def isFolder(path):
    if os.path.isdir(path):
        return True
    elif os.path.isfile(path):
        return False

# find folder in path
# path : target path like ./
# return : a list like:
# ['.git', '.vscode', 'build', 'data', 'dist', 'pianyuan', 'pianyuan.egg-info', 'test', '__pycache__']
def find_folder(path):
    folder=[]
    all = os.listdir(path)
    for i in all:
        if isFolder(i) is True:
            folder.append(i)
    return folder


# find all python file name in a folder without folder
# # path : target path like ./
# return ['crawl.py', 'key.py', 'picks.py', 'spider.py', 'test.py', 'tinydb.py']
def find_py_in_last_folder(path,suffix_list):
    list_temp = []
    list = []

    for i in os.listdir(path):
        list_temp.append(i)

    for a in list_temp:
        if isSuffix(a,suffix_list):
            list.append(a)

    return list


# find all python file in path
# path : target path like ./
#return :
def find_py(path):
    all_menu=[]
    all_menus={}
    folder=find_folder(path)
    for i in folder:
        all_menu.append(i)
    if len(all_menu)!=0:
        for j in all_menu:
            all = os.listdir(path+j)
            for x in all:
                all_menus[j]=all
        return all_menus
    else:
        return find_py_in_last_folder(path)


# the folder have python file
def have_py_in(listname,suffix_list):
    for i in listname:
        if isSuffix(i,suffix_list):
            return True
    return False

def get_py_in_folder(path,suffix_list):
    tmp=[]
    for i in os.listdir(path):
        if os.path.isfile(path+i) is True:
            if isSuffix(i,suffix_list) is True:
                tmp.append(i)
    return tmp

def have_py_in_folder(path,suffix_list):
    tmp=get_py_in_folder(path,suffix_list)
    if len(tmp)==0:
        return False
    else:
        return True

# find all folder which has python file
def return_py_folder(path):
    folder=find_py(path)
    py_folder=[]
    for i in folder:
        if have_py_in(folder[i]) is True:
            py_folder.append(i)
    return py_folder