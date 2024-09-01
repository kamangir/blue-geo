# 🌐 `@geo watch`

watching [targets](./targets.yaml) through `@geo`.

```bash
 > @geo watch help
```

## case study: Chilcotin River Landslide

![image](https://github.com/kamangir/assets/blob/main/blue-geo/chilcotin-river-landslide-2.jpg?raw=true)

background:
- [Chilcotin River Landslide Information Portal](https://chilcotin-river-landslide-2024-bcgov03.hub.arcgis.com/) - source of ⬆️ image.
- [Google Map](https://maps.app.goo.gl/WHTNCDsFNoZAAnzX8): `lat: 51°50'51.1"N`, `lon: 122°47'06.8"W`.
- [Chilcotin River’s Landslide Lake Begins Draining](https://www.bluemarble.nasa.gov/images/153195/chilcotin-rivers-landslide-lake-begins-draining)
- [Reddit: Before and after satellite images of the Chilcotin River landslide](https://www.reddit.com/r/britishcolumbia/comments/1eh9eql/before_and_after_satellite_images_of_the/)


```yaml
toi:
    - from: 2024-07-30
    - to: 2024-08-09
aoi: 
    - lat: 51.83
    - lon: -122.78
```

---

using [chilcotin-river-landslide](./targets/chilcotin-river-landslide.md).

## example run

```bash
@batch eval - \
  blue_geo watch - target=chilcotin-river-landslide to=aws_batch - - \
  geo-watch-2024-08-31-chilcotin-c
```

```
@select geo-watch-2024-08-31-chilcotin-c
@publish tar .
@publish suffix=.gif .
```

[geo-watch-2024-08-31-chilcotin-c.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-08-31-chilcotin-c.tar.gz)

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-08-31-chilcotin-c/geo-watch-2024-08-31-chilcotin-c.gif)
