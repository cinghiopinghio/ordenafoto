#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys,os
import pyexiv2
from matplotlib import pylab
import Image as im
import tempfile as tmp
import mimetypes

class Photo:
  'store photo data: path, date, preview...'
  def __init__(self,path):
    self.path = path
    metadata=pyexiv2.ImageMetadata(self.path)
    metadata.read()
    ims=metadata.previews
    if len (ims) > 0:
      self.thumb = ims[-1]
    else:
      self.thumb = pyexiv2.Preview
      #self.thumb.mime_type = None
  def __repr__(self):
    return self.path
  def __str__(self):
    return self.path

  #def preview(self):


def get_photo_list(rootdir):
  fileList = []
  #rootdir = sys.argv[1]
  for root, subFolders, files in os.walk(rootdir):
    for file in files:
      longfname = os.path.join(root,file)
      mime = mimetypes.guess_type(longfname)[0]
      if mime is not None:
        mime = mime.split('/')[0]
        if mime == 'image':
          fileList.append(Photo(longfname))
  return fileList

def main():
  rootdir='tmp-source'
  fileList = get_photo_list(rootdir)

  for f in fileList:
    print (f)
    #f.preview()
    print (f.thumb.mime_type)


if __name__ == '__main__':
  main()
