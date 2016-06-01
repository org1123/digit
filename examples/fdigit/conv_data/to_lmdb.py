'''
Created on Jul 18, 2015

@author: kashefy
'''
import os
import numpy as np
from scipy import io
import lmdb
from read_img import read_img_cv2

NUM_IDX_DIGITS = 10
IDX_FMT = '{:0>%d' % NUM_IDX_DIGITS + 'd}'

def imgs_to_lmdb(paths_src, path_dst, CAFFE_ROOT=None):
    '''
    Generate LMDB file from set of images
    Source: https://github.com/BVLC/caffe/issues/1698#issuecomment-70211045
    credit: Evan Shelhamer
    '''
    import numpy as np
    if CAFFE_ROOT is not None:
        import sys
        sys.path.insert(0, CAFFE_ROOT + 'python')
    import caffe
    
    db = lmdb.open(path_dst, map_size=int(1e12))
    size = np.zeros([len(paths_src), 2])
    with db.begin(write=True) as in_txn:
        i = 1
        for idx, path_ in enumerate(paths_src):
            print str(i)+' of '+str(len(paths_src))+' ...'
            #print str(paths_src)
            img = read_img_cv2(path_)
            size[i-1, :] = img.shape[1:]
            img_dat = caffe.io.array_to_datum(img)
            in_txn.put(IDX_FMT.format(idx), img_dat.SerializeToString())
            i = i + 1
    db.close()

    return size

def matfiles_to_lmdb(paths_src, path_dst, fieldname,
                     CAFFE_ROOT=None,
                     lut=None):
    '''
    Generate LMDB file from set of images
    Source: https://github.com/BVLC/caffe/issues/1698#issuecomment-70211045
    credit: Evan Shelhamer
    
    '''
    if CAFFE_ROOT is not None:
        import sys
        sys.path.insert(0,  os.path.join(CAFFE_ROOT, 'python'))
    import caffe
    db = lmdb.open(path_dst, map_size=int(1e12))
    size = np.zeros([len(paths_src), 2])
    with db.begin(write=True) as in_txn:
        i = 1
        for idx, path_ in enumerate(paths_src):
            print str(i)+' of '+str(len(paths_src))+' ...'
            
            content_field = io.loadmat(path_)[fieldname]          
            content_field = np.expand_dims(content_field, axis=0)   ##########
            #content_field = np.transpose(content_field,(2,0,1))
            content_field = content_field.astype(float)
	    print content_field.shape
            
            if lut is not None:
                content_field = lut(content_field)
            size[i-1, :] = content_field.shape[1:]
            img_dat = caffe.io.array_to_datum(content_field)
            in_txn.put(IDX_FMT.format(idx), img_dat.SerializeToString())
            i = i + 1
    
    db.close()

    return size

