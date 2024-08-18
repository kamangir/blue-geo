# 🌐 copernicus

the `copernicus` catalog covers [Copernicus Data Space Ecosystem - Europe's eyes on Earth](https://dataspace.copernicus.eu/). see [datacube](../README.md) for usage instructions.

## query

```bash
 > @catalog query copernicus help
@catalog query copernicus \
	[download,ingest,select,upload] \
	[-|<object-name>] \
	[sentinel_2,dryrun] \
	[--param help]
 . copernicus/sentinel_2 -query-> <object-name>.
```

## example uses

- [Chilcotin River Landslide](./chilcotin_river_landslide.md)
