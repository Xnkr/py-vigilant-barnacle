import os
folder_path = "C:\\Users\\Shankar\\Desktop\\Test"

def expand_folders(folder_names):
    result_dict= {}
    for name in folder_names:
        folder = os.path.join(folder_path, name)
        result_dict[name] = os.listdir(folder)
    return result_dict



print("Folders List")
print(os.listdir(folder_path))
print()
folder_names = []
while True:
    name = input("Select a folder to expand: ")
    if(name == 'Q' or name == 'q'):
        break
    folder_names.append(name)
result_dict = expand_folders(folder_names)
print(result_dict)