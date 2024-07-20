# 🧊

`datacube`s can be queried, selected, and ingested, and then they become ordinary objects.

```bash
@datacube query firms_area <object-name> \
	select \
	--source <source> \
	--area <area> \
	--date <date> \
	--depth <depth>

@datacube query len

@datacube query select \
  <object-name> \
  - \
  --index <index> \
  --prefix <prefix> \
  --suffix <suffix> \
  --contains <contains> \
  --not-contains <not-contains>

@datacube ingest \
  all,items=<item-1+item-2>,suffix=<suffix> \
  <object-name>
```