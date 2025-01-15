# 🌐 Maxar Open Data (`maxar_open_data`)

The `maxar_open_data` catalog covers [Maxar's Open Data program](https://www.maxar.com/open-data/).

 - [home](https://www.maxar.com/open-data)

## query

```bash
@catalog query maxar_open_data help
```
```bash
@catalog query maxar_open_data \
	[dryrun,collection,select,upload] \
	[ingest,~copy_template,dryrun,overwrite,scope=<scope>,upload] \
	[-|<object-name>] \
	[--collection_id <@maxar list>] \
	[--end_date <yyyy-mm-dd>] \
	[--start_date <yyyy-mm-dd>]
 . maxar_open_data/collection -query-> <object-name>.
   scope: @datacube ingest help.
```

## example use

```bash
@catalog query maxar_open_data select ingest - \
    --collection_id WildFires-LosAngeles-Jan-2025 \
    --start_date 2025-01-10 \
    --end_date 2025-01-13

@open QGIS .
@publish tar .
```

🔥


```yaml
🚧
```

🚧 🖼️

🚧 🖼️

[.tar.gz](https://kamangir-public.....tar.gz)

🚧 🖼️
