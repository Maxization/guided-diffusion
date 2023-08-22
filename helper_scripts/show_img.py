import numpy as np
from PIL import Image

path = 'E:/samples_20x256x256x3.npz'

npzfile = np.load(path)

images = npzfile['arr_0']

for img_array in images:
  img = Image.fromarray(img_array)
  img.show()
  print('Test!')
