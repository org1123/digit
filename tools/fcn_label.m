clear;
clc;
fig_path =  './figure/';  
img_path_list = dir(strcat(fig_path,'*.jpg'));
len = length(img_path_list);
if(~exist('./fcn_label2/fig/')) mkdir('fcn_label2/fig');end
if(~exist('./fcn_label2/temp/')) mkdir('fcn_label2/temp');end
if(~exist('./fcn_label2/mat/')) mkdir('fcn_label2/mat');end
m=0;
orients = [0,5,-5]; %旋转角度
ratio = 0.5;        
for j = 1:len 
    img_name = img_path_list(j).name; 
    image =  imread(strcat(fig_path,img_name)); 
    image = imresize(image,ratio);
    fprintf('%d %s\n',j,strcat(fig_path,img_name));% 显示正在处理的图像名
    img_name=img_name(1:end-4);
    bbs = load(['./bbs_mat/',img_name,'.mat']);  %load原始bbx
    siz=size(image);
    N=size(bbs.bbs,1);
    gt=zeros(siz(1),siz(2));
    for i = 1:N
        for k=0:N-i                 
            image1=image;
            xmin1=ceil(ratio*bbs.bbs(i,1));  ymin1=ceil(ratio*bbs.bbs(i,2));
            xmax1=ceil(ratio*bbs.bbs(i,3));  ymax1=ceil(ratio*bbs.bbs(i,4));   label1=bbs.bbs(i,5);
            xmin2=ceil(ratio*bbs.bbs(i+k,1));ymin2=ceil(ratio*bbs.bbs(i+k,2));
            xmax2=ceil(ratio*bbs.bbs(i+k,3));ymax2=ceil(ratio*bbs.bbs(i+k,4)); label2=bbs.bbs(i+k,5);
            IO1=image(ymin1:ymax1,xmin1:xmax1,:);
            IO2=image(ymin2:ymax2,xmin2:xmax2,:);
            BBx=bbs.bbs;
            BBx(:,1:4)=ceil(ratio*BBx(:,1:4));
            BBx(i,5)=label2;
            BBx(i+k,5)=label1;
            for o1 = orients
                J1=imrotate(IO1,o1,'bilinear','crop');
                J1=J1(3:end-2,3:end-2,:);
                OUT1=imresize(J1,[ymax2-ymin2+1 xmax2-xmin2+1]); 
                for o2=orients
                    J2=imrotate(IO2,o2,'bilinear','crop');
                    J2=J2(3:end-2,3:end-2,:);
                    OUT2=imresize(J2,[ymax1-ymin1+1 xmax1-xmin1+1]);
                    image1(ymin2:ymax2,xmin2:xmax2,:)=OUT1;
                    image1(ymin1:ymax1,xmin1:xmax1,:)=OUT2;
                    m=m+1;
                    imwrite(image1,['./fcn_label2/fig/',img_name,'-',num2str(m),'.jpg']);
                    save(['./fcn_label2/temp/',img_name,'-',num2str(m),'.mat'],'BBx');
                end
            end
        end
    end    
end
fig_path =  './fcn_label2/fig/';  
img_path_list = dir(strcat(fig_path,'*.jpg'));
len = length(img_path_list);
A = {0,0};
img_path = 'fig/';  mat_path = 'mat/';
for j = 1:len 
    img_name = img_path_list(j).name; 
    image =  imread(strcat(fig_path,img_name));  
    fprintf('%d %s\n',j,strcat(fig_path,img_name));% 显示正在处理的图像名
    img_name=img_name(1:end-4);
    bbs = load(['./fcn_label2/temp/',img_name,'.mat']);
    siz=size(image);
    N=size(bbs.BBx,1);
    gt=ones(siz(1),siz(2));
    gt=10*gt;
    for i = 1:N
        xmin=bbs.BBx(i,1);ymin=bbs.BBx(i,2);xmax=bbs.BBx(i,3);ymax=bbs.BBx(i,4);label=bbs.BBx(i,5);
        gt(ymin+ceil(0.5*(ymax-ymin))-3:ymin+ceil(0.5*(ymax-ymin))+3,xmin+ceil(0.5*(xmax-xmin))-3:xmin+ceil(0.5*(xmax-xmin))+3)=label;
    end
    save(['./fcn_label2/mat/',img_name,'.mat'],'gt');   
    A(end+1,:) = {strcat(img_path,img_name,'.jpg'),strcat(mat_path,img_name,'.mat')};
end
fid=fopen('./fcn_label2/pair.txt','w');
row=size(A,1);
for k=2:row
    fprintf(fid,'%s  %s\r\n',A{k,1},A{k,2});
end
fclose(fid);





