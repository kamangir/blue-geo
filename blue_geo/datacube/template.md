# 🧊 datacube

`datacube`s are items from [collections in catalogs](../catalog/) that are represented by children of [`GenericDatacube`](../../catalog/generic/datacube.py) and can be [ingested](#ingesting-a-datacube) as 🌀 [objects](https://github.com/kamangir/blue-objects).

`datacube`s are generalized [STAC](https://stacspec.org/en/tutorials/intro-to-stac/) Items.

to add a new datacube class follow [these instructions](../doc/adding-catalogs-and-datacubes.md).

## ingesting a datacube

run `@datacube ingest`  or use [`@catalog query <catalog> <collection> ingest`](../catalog/). 

```bash
@datacube ingest help
```
--help-- blue_geo datacube ingest