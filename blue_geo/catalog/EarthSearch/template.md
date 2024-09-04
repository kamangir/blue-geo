# 🌐 Earth Search by Element 84 (earth-search-aws)

the `Earth Search` catalog covers [Earth Search by Element 84](https://stacindex.org/catalogs/earth-search#/). see [datacube](../) for usage instructions.

- https://registry.opendata.aws/sentinel-2/
- https://viewer.aws.element84.com/

## query

```bash
 > @catalog query EarthSearch help
@catalog query EarthSearch \
	[dryrun,sentinel_2_l1c,select,upload] \
	[ingest,~copy_template,dryrun,overwrite,upload,scope=all|metadata|quick|raster|<.jp2+.tif+.tiff>] \
	[-|<object-name>] \
	[--bbox <-122.88,51.73,-122.68,51.93>] \
	[--count <10>, -1: all] \
	[--datetime <2024-07-30/2024-08-09>, more: https://documentation.dataspace.copernicus.eu/APIs/STAC.html#search-items-by-datetime] \
	[--keyword <keyword>] \
	[--lat <51.83>] \
	[--lon <-122.78>] \
	[--radius <0.1>]
 . EarthSearch/sentinel_2_l1c -query-> <object-name>.
```

--include-- ../../watch/targets/chilcotin-river-landslide.md case study: Chilcotin River Landslide

## example run

```bash
@select
@catalog query EarthSearch sentinel_2_l1c - . \
  --count 10 \
  --datetime 2024-07-30/2024-08-09 \
  --lat  51.83 \
  --lon -122.78

@select $(@catalog query read - . --count 1 --offset 3)
@datacube ingest scope=metadata+quick .
@publish tar .
```

![image](https://github.com/kamangir/assets/blob/main/blue-geo/datacube-EarthSearch-sentinel_2_l1c-S2A_10UEC_20240807_0_L1C.png?raw=true)

[datacube-EarthSearch-sentinel_2_l1c-S2A_10UEC_20240807_0_L1C.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/datacube-EarthSearch-sentinel_2_l1c-S2A_10UEC_20240807_0_L1C.tar.gz)

- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-204-f86ea5434630)