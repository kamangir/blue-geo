# 🌐 SkyFox

the `SkyFox` catalog covers [EDS (Earth Data Store)](https://earthdaily.github.io/EDA-Documentation/). see [datacube](../) for usage instructions.

 - [keyword](url)

## query

```bash
@catalog query SkyFox help
```
```bash
@catalog query SkyFox \
	[dryrun,Venus,select,upload] \
	[ingest,~copy_template,dryrun,overwrite,scope=<scope>,upload] \
	[-|<object-name>] \
	[--arg <value>]
 . SkyFox/Venus -query-> <object-name>.
   scope: @datacube ingest help.
```

## case study: Leonardo da Vinci International Airport

![image](https://github.com/kamangir/assets/blob/main/blue-geo/Leonardo.png?raw=true)

 - [Google Maps](https://maps.app.goo.gl/Zpnj53kVcQQ4fNA17): `lat: 41.8150"N`, `lon: 12.2550"E`.
 - [Wikipedia](https://en.wikipedia.org/wiki/Rome_Fiumicino_Airport): The 9th busiest airport in Europe and the world's 46th-busiest airport with over 40.5 million passengers served in 2023.

---


using [Leonardo](../../watch/targets/md/Leonardo.md).

## example run

```bash
@select
@catalog query SkyFox Venus - . \
  --count 10 \
  --datetime 2019-12-13/2020-10-28 \
  --lat  41.8003 \
  --lon 12.2389

@select $(@catalog query read - . --count 1 --offset 3)
@datacube ingest scope=metadata+rgbx .
@datacube generate - . \
	--modality rgb
```

- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-234-7ffa6d34230b)
