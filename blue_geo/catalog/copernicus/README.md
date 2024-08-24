# 🌐 copernicus

the `copernicus` catalog covers [Copernicus Data Space Ecosystem - Europe's eyes on Earth](https://dataspace.copernicus.eu/). see [datacube](../) for usage instructions.

## query

```bash
 > @catalog query copernicus help
@catalog query copernicus \
	[dryrun,sentinel_2,select,upload] \
	[ingest,~copy_template,dryrun,overwrite,upload,what=all|metadata|quick|<suffix>] \
	[-|<object-name>] \
	[--bbox <-122.88,51.73,-122.68,51.93>]\
	[--count <10>, -1: all]\
	[--datetime <2024-07-30/2024-08-09>]\
	[--lat <51.83>]\
	[--lon <-122.78>]\
	[--radius <0.1>]
 . copernicus/sentinel_2 -query-> <object-name>.
```

## example use

```bash
@catalog query copernicus \
	sentinel_2,select \
	ingest - \
	--count 1 \
	--datetime 2024-07-30/2024-08-15 \
	--lat 51.83 \
	--lon -122.78

@publish tar .
```

[datacube-copernicus-sentinel_2-S2A_MSIL1C_20240731T191911_N0511_R099_T10UDC_20240801T003519-SAFE.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/datacube-copernicus-sentinel_2-S2A_MSIL1C_20240731T191911_N0511_R099_T10UDC_20240801T003519-SAFE.tar.gz)

also see:

- [Chilcotin River Landslide](./sentinel_2/chilcotin_river_landslide.md)