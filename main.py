import os
import shutil
from os import listdir
from os.path import isfile, join


def organize_files(downpath):
    files = [f for f in listdir(downpath) if isfile(join(downpath, f))]
    file_type_variation_list=[]
    ext_folder_dic={}
    for file in files:
        file_extension=file.split('.')[1]
        if file_extension not in file_type_variation_list:
            file_type_variation_list.append(file_extension)
            newfolder=downpath+'/'+ file_extension + '_folder'
            ext_folder_dic[str(file_extension)]=str(newfolder)
            if os.path.isdir(newfolder)==True:  #folder exists
                continue
            else:
                os.mkdir(newfolder)

    for file in files:
        src_path=downpath+'/'+file
        file_extension=file.split('.')[1]
        if file_extension in ext_folder_dic.keys():
            dest_path=ext_folder_dic[str(file_extension)]
            try:
                shutil.move(src_path,dest_path)
            except:
                continue

if __name__=="__main__":
    downloads_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    while True:
        organize_files(downloads_folder)