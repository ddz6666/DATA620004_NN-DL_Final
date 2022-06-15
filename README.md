# DATA620004_NN-DL_Final

### 1. video segmentation

任务要求：使用在Cityscapes数据集上开源的任意一个语义分割模型，网络下载一段驾驶视频（类似行车记录仪视频），对视频每一帧进行测试并可视化，结果视频上传至网盘；



本部分DVSNet的实现参考：[XUSean0118/DVSNet: Modified implementation for DVSNet based on Tensorflow (github.com)](https://github.com/XUSean0118/DVSNet)



环境配置：

python版本：2.7

安装所需环境：

```
pip install tensorflow-gpu==1.4.1
pip install opencv-python
pip install Pillow
pip install scipy
```



测试步骤：

1. 将视频按帧分为图片，放在/data/dataset下，将图片的顺序写入1.txt文件放在/data下

2. 下载checkpoint文件并解压放在/checkpoint下

3. 在inference.py所在的文件夹下输入下面的命令进行测试：

   ```
   python inference.py --data_dir="./data/dataset" --data_list="./data/dataset/1.txt" --num_steps=[图片的数量]
   ```

4. 输出的图片会保存在video文件夹中，将图片重新合成为视频。



### 2. object detection

任务要求：对Faster R-CNN模型，分别进行以下训练：a) 随机初始化训练VOC；b) ImageNet预训练backbone网络，然后使用VOC进行fine tune；c)使用coco训练的Mask R-CNN的backbone网络参数，初始化Faster R-CNN的backbone网络，然后使用VOC进行fine tune；



本部分Faster RCNN的实现参考：[bubbliiiing/faster-rcnn-tf2: 这是一个faster-rcnn的tensorflow2实现的库，可以利用voc数据集格式的数据进行训练。 (github.com)](https://github.com/bubbliiiing/faster-rcnn-tf2)



环境配置：

cuda10.1+cudnn7.6.5+tensorflow-gpu2.2.0

```
pip install -r requirements.txt
```



##### 训练步骤：

下载VOC2007数据并在目录下解压：

```
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCdevkit_08-Jun-2007.tar
tar xvf VOCtrainval_06-Nov-2007.tar
tar xvf VOCtest_06-Nov-2007.tar
tar xvf VOCdevkit_08-Jun-2007.tar
```



将voc_annotation.py中的annotation_mode修改为2并运行，生成2007_train.txt和2007_val.txt

```
python voc_annotation.py
```



将预训练权重放在model_data文件夹中，运行train.py开始训练

```
python train.py
```

训练的结果将保存在logs文件夹中



##### 测试步骤：

将frcnn.py中的model_path修改为训练好的权值文件，运行predict.py后输入图片路径进行检测

```
python predict.py
```

