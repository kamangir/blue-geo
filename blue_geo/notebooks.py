import folium
import geopandas as gpd
from IPython.display import display


def show_on_map(
    gdf: gpd.GeoDataFrame,
    zoom_start: int = 12,
):
    if gdf.empty:
        return

    map = folium.Map(
        location=gdf.unary_union.centroid.coords[0][::-1],
        zoom_start=zoom_start,
    )
    folium.GeoJson(gdf).add_to(map)

    display(map)
