# 🌐 firms-area

the `firms-area` catalog covers [FIRMS](https://firms.modaps.eosdis.nasa.gov): Fire Information for Resource Management System. see [datacube](../README.md) for usage instructions.

## query

```bash
 > @datacube query firms_area help
@datacube query firms_area \
	[download,ingest,select,upload] \
	[-|<object-name>] \
	[dryrun] \
	[--date 2024-07-21] \
	[--depth 1] \
	[--area east|north|south|west|world] \
	[--source LANDSAT_NRT|MODIS_NRT|MODIS_SP|VIIRS_NOAA20_NRT|VIIRS_NOAA21_NRT|VIIRS_SNPP_NRT|VIIRS_SNPP_SP] \
	[--log 1]
 . firms_area -query-> <object-name>.
```

## example use

```bash
@datacube query firms_area \
  ingest,select - - \
  --date 2024-07-18

@open QGIS .
@publish tar .
```

```yaml
datacube:
  area: WORLD
  date: '2024-07-18'
  depth: 1
  id: datacube-firms_area-world-MODIS_NRT-2024-07-18-1
  len: 23627
  source: MODIS_NRT
```


![image](https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/datacube-firms_area-ingest.png)

[datacube-firms_area-world-MODIS_NRT-2024-07-18-1.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/datacube-firms_area-world-MODIS_NRT-2024-07-18-1.tar.gz)

![image](https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/datacube-firms_area.jpg)

---

map-key: https://firms.modaps.eosdis.nasa.gov/api/map_key/

area api: https://firms.modaps.eosdis.nasa.gov/api/area/
