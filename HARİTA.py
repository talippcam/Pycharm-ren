import geopandas as gpd
import matplotlib.pyplot as plt

# Türkiye shapefile veya GeoJSON dosyasını yükle
turkiye = gpd.read_file("tr.json")

# Haritayı çiz
turkiye.plot()
plt.show()