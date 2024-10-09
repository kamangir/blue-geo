# 🌐 copernicus

the `copernicus` catalog covers [Copernicus Data Space Ecosystem - Europe's eyes on Earth](https://dataspace.copernicus.eu/). see [datacube](../) for usage instructions.

--urls--

## ⚠️ issues

⚠️ "Too Many Requests" error likely.

## query

```bash
@catalog query copernicus help
```
--help-- blue_geo catalog query copernicus sentinel_2

--include-- ../../watch/targets/md/chilcotin-river-landslide.md case study: Chilcotin River Landslide

## example run

```bash
@select
@catalog query copernicus sentinel_2 - . \
  --count 10 \
  --datetime 2024-07-30/2024-08-09 \
  --lat  51.83 \
  --lon -122.78

@select $(@catalog query read - . --count 1 --offset 3)
@datacube ingest scope=metadata+rgb .

@publish tar .
```

![image](https://github.com/kamangir/assets/blob/main/blue-geo/chilcotin-query-2024-08-23-v1.png?raw=true)

[datacube-copernicus-sentinel_2-S2A_MSIL1C_20240807T190911_N0511_R056_T10UEC_20240808T002811-SAFE.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/datacube-copernicus-sentinel_2-S2A_MSIL1C_20240807T190911_N0511_R056_T10UEC_20240808T002811-SAFE.tar.gz)

- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-183-53e60268d40e)