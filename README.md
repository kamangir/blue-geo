# 🌐 Blue-GEO

AI for precise geospatial data analysis and visualization.

```bash
pip install blue-geo
```

| | | |
|-|-|-|
| 🌐 [QGIS](./blue_geo/.abcli/QGIS/README.md) | 🇺🇦 [ukraine-timemap](./blue_geo/.abcli/ukraine-timemap/README.md) | 🌈 [vancouver-watching](https://github.com/kamangir/Vancouver-Watching) |
| [![image](https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/QGIS.png)](./blue_geo/.abcli/QGIS/README.md) | [![image](https://github.com/kamangir/assets/blob/main/nbs/ukraine-timemap/QGIS.png?raw=true)](./blue_geo/.abcli/ukraine-timemap/README.md) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_vancouver_watching_ingest/animation.gif?raw=true)](https://github.com/kamangir/Vancouver-Watching)  |
| an AI terraform for [QGIS](https://www.qgis.org/). | ingests the [Bellingcat](https://www.bellingcat.com/) [Civilian Harm in Ukraine TimeMap](https://github.com/bellingcat/ukraine-timemap) dataset, available through [this UI](https://ukraine.bellingcat.com/) and [this API](https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json), and generates a `geojson`, a QGIS project, and [more](https://kamangir-public.s3.ca-central-1.amazonaws.com/ukraine_timemap/ukraine_timemap.png).  | 🌈 Vancouver watching with AI, last build: [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_vancouver_watching_ingest/animation.gif). |  |






---

[![PyPI version](https://img.shields.io/pypi/v/blue-geo.svg)](https://pypi.org/project/blue-geo/)

📜 [metadata](./metadata.yaml)

---

To use on [AWS SageMaker](https://aws.amazon.com/sagemaker/) replace `<plugin-name>` with the name of the plugin and follow [these instructions](https://github.com/kamangir/notebooks-and-scripts/blob/main/SageMaker.md).
