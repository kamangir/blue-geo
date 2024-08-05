# 🇺🇦 ukraine-timemap

the `ukraine-timemap` catalog covers the [Bellingcat](https://www.bellingcat.com/) [Civilian Harm in Ukraine TimeMap](https://github.com/bellingcat/ukraine-timemap) dataset, available through [this UI](https://ukraine.bellingcat.com/) and [this API](https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json).

## query

```
 > @catalog query ukraine_timemap help
@catalog query ukraine_timemap \
	[download,ingest,select,upload] \
	[-|<object-name>] \
	[dryrun]
 . ukraine_timemap -query-> <object-name>.
```

## example use

```bash
@catalog query ukraine_timemap \
	ingest,select - 

@open QGIS .
@publish tar .
```

:fire

--- digest :below

```bash
 > ukraine_timemap help
ukraine_timemap browse \
	[dataset|github]
 . browse ukraine-timemap.
ukraine_timemap ingest \
	[dryrun,~upload] \
	[-|<object-name>] \
	[--verbose 1]
 . ingest the latest dataset from https://github.com/bellingcat/ukraine-timemap.
```

example use,

```
@select ukraine-timemap-$(@@timestamp)
ukraine_timemap ingest - . --verbose 1
@open . QGIS
@publish tar .
```

![image](https://github.com/kamangir/assets/blob/main/nbs/ukraine-timemap/ingest_log.png?raw=true)

latest ingested object: [ukraine-timemap.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/ukraine_timemap.tar.gz), sandbox: [ukraine-timemap/sandbox.ipynb](./notebooks/ukraine-timemap/sandbox.ipynb).

last build [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/ukraine_timemap/ukraine_timemap.png)

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/ukraine_timemap/ukraine_timemap.png)

![image](https://github.com/kamangir/assets/blob/main/nbs/ukraine-timemap/QGIS.png?raw=true)

more: https://arash-kamangir.medium.com/%EF%B8%8F-openai-experiments-93-bf0cee062693