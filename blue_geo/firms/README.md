# 🌐 firms

[FIRMS](https://firms.modaps.eosdis.nasa.gov): Fire Information for Resource Management System.

map-key: https://firms.modaps.eosdis.nasa.gov/api/map_key/

area api: https://firms.modaps.eosdis.nasa.gov/api/area/

```bash
pip install blue-geo
```

```bash
 > blue_geo ingest firms \
	[dryrun,~upload] \
	[.|<object-name>] \
	[--date 2024-07-16] \
	[depth 1] \
	[--area east|north|south|west|world] \
	[--source LANDSAT_NRT|MODIS_NRT|MODIS_SP|VIIRS_NOAA20_NRT|VIIRS_NOAA21_NRT|VIIRS_SNPP_NRT|VIIRS_SNPP_SP] \
	[--log 1]
 . firms -ingest-> <object-name>.
```