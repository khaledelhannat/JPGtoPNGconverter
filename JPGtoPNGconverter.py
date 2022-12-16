# Enter the name of the Python file first,
# followed by the folder where the images need to be converted,
# and finally the folder name where you want the converted images to be placed.

import sys
import os
from PIL import Image
from pathlib import Path

first = sys.argv[1]
second = sys.argv[2]

dir_path1 = 'D:\Career\My_Projects\image-playground\\' + first
isExist1 = os.path.exists(dir_path1)

if isExist1:

    dir_path2 = 'D:\Career\My_Projects\image-playground\\' + second
    isExist2 = os.path.exists(dir_path2)

    if not isExist2:
        parent_dir = 'D:\Career\My_Projects\image-playground'
        directory = second
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)

    for item in os.scandir('D:\Career\My_Projects\image-playground\\' + first):
        # img = Image.open(os.path.splitext(item)[0] + os.path.splitext(item)[1])
        img = Image.open(os.path.dirname(item) + ('\\') + os.path.basename(item))
        img.save('D:\Career\My_Projects\image-playground\\'+ second + ('\\') + Path(item).stem + '.png')
        print('all done!')

else:
    print('Please enter a valid or already-existing folder name.')