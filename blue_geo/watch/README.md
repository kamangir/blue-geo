# 🌐 `@geo watch`

watching [targets](./targets.yaml) through `@geo`.

```bash
 > @geo watch help
@geo watch  \
  [dryrun] \
  [<query-object-name>,target=burning-man-2024|chilcotin-river-landslide|elkhema|Mount-Etna|test] \
  [dryrun,to=aws_batch|generic|local] \
  [dryrun] \
  [dryrun,~gif,publish] \
  [-|<object-name>]
  . watch target -> <object-name>.
```

## example run

```bash
@batch eval - \
  blue_geo watch - \
  target=chilcotin-river-landslide \
  to=aws_batch - \
  publish \
  geo-watch-2024-09-01-chilcotin-a
```

## [Chilcotin River Landslide](./targets/chilcotin-river-landslide.md)
- [`test_blue_geo_watch`](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch/test_blue_geo_watch.gif), [![bashtest](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml).
- [`geo-watch-2024-08-31-chilcotin-c`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-08-31-chilcotin-c.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-08-31-chilcotin-c/geo-watch-2024-08-31-chilcotin-c.gif), L1C and L2A mixed, `2024-07-30/2024-08-09`, [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-199-11f9b5497ef0).
- [`geo-watch-2024-09-01-chilcotin-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-a/geo-watch-2024-09-01-chilcotin-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-201-d64e9bb3716b).
- [`geo-watch-2024-09-01-chilcotin-c`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-c.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-c/geo-watch-2024-09-01-chilcotin-c.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-202-d59ba811398b).

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-c/geo-watch-2024-09-01-chilcotin-c-2X.gif?raw=true&random=1cbjHGR0EMNvU6jS)

## [Burning Man 2024](./targets/burning-man-2024.md)

## [Mount Etna](./targets/Mount-Etna.md)


