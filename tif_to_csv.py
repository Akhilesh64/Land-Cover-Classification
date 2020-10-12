#This script requires raster2xyz python library to run
#pip install raster2xyz

from raster2xyz.raster2xyz import Raster2xyz
import os
from glob import glob

for infile in glob(os.getcwd() + '\*.tif'):
    file, ext1 = os.path.splitext(infile)
    rtxyz = Raster2xyz()
    rtxyz.translate(infile, file+'.csv')

