# 🧊 datacube

`datacube`s are items from [collections in catalogs](../catalog/) that are represented by children of [`GenericDatacube`](../../catalog/generic/datacube.py) and can be [ingested](#ingesting-a-datacube) as 🌀 [objects](https://github.com/kamangir/blue-objects).

`datacube`s are generalized [STAC](https://stacspec.org/en/tutorials/intro-to-stac/) Items.

to add a new datacube class follow [these instructions](../doc/adding-catalogs-and-datacubes.md).

## ingesting a datacube

run `@datacube ingest`  or use [`@catalog query <catalog> <collection> ingest`](../catalog/). 

```bash
@datacube ingest help
```
```bash
@datacube \
	ingest \
	[~copy_template,dryrun,overwrite,scope=<scope>,upload] \
	[.|<datacube-id>] \
	[<args>]
 . ingest <datacube-id>/<scope>.
   scope: all + metadata + raster + rgb + rgbx + <.jp2> + <.tif> + <.tiff>
      all: ALL files.
      metadata (default): any < 1 MB.
      raster: all raster.
      rgb: rgb.
      rgbx: rgb and what is needed to build rgb.
      <suffix>: any *<suffix>.
```
