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
# Try to expand any rectangular crops into squares
PAD_TO_BOX = True

# Load the JSON annotations
for json_fn in sys.argv[1:]:
  annotations = json.loads(open(json_fn).read())
  for data in annotations:
    fn = data['filename']
    # Fix any filenames that start with '../imgs/'
    fn = fn[3:] if fn.startswith('../') else fn
    print 'Processing {}'.format(fn)
    if data['annotations']:
      # We're only interested in the Head annotations
      points = [x for x in data['annotations'] if x['class'] == 'Head']
      if not points:
        continue
      points = points[0]
      print 'Processing {}'.format(fn)
      ###
      pw, ph = points['width'], points['height']
      if PAD_TO_BOX:
        # FIX: Off by one sometimes results in white on bottom or right edge
        jumpw, jumph = 0, 0
        if pw > ph:
          jumph = int(math.ceil((pw - ph) / 2))
        else:
          jumpw = int(math.ceil((ph - pw) / 2))
        left, upper = points['x'] - jumpw, points['y'] - jumph
        right, lower = points['x'] + pw + jumpw, points['y'] + ph + jumph
      else:
        left, upper = points['x'], points['y']
        right, lower = points['x'] + pw, points['y'] + ph
      box = map(int, [left, upper, right, lower])
      im = Image.open(fn)
      region = im.crop(box)
      region.thumbnail((mw, mh), Image.ANTIALIAS)
      ###
      # Paste the image centered into the given box
      old_width, old_height = region.size
      x1 = int(math.ceil(math.ceil((mw - old_width) / 2)))
      y1 = int(math.ceil(math.ceil((mh - old_height) / 2)))
      new_background = (255, 255, 255)
      cropped = Image.new(region.mode, (mw, mh), new_background)
      cropped.paste(region, (x1, y1, x1 + old_width, y1 + old_height))
      ###
      outfn = fn.replace('imgs', 'heads')
      ensure_dir(outfn)
      cropped.save(outfn)
