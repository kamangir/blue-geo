# 🧊

`datacube`s are [objects](https://kamangir-public.s3.ca-central-1.amazonaws.com/giza-v1/giza.pdf) that can be [queried](#query) and [ingested](#ingest).

## query

run an `@datacube query`, then `@datacube query read` the `datacube-id`(s) as object names and use them with commands.

```bash
 > @datacube query help
@datacube query \
	<catalog> \
	download,ingest,select,upload \
	-|<object-name> \
	<query-options> \
	<args>
 . <catalog> -query-> <object-name>.
@datacube query read \
	[all,download,len] \
	[.|<object-name>] \
	[--count <count>] \
	[--delim <delim>] \
	[--index <index>] \
	[--prefix <prefix>] \
	[--suffix <suffix>] \
	[--contains <contains>] \
	[--notcontains <not-contains>]
 . read query results in <object-name>.
```

supported `<catalog>`s: [firms_area](./firms_area/).

## ingest

run `@datacube ingest` to ingest a datacube, or `@datacube query <catalog> ingest,...`. 

```bash
 > @datacube ingest help
@datacube ingest \
	[assets=all|<item-1+item-2>,dryrun,suffix=<suffix>,upload] \
	[.|<object-name>] \
	<args>
 . ingest <object-name>.
 ```