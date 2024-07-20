# 🌐 firms

[FIRMS](https://firms.modaps.eosdis.nasa.gov): Fire Information for Resource Management System.

map-key: https://firms.modaps.eosdis.nasa.gov/api/map_key/

area api: https://firms.modaps.eosdis.nasa.gov/api/area/

```bash
pip install blue-geo
```

```bash
@datacube query firms_area <object-name> \
	select \
	--source <source> \
	--area <area> \
	--date <date> \
	--depth <depth>

# runs @datacube select query - rm

@datacube query len

@datacube query select \
  <object-name> \
  - \
  --index <index> \
  --prefix <prefix> \
  --suffix <suffix> \
  --contains <contains> \
  --not-contains <not-contains>

@datacube ingest \
  all,items=<item-1+item-2>,suffix=<suffix> \
  <object-name>

blue_geo ingest firms - .
@open QGIS .
@publish tar .
```



🔥

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

```bash
@select firms-$(@@timestamp)
blue_geo ingest firms - .
@open QGIS .
@publish tar .
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