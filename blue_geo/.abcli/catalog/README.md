# 🌐 catalog

`catalog`s can be listed and browsed and queried for [`datacube`](../datacube/)s,

```bash
 > @catalog help
@catalog browse \
	<catalog> \
	[<args>]
 . browse <catalog>.
@catalog list \
	[-] \
	[--delim space] \
	[--log 0]
 . list catalogs.
@catalog query \
	<catalog> \
	[download,ingest,select,upload] \
	[-|<object-name>] \
	[<query-options>] \
	[<args>]
 . <catalog> -query-> <object-name>.
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

supported `<catalog>`s: [firms](./firms/).
