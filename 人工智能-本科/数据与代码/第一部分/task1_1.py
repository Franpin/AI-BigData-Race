#task1_1.py
import torch
import sys
import sklearn
print(sys.version)
print(torch.__version__)
print("Sklearn verion is {}".format(sklearn.__version__))

x1 = torch.zeros(3, 4)
print("x1 :",x1)
y1 = torch.rand(3, 4)
print("y1 : ", y1)
print("x1 + y1 :", x1 + y1)