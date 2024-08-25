# 🌐 `@geo watch`

watching targets through `@geo`.

```bash
 > @geo watch help
```

--include-- ./targets/chilcotin-river-landslide.md case study: Chilcotin River Landslide

## example run

```bash
@geo watch  \
	dryrun,query=chilcotin | query_object_name \
	dryrun,to=generic \
	$object-name
```

🔥