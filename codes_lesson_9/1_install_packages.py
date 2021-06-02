#You'll probably need to install these packages:
!pip install geopandas 
!pip install rasterio 
!pip install rioxarray

# shapely needs to be reinstalled to use the same geos install as cartopy (https://github.com/SciTools/cartopy/issues/871)
!pip uninstall -y shapely
!pip install --no-binary shapely shapely
!pip install cartopy
