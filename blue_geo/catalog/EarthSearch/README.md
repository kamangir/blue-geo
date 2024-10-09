# 🌐 Earth Search by Element 84 (earth-search-aws)

the `Earth Search` catalog covers [Earth Search by Element 84](https://stacindex.org/catalogs/earth-search#/). see [datacube](../) for usage instructions.

 - [api](https://earth-search.aws.element84.com/v1/)
 - [sentinel 2 on aws open data](https://registry.opendata.aws/sentinel-2/)
 - [stac api info](https://stacindex.org/catalogs/earth-search#/)
 - [ui](https://viewer.aws.element84.com/)

## ⚠️ issues

⚠️ some L1C datacubes carry only L2A assets, example: `datacube-EarthSearch-sentinel_2_l1c-S2A_10UDV_20221109_0_L1C`.

to validate, type in,

```bash
@select datacube-EarthSearch-sentinel_2_l1c-S2A_10UDV_20221109_0_L1C
@datacube get raw .
@datacube list . --scope all
```

notice that `all` returns zero items, because no asset starts with the expected prefix `s3://sentinel-s2-l1c/tiles`. instead, there are many assets with the prefix `s3://sentinel-s2-l2a/tiles` - [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-252-2118326b1de2).

## query

```bash
@catalog query EarthSearch help
```
```bash
@catalog query EarthSearch \
	[dryrun,sentinel_2_l1c,select,upload] \
	[ingest,~copy_template,dryrun,overwrite,scope=<scope>,upload] \
	[-|<object-name>] \
	[--bbox <-122.88,51.73,-122.68,51.93>] \
	[--count <10>, -1: all] \
	[--datetime <2024-07-30/2024-08-09>, more: https://documentation.dataspace.copernicus.eu/APIs/STAC.html#search-items-by-datetime] \
	[--keyword <keyword>] \
	[--lat <51.83>] \
	[--lon <-122.78>] \
	[--radius <0.1>]
 . EarthSearch/sentinel_2_l1c -query-> <object-name>.
   scope: @datacube ingest help.
```

## case study: Chilcotin River Landslide

![image](https://github.com/kamangir/assets/blob/main/blue-geo/chilcotin-river-landslide-2.jpg?raw=true)

 - [Google Maps](https://maps.app.goo.gl/WHTNCDsFNoZAAnzX8): `lat: 51.8472"N`, `lon: 122.7903"W`.
 - [Nasa](https://www.bluemarble.nasa.gov/images/153195/chilcotin-rivers-landslide-lake-begins-draining): Chilcotin River’s Landslide Lake Begins Draining.
 - [Reddit](https://www.reddit.com/r/britishcolumbia/comments/1eh9eql/before_and_after_satellite_images_of_the/): Before and after satellite images of the Chilcotin River landslide.
 - [portal](https://chilcotin-river-landslide-2024-bcgov03.hub.arcgis.com/): Chilcotin River Landslide Information Portal, source of ⬆️ image.

---


using [chilcotin-river-landslide](../../watch/targets/md/chilcotin-river-landslide.md).

## example run

```bash
@select
@catalog query EarthSearch sentinel_2_l1c - . \
  --count 10 \
  --datetime 2024-07-30/2024-08-09 \
  --lat  51.83 \
  --lon -122.78

@select $(@catalog query read - . --count 1 --offset 3)
@datacube ingest scope=metadata+rgbx .
@publish tar .
```

![image](https://github.com/kamangir/assets/blob/main/blue-geo/datacube-EarthSearch-sentinel_2_l1c-S2A_10UEC_20240807_0_L1C.png?raw=true)

[datacube-EarthSearch-sentinel_2_l1c-S2A_10UEC_20240807_0_L1C.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/datacube-EarthSearch-sentinel_2_l1c-S2A_10UEC_20240807_0_L1C.tar.gz)

- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-204-f86ea5434630)
