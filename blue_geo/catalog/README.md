# 🌐 catalog

`catalog`s are [lists](#listing-catalogs) of collections that can be [browsed](#browsing-a-catalog), [queried](#running-a-query-for-datacubes), and [ingested as `datacube`](../datacube/)s.

`catalog`s are generalized [STAC](https://stacspec.org/en/tutorials/intro-to-stac/) Catalogs.

to add a new catalog follow [these instructions](../doc/adding-catalogs-and-datacubes.md).

## supported catalogs

- [copernicus](./copernicus/)
- [EarthSearch](./EarthSearch/)
- [firms](./firms/)
- [SkyFox](./SkyFox/)
- [ukraine_timemap](./ukraine_timemap/)

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
@catalog browse \
	firms \
	home|area|map-key
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
