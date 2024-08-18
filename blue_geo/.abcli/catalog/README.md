# 🌐 catalog

`catalog`s can be [listed](#listing-catalogs) and [browsed](#browsing-a-catalog) and [queried](#running-a-query-for-datacubes) for [`datacube`](../datacube/)s.

## listing catalogs

to see the list of catalogs, 

```bash
@catalog list
```
```bash
🌐  4 catalog(s): copernicus,firms,generic,ukraine_timemap
```

to see the list of collections in a catalog,

```bash
@catalog list collections --catalog copernicus
```
```bash
🌐  16 collection(s): CCM,COP-DEM,ENVISAT,GLOBAL-MOSAICS,LANDSAT-5,LANDSAT-7,LANDSAT-8,S2GLC,SENTINEL-1,SENTINEL-1-RTC,SENTINEL-2,SENTINEL-3,SENTINEL-5P,SENTINEL-6,SMOS,TERRAAQUA
```

for special collections, a [datacube class](../datacube/) is defined, and, therefore, items from these collections can be ingested as datacubes, which are objects.

to see the list of datacube classes for a catalog,

```bash
@catalog list datacube_classes --catalog copernicus
```
```bash
🌐  1 datacube class(s): sentinel_2
```

## browsing a catalog

to see the list of pages that can be browsed for catalog,

```bash
@catalog browse <catalog> [help]
```

```bash
@catalog browse firms area
```
```bash
@catalog: browsing firms ...
🔗 https://firms.modaps.eosdis.nasa.gov/api/area/
```

## running a query on a catalog for datacubes

to run a query on a catalog,

```bash
@catalog query <catalog> select,ingest \
	$object_name \
	<args>
```

or, drop `select`, and access the datacube-ids,

```bash
datacube_id=$(@catalog query read - \
	$object_name \
	[--count <count>] \
	[--delim <delim>] \
	[--index <index>] \
	[--prefix <prefix>] \
	[--suffix <suffix>] \
	[--contains <contains>] \
	[--notcontains <not-contains>]
```

to see catalog-specific query args,

```bash
@catalog query <catalog> help
```
```bash
@catalog query copernicus \
	[download,ingest,select,upload] \
	[-|<object-name>] \
	[sentinel_2,dryrun] \
	[--param help]
 . copernicus/sentinel_2 -query-> <object-name>.
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
 ```

refer to examples in these catalogs: [copernicus](./copernicus/), [firms](./firms/), [ukraine_timemap](./ukraine_timemap/).