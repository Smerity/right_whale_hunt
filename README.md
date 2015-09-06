# The Right Whale Hunt
## Annotated faces for NOAA Right Whale Recognition Kaggle competition

![Right Whale Hunt](http://i.imgur.com/RuINg4m.jpg)

This repository contains Sloth annotations for extracting whale heads from whale images in the [NOAA Right Whale Recognition Kaggle competition](https://www.kaggle.com/c/noaa-right-whale-recognition).

The initial dataset has 300 images over 11 whales:

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

The data is assumed to be in the `imgs` folder, sorted by identified whale as provided by inversion's [Python script to sort the whale images](https://www.kaggle.com/c/noaa-right-whale-recognition/forums/t/16275/python-script-to-sort-images).

To extract the heads, simply run:

    python extract_tiles_from_sloth.py annotated_whales.json

By default this will provide a 256 x 256 image of the head.

![Whale 26288](http://i.imgur.com/o5cf6pd.jpg)

# Contributing to annotations

If you'd like to provide additional annotation, or augment the annotation yourself, you can do so by using [Sloth](http://sloth.readthedocs.org/en/latest/), a versatile tool for various labeling tasks in the context of computer vision research.

    sloth --config slothwhales.py annotated_whales.json

Whilst no explicit annotation guidelines were used, the head should capture all of the visible callosity patterns on the whale's head and include the eyes and eyebrow callosities if visible. If in doubt, more is better advised than less.

# License

MIT License, as per `LICENSE`
