# 🌐 SkyFox

the `SkyFox` catalog covers [EDS (Earth Data Store)](https://earthdaily.github.io/EDA-Documentation/). see [datacube](../) for usage instructions.

--urls--

## query

```bash
 > @catalog query SkyFox help
@catalog query SkyFox \
	[dryrun,Venus,select,upload] \
	[ingest,~copy_template,dryrun,overwrite,upload,scope=all|metadata|quick|raster|<.jp2+.tif+.tiff>] \
	[-|<object-name>] \
	[--bbox <-122.88,51.73,-122.68,51.93>] \
	[--count <10>, -1: all] \
	[--datetime <2024-07-30/2024-08-09>, more: https://documentation.dataspace.copernicus.eu/APIs/STAC.html#search-items-by-datetime] \
	[--keyword <keyword>] \
	[--lat <51.83>] \
	[--lon <-122.78>] \
	[--radius <0.1>]
 . SkyFox/Venus -query-> <object-name>.
```

--include-- ../../watch/targets/Leonardo.md case study: Leonardo da Vinci International Airport

## example run

🔥

```bash
@select
@catalog query SkyFox Venus - . \
  --count 10 \
  --datetime 2019-12-13/2020-10-28 \
  --lat  41.8003 \
  --lon 12.2389

@select $(@catalog query read - . --count 1 --offset 3)
@datacube ingest scope=metadata+quick .

@publish tar .
```

![image](...)

[....tar.gz](...)

- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-234-7ffa6d34230b)