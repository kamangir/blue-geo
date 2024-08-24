# 🌐 `@geo watch`

watching targets through `@geo`.

```bash
 > @geo watch help
@geo watch \
	[dryrun,upload] \
	[target=chilcotin-river-landslide,datetime=<2024-07-30/2024-08-15>,lat=<51.83>,lon=<-122.78>] \
	[dryrun,to=aws_batch|generic|local] \
	[-|<object-name>]
 . watch a target.
```

--include-- ./targets/chilcotin-river-landslide.md case study: Chilcotin River Landslide

## example run

```bash
@geo watch  \
	[dryrun,frames=<frames>,upload] \
	[dryrun,datetime=<2024-07-30/2024-08-15>,lat=<51.83>,lon=<-122.78>,target=chilcotin-river-landslide] \
	[dryrun,to=aws_batch|generic|local] \
	[-|<object-name>]
```

🔥