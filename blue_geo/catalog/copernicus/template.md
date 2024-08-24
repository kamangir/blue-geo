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

--include-- ../../watch/targets/chilcotin-river-landslide.md case study: Chilcotin River Landslide

## example run

```bash
@select chilcotin-query-2024-08-23-v1
@catalog query copernicus sentinel_2 ingest . \
  --count 10 \
  --datetime 2024-07-30/2024-08-09 \
  --lat  51.83 \
  --lon -122.78

@select $(@catalog query read - . --count 1 --offset 3)
@datacube ingest what=quick .
@publish tar .
```

![image](https://github.com/kamangir/assets/blob/main/blue-geo/chilcotin-query-2024-08-23-v1.png?raw=true)

[datacube-copernicus-sentinel_2-S2A_MSIL1C_20240807T190911_N0511_R056_T10UEC_20240808T002811-SAFE.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/datacube-copernicus-sentinel_2-S2A_MSIL1C_20240807T190911_N0511_R056_T10UEC_20240808T002811-SAFE.tar.gz)

more: [1](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-183-53e60268d40e)