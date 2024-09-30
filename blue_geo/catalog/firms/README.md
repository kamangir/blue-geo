# 🌐 firms

the `firms` catalog covers [FIRMS](https://firms.modaps.eosdis.nasa.gov): Fire Information for Resource Management System. see [datacube](../) for usage instructions.

 - [area](https://firms.modaps.eosdis.nasa.gov/api/area/)
 - [home](https://firms.modaps.eosdis.nasa.gov/)
 - [map key](https://firms.modaps.eosdis.nasa.gov/api/map_key/)

## query

```bash
@catalog query firms help
```
```bash
@catalog query firms \
	[dryrun,area,select,upload] \
	[ingest,~copy_template,dryrun,overwrite,scope=<scope>,upload] \
	[-|<object-name>] \
	[--area east|north|south|west|world] \
	[--date <yyyy-mm-dd>] \
	[--depth 1..10] \
	[--source LANDSAT_NRT|MODIS_NRT|MODIS_SP|VIIRS_NOAA20_NRT|VIIRS_NOAA21_NRT|VIIRS_SNPP_NRT|VIIRS_SNPP_SP]
 . firms/area -query-> <object-name>.
   scope: @datacube ingest help.
```

## example use

```bash
@catalog query firms area,select ingest - \
	--date 2024-07-20

@open QGIS .
@publish tar .
```

```yaml
datacube:
  area: WORLD
  date: '2024-07-24'
  depth: 1
  id: datacube-firms-area-world-MODIS_NRT-2024-07-24-1
  len: 28543
  source: MODIS_NRT
```


![image](https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/datacube-firms_area-ingest.png)

[datacube-firms-area-world-MODIS_NRT-2024-07-24-1.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/datacube-firms-area-world-MODIS_NRT-2024-07-24-1.tar.gz)

![image](https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/datacube-firms_area.jpg)

---

map-key: https://firms.modaps.eosdis.nasa.gov/api/map_key/

area api: https://firms.modaps.eosdis.nasa.gov/api/area/

