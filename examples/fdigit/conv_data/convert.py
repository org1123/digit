import os
import sys
import numpy as np
import to_lmdb
import fileSystemUtils as fs
import cv2 as cv2
#import cv2.cv as cv
import lmdb
import scipy.io
CAFFE_ROOT = '../../../'


phase = 'train'


sys.path.insert(0, CAFFE_ROOT + 'python/')
print os.listdir(CAFFE_ROOT + 'python')
import caffe
src_dir = CAFFE_ROOT+'data/fcn_label_full/'
dst_dir = CAFFE_ROOT+'data/'
lmimgDst   = dst_dir + phase +'_imgs_lmdb/'
lmlabelDst = dst_dir + phase + '_labels_lmdb/'
def gen_net(lmdb, batch_size):
     # our version of LeNet: a series of linear and simple nonlinear transformations
     n = caffe.NetSpec()
     n.data, n.label = L.Data(batch_size=batch_size, backend=P.Data.LMDB, source=lmdb,
                              transform_param=dict(scale=1./255), ntop=2)
     return n.to_proto()

def main(args):
     dir_imgs = CAFFE_ROOT+'data/fcn_label_full/' + phase + '_jpg'
     paths_imgs = fs.gen_paths(dir_imgs, fs.filter_is_img)
     
     dir_segm_labels = CAFFE_ROOT + 'data/fcn_label_full/' + phase + '_maps'
     paths_segm_labels = fs.gen_paths(dir_segm_labels)
      
     paths_pairs = fs.fname_pairs(paths_imgs, paths_segm_labels)    
     paths_imgs, paths_segm_labels = map(list, zip(*paths_pairs))
     if not os.path.exists(lmimgDst):
     	print 'lmdb dir not exists,make it'
     	os.makedirs(lmimgDst)
 	if not os.path.exists(lmlabelDst):
 	    print 'lmdb dir not exists,make it'
 	    os.makedirs(lmlabelDst)
     #for a, b in paths_pairs:
     #   print a,b     
     size1 = to_lmdb.imgs_to_lmdb(paths_imgs, lmimgDst, CAFFE_ROOT = CAFFE_ROOT)
     size2 = to_lmdb.matfiles_to_lmdb(paths_segm_labels, lmlabelDst, 'gt',CAFFE_ROOT = CAFFE_ROOT)
     dif = size1 - size2
     dif = dif.sum()
     scipy.io.savemat('./size1',dict({'sz':size1}),appendmat=True)
     scipy.io.savemat('./size2',dict({'sz':size2}),appendmat=True)
     print 'size dif:'+str(dif)
     return 0
 
if __name__ == '__main__':
     
     main(None)
     
     pass
