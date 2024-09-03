# 🌐 Earth Search

the `Earth Search` catalog covers [Earth Search by Element 84](https://stacindex.org/catalogs/earth-search#/). see [datacube](../) for usage instructions.

- https://registry.opendata.aws/sentinel-2/
- https://viewer.aws.element84.com/

## query

```bash
 > @catalog query EarthSearch help

🔥

```

## case study: Chilcotin River Landslide

![image](https://github.com/kamangir/assets/blob/main/blue-geo/chilcotin-river-landslide-2.jpg?raw=true)

background:
- [Chilcotin River Landslide Information Portal](https://chilcotin-river-landslide-2024-bcgov03.hub.arcgis.com/) - source of ⬆️ image.
- [Google Map](https://maps.app.goo.gl/WHTNCDsFNoZAAnzX8): `lat: 51°50'51.1"N`, `lon: 122°47'06.8"W`.
- [Chilcotin River’s Landslide Lake Begins Draining](https://www.bluemarble.nasa.gov/images/153195/chilcotin-rivers-landslide-lake-begins-draining)
- [Reddit: Before and after satellite images of the Chilcotin River landslide](https://www.reddit.com/r/britishcolumbia/comments/1eh9eql/before_and_after_satellite_images_of_the/)


details: [targets.yaml](../targets.yaml).

using [chilcotin-river-landslide](../../watch/targets/chilcotin-river-landslide.md).

## example run

```bash
@select chilcotin-query-2024-08-23-v1
@catalog query EarthSearch sentinel_2_l1c ingest . \
  --count 10 \
  --datetime 2024-07-30/2024-08-09 \
  --lat  51.83 \
  --lon -122.78

@select $(@catalog query read - . --count 1 --offset 3)
@datacube ingest what=quick .
@publish tar .
```

🔥

![image](https://github.com/kamangir/assets/blob/main/blue-geo/TBA.png?raw=true)

[datacube-EarthSearch-sentinel_2_l1c-TBA.tar.gz](TBA)

- [dev notes](TBA)
