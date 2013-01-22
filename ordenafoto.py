#!/usr/bin/env python2.7

from __future__ import print_function

import sys,os
import pyexiv2
from matplotlib import pylab
import Image as im
import tempfile as tmp

def main():
  rootdir='tmp-source'
  fileList = []
  #rootdir = sys.argv[1]
  for root, subFolders, files in os.walk(rootdir):
      for file in files:
          fileList.append(os.path.join(root,file))
  print (fileList)

  for f in fileList:
    metadata=pyexiv2.ImageMetadata(f)
    metadata.read()
    ims=metadata.previews
    I=Image.frombuffer(ims[-1].data)
    I.show()

  return 0


if __name__ == '__main__':
  main()
