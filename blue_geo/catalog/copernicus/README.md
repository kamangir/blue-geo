# 🌐 copernicus

the `copernicus` catalog covers [Copernicus Data Space Ecosystem - Europe's eyes on Earth](https://dataspace.copernicus.eu/). see [datacube](../) for usage instructions.

## query

```bash
 > @catalog query copernicus help
@catalog query copernicus \
	[dryrun,sentinel_2,select,upload] \
	[ingest,assets=all|<item-1+item-2>,~copy_template,dryrun,suffix=<suffix>,upload] \
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

```
@catalog query copernicus \
	sentinel_2,select \
	ingest,metadata - \
	--count 20 \
	--datetime 2024-07-30/2024-08-15 \
	--lat 51.83 \
	--lon -122.78
```

also see:

- [Chilcotin River Landslide](./sentinel_2/chilcotin_river_landslide.md)
