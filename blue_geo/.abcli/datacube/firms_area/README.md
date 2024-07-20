# 🌐 firms

[FIRMS](https://firms.modaps.eosdis.nasa.gov): Fire Information for Resource Management System.

map-key: https://firms.modaps.eosdis.nasa.gov/api/map_key/

area api: https://firms.modaps.eosdis.nasa.gov/api/area/

```bash
pip install blue-geo
```

```bash
@select firms-query-$(@@timestamp)
@datacube query firms_area . ingest,select
@open QGIS .
@publish tar .
```

TODO: consume and refactor 🔥

```bash
 > blue_geo ingest firms \
	[dryrun,~upload] \
	[.|<object-name>] \
	[--date 2024-07-16] \
	[--depth 1] \
	[--area east|north|south|west|world] \
	[--source LANDSAT_NRT|MODIS_NRT|MODIS_SP|VIIRS_NOAA20_NRT|VIIRS_NOAA21_NRT|VIIRS_SNPP_NRT|VIIRS_SNPP_SP] \
	[--log 1]
 . firms -ingest-> <object-name>.
```


```yaml
datacube:
  area: WORLD
  date: '2024-07-14'
  depth: 1
  id: blue-geo-firms-world-MODIS_NRT
  len: 17105
  source: MODIS_NRT
```

![image](https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/firms-ingest.png)

[firms-2024-07-19-26884.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/firms-2024-07-19-26884.tar.gz)

![image](https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/firms.jpg)