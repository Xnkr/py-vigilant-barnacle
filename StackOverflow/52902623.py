import os
import shutil

src_dir = "F:\\Port"
f_list = os.listdir(src_dir)
print(f'Initial directory listing {f_list}')
retain_list = []

for folder in f_list:
    if len(os.listdir(os.path.join(src_dir,folder))):
        # Folder not empty
        base, n = folder.rsplit('_',1)
        if base not in retain_list:
            retain_list.append(base)
    else:
        shutil.rmtree(os.path.join(src_dir,folder))

f_list = os.listdir(src_dir)
print(f'Directory listing after removing empty folders {f_list}')

for f in retain_list:
    i = 1
    for folder in f_list:
        base, n = folder.rsplit('_',1)
        if f == base:
            os.rename(os.path.join(src_dir,folder),os.path.join(src_dir,f'{base}_{i}'))
            i += 1

f_list = os.listdir(src_dir)
print(f'Final directory listing {f_list}')