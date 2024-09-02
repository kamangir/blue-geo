# 🌐 Earth Search

the `Earth Search` catalog covers [Earth Search by Element 84](https://stacindex.org/catalogs/earth-search#/). see [datacube](../) for usage instructions.


## query

```bash
 > @catalog query EarthSearch help

🔥

```

--include-- ../../watch/targets/chilcotin-river-landslide.md case study: Chilcotin River Landslide

## example run

```bash
@select chilcotin-query-2024-08-23-v1
@catalog query EarthSearch sentinel_2_l1c ingest . \
  --count 10 \
  --datetime 2024-07-30/2024-08-09 \
  --lat  51.83 \
  --lon -122.78

@select $(@catalog query read - . --count 1 --offset 3)
@datacube ingest what=quick .
@publish tar .
```

![image](https://github.com/kamangir/assets/blob/main/blue-geo/TBA.png?raw=true)

[datacube-EarthSearch-sentinel_2_l1c-TBA.tar.gz](TBA)

- [dev notes](TBA)