# 🌐 `@geo watch`

watch the planet's story unfold.

```bash
@geo watch help
```
```bash
@geo watch \
	[batch,dryrun,name=<job-name>] \
	[<query-object-name> | target=<target>] \
	[dryrun,to=<runner>] \
	[dryrun,modality=<modality>] \
	[dryrun,~gif,publish] \
	[-|<object-name>]
 . watch target -> <object-name>.
   modality: rgb|diff
   runner: aws_batch|generic|local
   target: 
@geo watch \
	batch,dryrun,name=<job-name> \
	[<query-object-name> | target=<target>] \
	[dryrun,to=<runner>] \
	[dryrun,modality=<modality>] \
	[dryrun,~gif,publish] \
	[-|<object-name>]
 . watch target -aws-batch-> <object-name>.
   modality: rgb|diff
   runner: aws_batch|generic|local
   target: 
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
@targets cat \
	<target-name>
 . cat <target-name>.
@targets cp|copy \
	[-] \
	[..|<object-name-1>] \
	[.|<object-name-2>]
 . copy <object-name-1>/target -> <object-name-2>.
@targets download
 . download watch targets.
   $BLUE_GEO_WATCH_TARGET_LIST: blue-geo-target-list-v1
@targets edit
 . edit watch targets.
   /home/codespace/storage/abcli/blue-geo-target-list-v1/metadata.yaml
@targets get \
	[--delim space] \
	[--including_versions 0] \
	[--target_name <target>] \
	[--what <catalog|collection|exists|one_liner|query_args>]
 . get <target> info.
@targets list \
	[--catalog <catalog>] \
	[--collection <collection>] \
	[--count <count>] \
	[--delim <space>] \
	[--including_versions 0]
 . list targets.
@targets publish
 . publish watch targets.
   $BLUE_GEO_WATCH_TARGET_LIST: blue-geo-target-list-v1
@targets save \
	[target=all|<target-name>] \
	[.|<object-name>]
 . save target(s) -> <object-name>.
@targets test
 . test watch targets.
   $BLUE_GEO_WATCH_TARGET_LIST: blue-geo-target-list-v1
@targets upload
 . upload watch targets.
   $BLUE_GEO_WATCH_TARGET_LIST: blue-geo-target-list-v1
```

🎯 [`geo-watch-targets/metadata.yaml`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-targets/metadata.yaml): [geojson](./targets.geojson).

## example run

```bash
@geo watch \
  batch \
  target=elkhema-2024 \
  to=aws_batch \
  modality=rgb \
  publish \
  geo-watch-elkhema-2024-2024-10-05-a-b
```

[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-252-2118326b1de2).

ℹ️ suffix published gif urls with `-2X` and `-4X` for different scales. example: [1X](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b.gif), [2X](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b-2X.gif), [4X](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b-4X.gif).

## `Cache-Creek`

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2x-wider-2024-10-06-a/geo-watch-Cache-Creek-2x-wider-2024-10-06-a-4X.gif?raw=true&random=IyA0a7Ushpntitbg)
- [`geo-watch-Cache-Creek-2024-10-06-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2024-10-06-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2024-10-06-a/geo-watch-Cache-Creek-2024-10-06-a.gif), [dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-253-8f12ef5bd8fc).
- [`geo-watch-Cache-Creek-2x-wider-2024-10-06-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2x-wider-2024-10-06-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2x-wider-2024-10-06-a/geo-watch-Cache-Creek-2x-wider-2024-10-06-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-256-c1b564c9f89e).

## [`Fagradalsfjall`](./targets/Fagradalsfjall.md)

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Fagradalsfjall-a/geo-watch-2024-09-04-Fagradalsfjall-a-2X.gif?raw=true&random=g6eYD24LsSlmGypr)
- [`geo-watch-2024-09-04-Fagradalsfjall-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Fagradalsfjall-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Fagradalsfjall-a/geo-watch-2024-09-04-Fagradalsfjall-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-206-f7996520dc15).

## [`Jasper`](./targets/Jasper.md)

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-06-Jasper-a/geo-watch-2024-09-06-Jasper-a-2X.gif?raw=true&random=bzif7PrWmS39OPuk)
- [`geo-watch-2024-09-06-Jasper-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-06-Jasper-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-06-Jasper-a/geo-watch-2024-09-06-Jasper-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-208-7063fca1423b).

