# 🌐 SkyFox

the `SkyFox` catalog covers ...


[Copernicus Data Space Ecosystem - Europe's eyes on Earth](https://dataspace.copernicus.eu/). see [datacube](../) for usage instructions.

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

## case study: Leonardo da Vinci International Airport

- [ ] add example image 🔥

background:
- [Wikipedia](https://en.wikipedia.org/wiki/Rome_Fiumicino_Airport): "the 9th busiest airport in Europe and the world's 46th-busiest airport with over 40.5 million passengers served in 2023."

- [Google Map](https://maps.app.goo.gl/Zpnj53kVcQQ4fNA17): `lat: 41.8003°N`, `lon: 12.2389° E`.

details: [targets.yaml](../targets.yaml).


using [Leonardo](../../watch/targets/Leonardo.md).

## example run

🔥

```bash
@select
@catalog query SkyFox Venus - . \
  --count 10 \
  --datetime 2024-07-30/2024-08-09 \
  --lat  51.83 \
  --lon -122.78

@select $(@catalog query read - . --count 1 --offset 3)
@datacube ingest scope=metadata+quick .

@publish tar .
```

![image](...)

[....tar.gz](...)

- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-234-7ffa6d34230b)
