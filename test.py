import numpy as np

zoom_factor = 1
width , height  = 216 , 216

n_width = width * zoom_factor
n_height = height * zoom_factor

x = np.arange(n_width)
y = np.arange(n_height)
# print(x)
# print(y)

xv,yv = np.meshgrid(x,y)
print(xv)
# print(yv)