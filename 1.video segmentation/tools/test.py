import tensorflow as tf

image = "/remote-home/dzdai/final/DVSNet-master/data/dataset/list/10000.png"
if tf.gfile.Exists(image):
    print(1)
else:
    print(0)