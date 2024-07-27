# 🧊 datacube

`datacube`s are [objects](https://kamangir-public.s3.ca-central-1.amazonaws.com/giza-v1/giza.pdf) that can be [queried](../catalog/README.md) and [ingested](#ingest).

## ingest

run `@datacube ingest` to ingest a datacube, or use `@catalog query <catalog> ingest`. 

```bash
 > @datacube ingest help
@datacube ingest \
	[assets=all|<item-1+item-2>,~copy_template,dryrun,suffix=<suffix>,upload] \
	[.|<object-name>] \
	[<args>]
 . ingest <object-name>.
 ```