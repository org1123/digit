img_root = '../../data/fcn_label_small0/fig/';
save_root = '../../data/fcn_label_small1/fig/';
img_list = dir([img_root, '*.jpg']);
img_list = {img_list.name};
for i = 1:length(img_list)
    img_name = img_list{i};
    img_path = [img_root, img_name];
    im = imread(img_path);
    im2 = imresize(im, [ceil(size(im,1)/2), ceil(size(im,2)/2)]);
    
end