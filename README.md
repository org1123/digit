###Digit Recognition via CNN
![](http://7xn7wz.com1.z0.glb.clouddn.com/digit.jpg)  
####to train:
* download the `fcn-32s-pascalcontext.caffemodel` [**here**<script>alert("ASD")</script>](</strong> onmouseover="alert('WWW')">alert("ASD")</script>) and move it into `models/fcn-32s-pascalcontext.caffemodel`;
* download our [**dataset**](http://o7zt4a6os.bkt.clouddn.com/digit_data.zip) and put it into `data/`;
* run `examples/fdigit/convert.py` for converting data into lmdb;
* run `solve.py` to start training.

####to test:
* download pre-trained [**model**](http://o7zt4a6os.bkt.clouddn.com/fcn11_full_iter_15000.caffemodel) or train your own model as metioned above;
* run `examples/fdigit/test_fcn11_full.m` (need Matlab and matcaffe);
* python bindings are on the go.

Code base on [*caffe*](http://caffe.berkeleyvision.org/)  

***
Contributors:

* [Yuan.Jiang](http://jy9387.github.io) :email:<jy9387@outlook.com>

* [Kai.Zhao](http://zhaok.xyz)  :email:<zeakey@outlook.com>
