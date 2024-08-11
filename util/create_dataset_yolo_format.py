import os
import shutil

DATA_OUT_DIR = os.path.join('.', 'data')
if not os.path.exists(DATA_OUT_DIR):
    os.mkdir(DATA_OUT_DIR)
    
for set_ in ['train', 'val', 'test']:
    for dir_ in [os.path.join(DATA_OUT_DIR, set_),
                 os.path.join(DATA_OUT_DIR, set_, 'images'),
                 os.path.join(DATA_OUT_DIR, set_, 'labels')]:
        if os.path.exists(dir_):
            shutil.rmtree(dir_)
        os.mkdir(dir_)

# Fill in selected classes IDs
class_ids = ['class1_id','class2_id',...]

train_bboxes_filename = os.path.join('.', 'oidv6-train-annotations-bbox.csv')
validation_bboxes_filename = os.path.join('.', 'validation-annotations-bbox.csv')
test_bboxes_filename = os.path.join('.','test-annotations-bbox.csv')


for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]):
    set_ = ['train', 'val', 'test'][j]
    with open(filename, 'r') as f:
        line = f.readline()
        while len(line) != 0:
            id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
            if class_name in class_ids:
                with open(os.path.join(DATA_OUT_DIR, set_, 'labels', '{}.txt'.format(id)), 'a') as f_ann:
                    # class_id, xc, yx, w, h
                    x1, x2, y1, y2 = [float(j) for j in [x1, x2, y1, y2]]
                    xc = (x1 + x2) / 2
                    yc = (y1 + y2) / 2
                    w = x2 - x1
                    h = y2 - y1

                    f_ann.write('{} {} {} {} {}\n'.format(class_ids.index(class_name),xc, yc, w, h))
                    f_ann.close()

            line = f.readline()