## [`Leonardo`](./targets/Leonardo.md)

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Leonardo-2024-10-06-a/geo-watch-Leonardo-2024-10-06-a-4X.gif?raw=true&random=nzO3z8lB9Kld0iqh)
- [`test_blue_geo_watch_v4-Leonardo-test`](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v4-Leonardo-test.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v4-Leonardo-test/test_blue_geo_watch_v4-Leonardo-test.gif), [![bashtest](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml).
- [`geo-watch-2024-09-30-Leonardo-g`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-30-Leonardo-g.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-30-Leonardo-g/geo-watch-2024-09-30-Leonardo-g.gif), [dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-237-99db71023445).
- [`geo-watch-Leonardo-2024-10-05-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Leonardo-2024-10-05-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Leonardo-2024-10-05-a/geo-watch-Leonardo-2024-10-05-a.gif), [dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-249-44ba1dcd2321).
- [`geo-watch-Leonardo-2024-10-06-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Leonardo-2024-10-06-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Leonardo-2024-10-06-a/geo-watch-Leonardo-2024-10-06-a.gif), [dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-255-1f2a8f1ccef5).

## [`Mount-Etna`](./targets/Mount-Etna.md)

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Mount-Etna-a/geo-watch-2024-09-04-Mount-Etna-a-2X.gif?raw=true&random=LZGI6xz8eNphtMqB)
- [`geo-watch-2024-09-04-Mount-Etna-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Mount-Etna-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Mount-Etna-a/geo-watch-2024-09-04-Mount-Etna-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-205-c272a95ce266).

## `bellingcat-2024-09-27-nagorno-karabakh`

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a-4X.gif?raw=true&random=NwcdUm8HZmHZETgz)
- [`bellingcat-2024-09-27-nagorno-karabakh-2024-10-01-c-b`](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-2024-10-01-c-b.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-2024-10-01-c-b/bellingcat-2024-09-27-nagorno-karabakh-2024-10-01-c-b.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-241-3e25857747a5).
- [`bellingcat-2024-09-27-nagorno-karabakh-b`](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-b.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-b/bellingcat-2024-09-27-nagorno-karabakh-b.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-244-a5f9b7959748).
- [`bellingcat-2024-09-27-nagorno-karabakh-6X-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-6X-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-6X-a/bellingcat-2024-09-27-nagorno-karabakh-6X-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-245-18f6d15e5fbd).
- [`geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b.gif), [dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-250-847d3d5f0d6e).
- [`geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a.gif), [dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-255-1f2a8f1ccef5).

## [`burning-man-2024`](./targets/burning-man-2024.md)

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-burning-man-2024-a/geo-watch-2024-09-04-burning-man-2024-a-2X.gif?raw=true&random=knJwgVAcEiUiYFMz)
- [`geo-watch-2024-09-04-burning-man-2024-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-burning-man-2024-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-burning-man-2024-a/geo-watch-2024-09-04-burning-man-2024-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-205-c272a95ce266).

## [`chilcotin-river-landslide`](./targets/chilcotin-river-landslide.md)

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-c/geo-watch-2024-09-01-chilcotin-c-2X.gif?raw=true&random=DbUTA3sIU9iKAjFp)
- [`test_blue_geo_watch_v4-chilcotin-river-landslide-test`](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v4-chilcotin-river-landslide-test.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v4-chilcotin-river-landslide-test/test_blue_geo_watch_v4-chilcotin-river-landslide-test.gif), [![bashtest](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml).
- [`geo-watch-2024-08-31-chilcotin-c`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-08-31-chilcotin-c.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-08-31-chilcotin-c/geo-watch-2024-08-31-chilcotin-c.gif), L1C and L2A mixed, `2024-07-30/2024-08-09`, [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-199-11f9b5497ef0).
- [`geo-watch-2024-09-01-chilcotin-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-a/geo-watch-2024-09-01-chilcotin-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-201-d64e9bb3716b).
- [`geo-watch-2024-09-01-chilcotin-c`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-c.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-c/geo-watch-2024-09-01-chilcotin-c.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-202-d59ba811398b), [on reddit](https://www.reddit.com/r/bash/comments/1f9cvyx/a_bash_python_tool_to_watch_a_target_in_satellite/)..

## `elkhema ⛺️`

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-elkhema-2024-2024-10-05-a-b/geo-watch-elkhema-2024-2024-10-05-a-b-4X.gif?raw=true&random=ftcWc7s9ONu02HZS)
- [`geo-watch-elkhema-2024-2024-10-05-a-b`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-elkhema-2024-2024-10-05-a-b.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-elkhema-2024-2024-10-05-a-b/geo-watch-elkhema-2024-2024-10-05-a-b.gif), [dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-251-a68fab7f52b8).


