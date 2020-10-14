############### 0)
import os

def mkdict (path = os.getcwd()):
    list_dir = os.listdir(path)
    files = []
    folders = []
    for item in list_dir:
        if os.path.isfile(item):
            files.append(item)
        else:
            folders.append(item)
    path_dict = {'files': files, 'folders': folders}
    return path_dict

path_dict = mkdict()
print(path_dict)