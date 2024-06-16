# 🌐 Blue-GEO

AI for precise geospatial data analysis and visualization.

```bash
pip install blue-geo
```

🔷 [QGIS](#QGIS) 🔷 [ukraine-timemap](#ukraine-timemap-) 🇺🇦 🔷 [sources](./sources.yaml) 🔷

---

## QGIS

```bash
 > QGIS help
QGIS seed [screen]
 . seed 🌱 QGIS.
QGIS expressions pull
 . pull QGIS expressions.
QGIS expressions push [push]
 . push QGIS expressions.
 📂 /Users/kamangir/Library/Application Support/QGIS/QGIS3/profiles/default/python/expressions
 📂 /Users/kamangir/git/blue-geo/blue_geo/QGIS/expressions
QGIS serve[r] [start]
 . start QGIS server.
```

to start, generate the seed 🌱,

```bash
QGIS seed
```

and paste it in the Python Console in QGIS.

![image](https://github.com/kamangir/assets/blob/main/blue-geo/QGIS-python-console.png?raw=true)

---

## ukraine-timemap 🇺🇦

[`ukraine-timemap`](./blue_geo/.abcli/ukraine-timemap/) ingests the [Civilian Harm in Ukraine TimeMap](https://github.com/bellingcat/ukraine-timemap) dataset, available through [this UI](https://ukraine.bellingcat.com/) and [this API](https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json), and generates a `geojson`, a QGIS project, and more.

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

---

[![PyPI version](https://img.shields.io/pypi/v/blue-geo.svg)](https://pypi.org/project/blue-geo/)

To use on [AWS SageMaker](https://aws.amazon.com/sagemaker/) replace `<plugin-name>` with the name of the plugin and follow [these instructions](https://github.com/kamangir/notebooks-and-scripts/blob/main/SageMaker.md).
