###Digit Recognition via CNN
![](http://7xn7wz.com1.z0.glb.clouddn.com/digit.jpg)  
####to train:
* download our [**dataset**](http://o7zt4a6os.bkt.clouddn.com/digit_data.zip) and put it into `data/`;
* run `examples/fdigit/convert.py` for converting data into lmdb
* run solve.py to start training

####to test:
* download pre-trained [**model**](http://7xocv2.dl1.z0.glb.clouddn.com/digit_iter_5000.caffemodel) or train your own model as metioned above.
* run `examples/fdigit/test_fcn11_full.m` (need Matlab and matcaffe)
* python bindings are on the go.

Code base on [*caffe*](http://caffe.berkeleyvision.org/)  

***  

Mail: <jy9387@outlook.com> Page: <http://jy9387.github.io>
or Mail: <zhaok.shu@gmail.com> Page: <http://zhaok.xyz>