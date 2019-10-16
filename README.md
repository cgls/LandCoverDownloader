# LandCoverDownloader
Download the landcover tiles

The code was created to download easily the Land Cover tiles from https://land.copernicus.eu/global/products/lc


Copy both the files in a folder and run "LCDownloader.py" using python 3.
All the Tiles will be downloaded and unzipped.

Running "LC_reorder.py", all the tiles will be rearranged in sub-folders according to the main topics:

* Discrete
* Classes: 'urban', 'tree', 'shrub', 'moss', 'grass', 'bare', 'crops', 'forest', 'water-seasonal', 'water-permanent', 'snow'
