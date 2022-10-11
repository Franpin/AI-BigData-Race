#task1_2.py
import tensorflow as tf
import sys
import sklearn
import cv2
print(sys.version)
print(tf.__version__)
print("Sklearn verion is {}".format(sklearn.__version__))
print(cv2.__version__)
vec_1=tf.constant([1,2,2,1])
vec_2=tf.constant([7,8,9,9])
ver_add=tf.add(vec_1,vec_2)
print(ver_add)