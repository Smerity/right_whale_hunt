# The Right Whale Hunt
## Annotated faces for NOAA Right Whale Recognition Kaggle competition

<p align="center">
  <img src="http://i.imgur.com/fqfbBFl.jpg" alt="Moby Dick" width="350px" />
</p>

This repository contains Sloth annotations for extracting whale heads from whale images in the [NOAA Right Whale Recognition Kaggle competition](https://www.kaggle.com/c/noaa-right-whale-recognition).

The initial dataset had 300 images over 11 whales:

    smerity@pegasus:~/Coding/whale_hunt$ find heads/ | grep "jpg" | cut -d '/' -f 2 | sort | uniq -c
         24 whale_08017
         29 whale_24458
         22 whale_26288
         32 whale_28892
         24 whale_34656
         30 whale_36851
         43 whale_38681
         22 whale_48813
         22 whale_48966
         28 whale_51195
         24 whale_52749
         
The new dataset has grown substantially as it has been helped by many!

The data is assumed to be in the `imgs` folder, sorted by identified whale as provided by inversion's [Python script to sort the whale images](https://www.kaggle.com/c/noaa-right-whale-recognition/forums/t/16275/python-script-to-sort-images).

To extract the heads, simply run:

    python extract_tiles_from_sloth.py annotations/*.json

By default this will provide a 256 x 256 image of the head, expanded to be a box. If you woud like to maintain the exact annotation, set `PAD_TO_BOX` to `False`.

![Whale 26288](http://i.imgur.com/o5cf6pd.jpg)

# Contributing to annotations

Whilst no explicit annotation guidelines have yet been formed, the head should capture all of the visible callosity patterns on the whale's head and include the eyes and eyebrow callosities if visible, even if obscured as they're underwater. If in doubt, more is better than less.

If you'd like to provide additional annotation, or augment the annotation yourself, you can do so by using [Sloth](http://sloth.readthedocs.org/en/latest/), a versatile tool for various labeling tasks in the context of computer vision research.

    find imgs/*/* -iname "*.jpg" | shuf | xargs sloth appendfiles annotations/whale_faces_smerity.json
    ln -s annotations/whale_faces_smerity.json .
    sloth --config slothwhales.py whale_faces_smerity.json

Replacing `smerity` with your identifying handle for easy merging. This will allow for easy merging of multiple annotations.

# Thanks to:

+ inversion
+ jfkingiii
+ sunilsu

# License

MIT License, as per `LICENSE`
