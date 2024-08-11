"""
This script creates a file to list dataset images.
Images are listed in the format :
train/00077932462df208
train/002ed7cd133939ea
validation/ce05c78f65ee8ade
test/86411d79db734687
"""

import os

class_ids = ['class1_id','class2_id',...]

train_bboxes_filename = os.path.join('.', 'oidv6-train-annotations-bbox.csv')
validation_bboxes_filename = os.path.join('.', 'validation-annotations-bbox.csv')
test_bboxes_filename = os.path.join('.', 'test-annotations-bbox.csv')

image_list_file_path = os.path.join('.', 'image_list_file.txt')

image_list_file_list = []
for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]):
    print(j,filename)
    with open(filename, 'r') as f:
        line = f.readline()
        while len(line) != 0:
            id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
            if class_name in class_ids and id not in image_list_file_list:
                image_list_file_list.append(id)
                with open(image_list_file_path, 'a') as fw:
                    fw.write('{}/{}\n'.format(['train', 'validation', 'test'][j], id))
            line = f.readline()

        f.close()
