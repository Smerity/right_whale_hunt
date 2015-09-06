import json
import math
import os
import sys
###
from PIL import Image

def ensure_dir(fn):
  d = os.path.dirname(fn)
  if not os.path.exists(d):
    os.makedirs(d)

# The output image's width and height
mw, mh = 256, 256

# Load the JSON annotations
annotations = json.loads(open(sys.argv[1]).read())
for data in annotations:
  fn = data['filename']
  print 'Processing {}'.format(fn)
  if data['annotations']:
    # We're only interested in the Head annotations
    points = [x for x in data['annotations'] if x['class'] == 'Head']
    if not points:
      continue
    points = points[0]
    left, upper = points['x'], points['y']
    right, lower = points['x'] + points['width'], points['y'] + points['height']
    box = map(int, [left, upper, right, lower])
    im = Image.open(fn)
    region = im.crop(box)
    region.thumbnail((mw, mh), Image.ANTIALIAS)
    ###
    # Paste the image centered into the given box
    old_width, old_height = region.size
    x1 = int(math.floor((mw - old_width) / 2))
    y1 = int(math.floor((mh - old_height) / 2))
    new_background = (255, 255, 255)
    cropped = Image.new(region.mode, (mw, mh), new_background)
    cropped.paste(region, (x1, y1, x1 + old_width, y1 + old_height))
    ###
    outfn = fn.replace('imgs', 'heads')
    ensure_dir(outfn)
    cropped.save(outfn)
