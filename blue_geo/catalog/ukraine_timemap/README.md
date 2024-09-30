# 🇺🇦 ukraine-timemap

the `ukraine-timemap` catalog covers the [Bellingcat](https://www.bellingcat.com/) [Civilian Harm in Ukraine TimeMap](https://github.com/bellingcat/ukraine-timemap) dataset, available through [this UI](https://ukraine.bellingcat.com/) and [this API](https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json).

 - [dataset](https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json)
 - [github](https://github.com/bellingcat/ukraine-timemap)
 - [home](https://ukraine.bellingcat.com/)

## query

```bash
@catalog query ukraine_timemap
```
```bash
@catalog query ukraine_timemap \
	[dryrun,ukraine_timemap,select,upload] \
	[ingest,~copy_template,dryrun,overwrite,scope=<scope>,upload] \
	[-|<object-name>] \
	[--arg <value>]
 . ukraine_timemap/ukraine_timemap -query-> <object-name>.
   scope: @datacube ingest help.
```

## example use

```bash
@catalog query ukraine_timemap \
	select ingest -

@open QGIS .
@publish tar .
```

![image](https://github.com/kamangir/assets/blob/main/nbs/ukraine-timemap/ingest_log.png?raw=true)

latest ingested object: [ukraine-timemap.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/ukraine_timemap.tar.gz), 

sandbox: [ukraine-timemap/sandbox.ipynb](./notebooks/ukraine-timemap/sandbox.ipynb).

last build [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/ukraine_timemap/ukraine_timemap.png)

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/ukraine_timemap/ukraine_timemap.png)

![image](https://github.com/kamangir/assets/blob/main/nbs/ukraine-timemap/QGIS.png?raw=true)

more: https://arash-kamangir.medium.com/%EF%B8%8F-openai-experiments-93-bf0cee062693
