import numpy as np
import matplotlib.pyplot as plt
n1=plt.imread('baidulogo.jpg')
print(type(n1),n1)
plt.imshow(n1)

# n2=np.array([0.299,0.587,0.114])
# x=np.dot(n1,n2)
# gray_image = 0.2989 * x[:, :, 0] + 0.5870 * x[:, :, 1] + 0.1140 * x[:, :, 2]
gray_image = 0.2989 * n1[:, :, 0] + 0.5870 * n1[:, :, 1] + 0.1140 * n1[:, :, 2]
plt.imshow(gray_image,cmap='gray')
plt.show()


