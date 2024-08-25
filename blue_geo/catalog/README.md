# 🌐 catalog

`catalog`s are [lists](#listing-catalogs) of collections that can be [browsed](#browsing-a-catalog), [queried](#running-a-query-for-datacubes), and [ingested as `datacube`](../datacube/)s. 

look for example uses in the supported catalogs: [copernicus](./copernicus/), [firms](./firms/), [ukraine_timemap](./ukraine_timemap/). 

## adding a new catalog

1️⃣ clone [blue_geo/catalog/generic](./generic/) similar to [blue_geo/catalog/copernicus](./copernicus/) and define `NovelCatalog`.

2️⃣ [add the datacube class `NovelDatacube`](../datacube/README.md#adding-a-new-datacube-class) to represent one of the collections in `NovelCatalog`.

3️⃣ add `NovelCatalog` to [blue_geo/catalog/classes.py](./classes.py).

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

to see the list of datacube classes for a catalog,

```bash
@catalog list datacube_classes --catalog copernicus
```
```bash
🌐  1 datacube class(s): sentinel_2
```

## browsing a catalog

to see the list of pages that can be browsed for a catalog,

```bash
@catalog browse firms help
```
```bash
@catalog browse firms \
	area|map_key
 . browse firms.
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
@catalog query <catalog> <collection>,select \
	ingest \
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
@catalog query help
```
```bash
@catalog query copernicus \
	[dryrun,sentinel_2,select,upload] \
	[ingest,~copy_template,dryrun,overwrite,upload,what=all|metadata|quick|<suffix>] \
	[-|<object-name>] \
	[--bbox <-122.88,51.73,-122.68,51.93>]\
	[--count <10>, -1: all]\
	[--datetime <2024-07-30/2024-08-09>]\
	[--lat <51.83>]\
	[--lon <-122.78>]\
	[--radius <0.1>]
 . copernicus/sentinel_2 -query-> <object-name>.
@catalog query firms \
	[dryrun,area,select,upload] \
	[ingest,~copy_template,dryrun,overwrite,upload,what=all|metadata|quick|<suffix>] \
	[-|<object-name>] \
	[--area east|north|south|west|world]\
	[--date <yyyy-mm-dd>]\
	[--depth 1..10]\
	[--source LANDSAT_NRT|MODIS_NRT|MODIS_SP|VIIRS_NOAA20_NRT|VIIRS_NOAA21_NRT|VIIRS_SNPP_NRT|VIIRS_SNPP_SP]
 . firms/area -query-> <object-name>.
@catalog query ukraine_timemap \
	[dryrun,ukraine_timemap,select,upload] \
	[ingest,~copy_template,dryrun,overwrite,upload,what=all|metadata|quick|<suffix>] \
	[-|<object-name>] \
	[--arg <value>]
 . ukraine_timemap/ukraine_timemap -query-> <object-name>.
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