import os
import shutil

ROOT_DIR = os.getcwd()

# Creating subfolders for I/O
inputdir = os.path.join(ROOT_DIR,'input')
outputdir = os.path.join(ROOT_DIR,'output')
if not os.path.exists(inputdir) :
    os.mkdir(inputdir)
if not os.path.exists(outputdir) :
    os.mkdir(outputdir)

# Moving config.yaml to data root directory
src = os.path.join(ROOT_DIR,'config.yaml')
dest = os.path.join(ROOT_DIR,'data','config.yaml')
shutil.move(src,dest) 

# Organizing utilities
utildir = os.path.join(ROOT_DIR,'util')
if not os.path.exists(utildir) :
    os.mkdir(utildir)
filenames = ['compute_class_freq.py','create_dataset_yolo_format.py','create_image_list_file.py',\
             'downloader_modified.py','image_list_file.txt']
for file in filenames:
    dest = os.path.join(ROOT_DIR,'util',file)
    shutil.move(os.path.join(ROOT_DIR,file),dest)
