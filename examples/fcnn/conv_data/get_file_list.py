__author__ = 'Administrator'

import os

def get_file_list(root_dir, file_list):
    new_dir = root_dir
    if os.path.isfile(root_dir):
        file_list.append(root_dir.decode('gbk'))
    elif os.path.isdir(root_dir):
        for s in os.listdir(root_dir):
            new_dir=os.path.join(root_dir,s)
            get_file_list(new_dir, file_list)
    return file_list

list = get_file_list('D:/WeiShen/Code/DPL/caffe2/BSR/BSDS500/data/images/train', [])
for e in list:
    print e
