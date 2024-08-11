"""
This scripts computes the number of images in each classes for train, validation, and test sets.
"""

import os
import pandas as pd

train_bboxes_filename = os.path.join('.', 'oidv6-train-annotations-bbox.csv')
validation_bboxes_filename = os.path.join('.', 'validation-annotations-bbox.csv')
test_bboxes_filename = os.path.join('.', 'test-annotations-bbox.csv')
class_des_filename = os.path.join('.', 'oidv6-class-descriptions.csv')
class_des = pd.read_csv(class_des_filename,index_col="LabelName")

def get_class_freq(cf, filename):
    with open(filename,'r') as f :
        line = f.readline()
        while len(line)!=0 :
            id, _, class_code, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
            if cf.get(class_code) == None :
                cf[class_code] = 0
            cf[class_code] = cf[class_code] + 1
            line = f.readline()
        f.close()
    return cf
    
class_freq = dict()
for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]):
    print(j,filename)
    col = ['train','val','test'][j]
    class_freq[col] = get_class_freq(dict(),filename)


class_freq = pd.DataFrame(class_freq)
class_des["Train"] = class_freq["train"]
class_des["Validation"] = class_freq["val"]
class_des["Test"] = class_freq["test"]
os.remove(class_des_filename)
class_des.to_csv(os.path.join(".","class_descriptions.csv"))


