import os
import shutil
from_dir="/Users/ratanswain/Desktop/folder1"
to_dir="/Users/ratanswain/Desktop/folder2"
list_files=os.listdir(from_dir)
print(list_files)
for file_name in list_files :
 name,extension=os.path.splitext(file_name)
 print(extension)
 print(name)

 path1= from_dir+'/'+file_name
 path2=to_dir+'/'+'Document_file'
 path3=to_dir+'/'+'Document_file'+'/'+file_name
 

if os.path.exists(path2):
    print('moving' + file_name+'....')

    shutil.move(path1,path3)

else:
    os.makedirs(path2)
    print('moving' + file_name+'....')
    shutil.move(path1,path3)