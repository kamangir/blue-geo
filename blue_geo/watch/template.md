# 🌐 `@geo watch`

watching [targets](./targets.yaml) through `@geo`.

```bash
 > @geo watch help
```

--include-- ./targets/chilcotin-river-landslide.md case study: Chilcotin River Landslide

## example run

```bash
@batch eval - \
  blue_geo watch - target=chilcotin-river-landslide to=aws_batch - publish \
  geo-watch-2024-08-31-chilcotin-c
```

--table--