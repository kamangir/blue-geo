# 🧊

`datacube`s are regular objects that can be queried and ingested.

```bash
@datacube query <catalog> \
	select \
    <object-name> \
	--source <source> \
	--area <area> \
	--date <date> \
	--depth <depth>

@datacube query len

@datacube query read \
    - \
    <object-name> \
    --index <index> \
    --prefix <prefix> \
    --suffix <suffix> \
    --contains <contains> \
    --not-contains <not-contains>

@datacube ingest \
    all,items=<item-1+item-2>,suffix=<suffix> \
    <object-name>
```