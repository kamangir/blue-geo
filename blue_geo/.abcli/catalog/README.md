# 🌐 catalog

`catalog`s can be listed and browsed and queried for [`datacube`](../datacube/)s,

```bash
 > @catalog help
@catalog browse firms \
	[map_key|area]
 . browse firms.
@catalog browse ukraine_timemap \
	[dataset|github]
 . browse ukraine-timemap.
@catalog get \
	[list_of_collections] \
	[--catalog <catalog>] \
	[--count 1] \
	[--delim ,] \
	[--log 0]
 . get list of collections in <catalog>.
@catalog list \
	[-] \
	[--delim space] \
	[--log 0]
 . list catalogs.
@catalog query firms \
	[download,ingest,select,upload] \
	[-|<object-name>] \
	[area,dryrun] \
	[--area east|north|south|west|world]\
	[--date yyyy-mm-dd]\
	[--depth 1..10]\
	[--source LANDSAT_NRT|MODIS_NRT|MODIS_SP|VIIRS_NOAA20_NRT|VIIRS_NOAA21_NRT|VIIRS_SNPP_NRT|VIIRS_SNPP_SP]
 . firms/area -query-> <object-name>.
@catalog query ukraine_timemap \
	[download,ingest,select,upload] \
	[-|<object-name>] \
	[dryrun]
 . ukraine_timemap -query-> <object-name>.
@catalog query read \
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

supported `<catalog>`s: [copernicus](./copernicus/), [firms](./firms/), [ukraine_timemap](./ukraine_timemap/).
