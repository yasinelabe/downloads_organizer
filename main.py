import os
import shutil
import random
from os import listdir
from os.path import isfile, join


def organize_files(downpath):
    files = [f for f in listdir(downpath) if isfile(join(downpath, f))]
    file_type_variation_list=[]
    ext_folder_dic={}
    for file in files:
        # if file contains more than one dot, remove all the dots except the last one
        if file.count('.') > 1:
            file_ext = file.split('.')[-1]
            file_name = file.split('.')[0]
            #rename the file to the file name with the file extension
            # delete if the file already exists
            if os.path.exists(join(downpath, file_name + '.' + file_ext)):
                os.chmod(join(downpath, file_name + '.' + file_ext), 0o777)
                os.remove(join(downpath, file_name + '.' + file_ext))

            os.rename(join(downpath, file), join(downpath, file_name + '.' + file_ext))
            file = file_name + '.' + file_ext
            
            

        
        file_extension=file.split('.')[-1]
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
        file_extension=file.split('.')[-1]
        if file_extension in ext_folder_dic.keys():
            dest_path=ext_folder_dic[str(file_extension)]
            try:
                shutil.move(src_path,dest_path)
            except:
                # rename the file name and add random number to it to avoid the same file name , then move it
                try:
                    file_name=file.split('.')[0]
                    file_ext=file.split('.')[-1]
                    file_name=file_name+'_'+str(random.randint(1,100))
                    os.rename(join(downpath,file),join(downpath,file_name+'.'+file_ext))
                    src_path= join(downpath, file_name + '.' + file_ext)
                    shutil.move(src_path,dest_path)
                except:
                    continue

if __name__=="__main__":
    downloads_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    while True:
        organize_files(downloads_folder)