# 🌐 Earth Search by Element 84 (earth-search-aws)

the `Earth Search` catalog covers [Earth Search by Element 84](https://stacindex.org/catalogs/earth-search#/). see [datacube](../) for usage instructions.

--urls--

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
--help-- blue_geo catalog query EarthSearch sentinel_2_l1c

--include-- ../../watch/targets/md/chilcotin-river-landslide.md case study: Chilcotin River Landslide

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