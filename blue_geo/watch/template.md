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

--table--
