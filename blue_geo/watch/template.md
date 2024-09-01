# 🌐 `@geo watch`

watching [targets](./targets.yaml) through `@geo`.

```bash
 > @geo watch help
```

--include-- ./targets/chilcotin-river-landslide.md case study: Chilcotin River Landslide

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