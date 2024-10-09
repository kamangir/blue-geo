# 🌐 SkyFox

the `SkyFox` catalog covers [EDS (Earth Data Store)](https://earthdaily.github.io/EDA-Documentation/). see [datacube](../) for usage instructions.

--urls--

## query

```bash
@catalog query SkyFox help
```
--help-- blue_geo catalog query SkyFox Venus

--include-- ../../watch/targets/md/Leonardo.md case study: Leonardo da Vinci International Airport

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