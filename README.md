# DATA620004_NN-DL_Final

### 1. video segmentation

使用在Cityscapes数据集上开源的任意一个语义分割模型，网络下载一段驾驶视频（类似行车记录仪视频），对视频每一帧进行测试并可视化，结果视频上传至网盘；



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