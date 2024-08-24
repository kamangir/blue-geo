# Chilcotin River Landslide

![image](https://github.com/kamangir/assets/blob/main/blue-geo/chilcotin-river-landslide-2.jpg?raw=true)

objective: review of before and after views of the Chilcotin River landslide on Sentinel-2.

background:
- [Chilcotin River Landslide Information Portal](https://chilcotin-river-landslide-2024-bcgov03.hub.arcgis.com/) - source of ⬆️ image.
- [Google Map](https://maps.app.goo.gl/WHTNCDsFNoZAAnzX8): `lat: 51°50'51.1"N`, `lon: 122°47'06.8"W`.
- [Chilcotin River’s Landslide Lake Begins Draining](https://www.bluemarble.nasa.gov/images/153195/chilcotin-rivers-landslide-lake-begins-draining)
- [Reddit: Before and after satellite images of the Chilcotin River landslide](https://www.reddit.com/r/britishcolumbia/comments/1eh9eql/before_and_after_satellite_images_of_the/)


```yaml
toi:
    - from: 2024-07-30
    - to: 2024-08-09
aoi: 
    - lat: 51.83
    - lon: -122.78
```

```bash
@catalog query copernicus \
  ingest,select - \
  sentinel_2,suffix=TCI.jp2 \
  --lat 51.83 \
  --lon -122.78 \
  --datetime 2024-07-30/2024-08-15 \
  --limit 20

@open QGIS .
```

help += https://documentation.dataspace.copernicus.eu/APIs/STAC.html#search-items-by-datetime 🔥

:fire object

🔥