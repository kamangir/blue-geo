# 🌐 `@geo watch`

watch the planet's [story](./targets.yaml) unfold

```bash
@geo watch help
```
```bash
@geo watch \
	[dryrun] \
	[<query-object-name> | target=<target>] \
	[dryrun,to=<runner>] \
	[dryrun,modality=<modality>] \
	[dryrun,~gif,publish] \
	[-|<object-name>]
 . watch target -> <object-name>.
   modality: rgb|diff
   runner: aws_batch|generic|local
   target: Chilcotin-test|Fagradalsfjall|Hurricane-Idalia-2023|Jasper|Leonardo|Leonardo-test|Mount-Etna|bellingcat-2024-09-27-nagorno-karabakh|bellingcat-2024-09-27-nagorno-karabakh-test|burning-man-2024|chilcotin-river-landslide|elkhema
@geo watch map \
	[dryrun,~download,modality=<modality>,offset=<offset>,suffix=<suffix>,~upload] \
	[.|<query-object-name>]
 . @geo watch map <query-object-name> @ <offset> -> /<suffix>.
   modality: rgb|diff,
@geo watch reduce \
	[dryrun,~download,publish,suffix=<suffix>,~upload] \
	[..|<query-object-name>] \
	[.|<object-name>]
 . @geo watch reduce <query-object-name>/<suffix> -> <object-name>.
@geo watch targets cp|copy \
	[-] \
	[..|<object-name-1>] \
	[.|<object-name-2>]
 . copy <object-name-1>/target -> <object-name-2>.
@geo watch targets get \
	[--delim space] \
	[--target_name <target>] \
	[--what <catalog|collection|exists|query_args>]
 . get <target> info.
@geo watch targets list \
	[--catalog <catalog>] \
	[--collection <collection>] \
	[--count <count>] \
	[--delim <space>]
 . list targets.
@geo watch targets save \
	[--target_name <target>] \
	[--object_name <object-name>]
 . save <target> -> <object-name>.
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
- [`test_blue_geo_watch_v3-Chilcotin-test`](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v3-Chilcotin-test.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v3-Chilcotin-test/test_blue_geo_watch_v3-Chilcotin-test.gif), [![bashtest](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml).
- [`geo-watch-2024-08-31-chilcotin-c`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-08-31-chilcotin-c.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-08-31-chilcotin-c/geo-watch-2024-08-31-chilcotin-c.gif), L1C and L2A mixed, `2024-07-30/2024-08-09`, [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-199-11f9b5497ef0).
- [`geo-watch-2024-09-01-chilcotin-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-a/geo-watch-2024-09-01-chilcotin-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-201-d64e9bb3716b).
- [`geo-watch-2024-09-01-chilcotin-c`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-c.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-c/geo-watch-2024-09-01-chilcotin-c.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-202-d59ba811398b), [on reddit](https://www.reddit.com/r/bash/comments/1f9cvyx/a_bash_python_tool_to_watch_a_target_in_satellite/)..

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-c/geo-watch-2024-09-01-chilcotin-c-2X.gif?raw=true&random=zA37euJiAZXcn0ui)

## [Burning Man 2024](./targets/burning-man-2024.md)
- [`geo-watch-2024-09-04-burning-man-2024-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-burning-man-2024-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-burning-man-2024-a/geo-watch-2024-09-04-burning-man-2024-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-205-c272a95ce266).

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-burning-man-2024-a/geo-watch-2024-09-04-burning-man-2024-a-2X.gif?raw=true&random=gN6fPYzFirVhiSO9)

## [Mount Etna](./targets/Mount-Etna.md)
- [`geo-watch-2024-09-04-Mount-Etna-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Mount-Etna-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Mount-Etna-a/geo-watch-2024-09-04-Mount-Etna-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-205-c272a95ce266).

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Mount-Etna-a/geo-watch-2024-09-04-Mount-Etna-a-2X.gif?raw=true&random=252SOgNIFO2IRAGD)

## [Fagradalsfjall](./targets/Fagradalsfjall.md)
- [`geo-watch-2024-09-04-Fagradalsfjall-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Fagradalsfjall-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Fagradalsfjall-a/geo-watch-2024-09-04-Fagradalsfjall-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-206-f7996520dc15).

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Fagradalsfjall-a/geo-watch-2024-09-04-Fagradalsfjall-a-2X.gif?raw=true&random=ttfOdkJHe3L5pnu6)

## [Jasper](./targets/Jasper.md)
- [`geo-watch-2024-09-06-Jasper-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-06-Jasper-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-06-Jasper-a/geo-watch-2024-09-06-Jasper-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-208-7063fca1423b).

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-06-Jasper-a/geo-watch-2024-09-06-Jasper-a-2X.gif?raw=true&random=Dqh3HabBOmPTemwa)

## [Leonardo](./targets/Leonardo.md)
- [`test_blue_geo_watch_v3-Leonardo-test`](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v3-Leonardo-test.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v3-Leonardo-test/test_blue_geo_watch_v3-Leonardo-test.gif), [![bashtest](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml).
- [`geo-watch-2024-09-30-Leonardo-g`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-30-Leonardo-g.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-30-Leonardo-g/geo-watch-2024-09-30-Leonardo-g.gif), [dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-237-99db71023445).

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-30-Leonardo-g/geo-watch-2024-09-30-Leonardo-g-2X.gif?raw=true&random=Hbyx4fGGMNCPosO7)


