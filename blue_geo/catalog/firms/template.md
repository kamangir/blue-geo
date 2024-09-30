# 🌐 firms

the `firms` catalog covers [FIRMS](https://firms.modaps.eosdis.nasa.gov): Fire Information for Resource Management System. see [datacube](../) for usage instructions.

--urls--

## query

```bash
@catalog query firms help
```
--help-- blue_geo catalog query firms area

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
