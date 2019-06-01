# -*- coding: utf-8 -*-
"""
@author: vee_nits123
"""

import shutil
import os
from tqdm import tqdm

#file path
source = "C:\\Users\\D\\Desktop\\cell_images\Parasitized"
#destination path
dest1 = "C:\\Users\\D\\Desktop\\cell_images\\Parasitized_Test"

import math
files = os.listdir(source)
# list all

split = 0.70
mark = math.floor(split * len(files))

for f in tqdm(files[mark:]):
        shutil.move(source+"\\"+f, dest1)
#ceil & floor
