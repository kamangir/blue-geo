# 🧊 datacube

`datacube`s are [objects](https://kamangir-public.s3.ca-central-1.amazonaws.com/giza-v1/giza.pdf) that can be queried in [catalogs](../catalog) and [ingested](#ingesting-a-datacube).

## adding a new datacube class

1️⃣ add the [catalog](../catalog/README.md#adding-a-new-catalog).

2️⃣ clone [blue_geo/catalog/generic/generic](../catalog/generic/generic/) similar to [blue_geo/catalog/copernicus/sentinel_2](../catalog/copernicus/sentinel_2/) and define `NovelDatacube`.

3️⃣ update [blue_geo/catalog/classes.py](../catalog/classes.py).

## ingesting a datacube

run `@datacube ingest` to ingest a [datacube](../datacube/), or use `@catalog query <catalog> <collection> ingest`. 

```bash
@datacube ingest \
    [assets=all|<item-1+item-2>,~copy_template,dryrun,suffix=<suffix>,upload] \
    [.|<datacube-id>] \
    [<args>]
 . ingest <datacube-id>.
 ```