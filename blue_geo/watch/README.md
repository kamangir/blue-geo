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
   target: Cache-Creek|Cache-Creek-2x-wider|Cache-Creek-test|Fagradalsfjall|Hurricane-Idalia-2023|Jasper|Leonardo|Leonardo-test|Mount-Etna|bellingcat-2024-09-27-nagorno-karabakh|bellingcat-2024-09-27-nagorno-karabakh-2X|bellingcat-2024-09-27-nagorno-karabakh-6X|bellingcat-2024-09-27-nagorno-karabakh-6X-test|bellingcat-2024-09-27-nagorno-karabakh-test|burning-man-2024|chilcotin-river-landslide|chilcotin-river-landslide-test|elkhema|elkhema-2024
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
   target: Cache-Creek|Cache-Creek-2x-wider|Cache-Creek-test|Fagradalsfjall|Hurricane-Idalia-2023|Jasper|Leonardo|Leonardo-test|Mount-Etna|bellingcat-2024-09-27-nagorno-karabakh|bellingcat-2024-09-27-nagorno-karabakh-2X|bellingcat-2024-09-27-nagorno-karabakh-6X|bellingcat-2024-09-27-nagorno-karabakh-6X-test|bellingcat-2024-09-27-nagorno-karabakh-test|burning-man-2024|chilcotin-river-landslide|chilcotin-river-landslide-test|elkhema|elkhema-2024
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
@targets download \
	[open,QGIS]
 . download watch targets.
   $BLUE_GEO_WATCH_TARGET_LIST: blue-geo-target-list-v1
@targets edit
 . edit watch targets.
   /Users/kamangir/storage/abcli/blue-geo-target-list-v1/metadata.yaml
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
@targets open \
	[QGIS]
 . open targets.
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

🎯 [`geo-watch-targets/`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-targets.tar.gz): [geojson](./targets.geojson).

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
 - [Google Maps](https://maps.app.goo.gl/kHypmxiEeqdVrBi77): `lat: 56.2036"N`, `lon: 120.8943"W`.
 - [reddit](https://www.reddit.com/r/britishcolumbia/comments/1fho5vq/10_days_of_reservoir_filling_at_cache_creek_site/): 10 Days of reservoir filling at Cache Creek - Site C Hydroelectric Project, British Columbia, Canada.

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2x-wider-2024-10-06-a/geo-watch-Cache-Creek-2x-wider-2024-10-06-a-4X.gif?raw=true&random=D2yN7M9rKWmXhIfV)
- [`geo-watch-Cache-Creek-2024-10-06-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2024-10-06-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2024-10-06-a/geo-watch-Cache-Creek-2024-10-06-a.gif), [dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-253-8f12ef5bd8fc).
- [`geo-watch-Cache-Creek-2x-wider-2024-10-06-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2x-wider-2024-10-06-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2x-wider-2024-10-06-a/geo-watch-Cache-Creek-2x-wider-2024-10-06-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-256-c1b564c9f89e).

## [`Fagradalsfjall`](./targets/md/Fagradalsfjall.md)
 - [Google Maps](https://maps.app.goo.gl/zkdc2DNLahc598k48): `lat: 63.9000"N`, `lon: 22.2667"W`.
 - [Wikipedia](https://en.wikipedia.org/wiki/Fagradalsfjall): An active tuya volcano formed in the Last Glacial Period on the Reykjanes Peninsula.

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Fagradalsfjall-a/geo-watch-2024-09-04-Fagradalsfjall-a-2X.gif?raw=true&random=PvIejYALvKIH5CZk)
- [`geo-watch-2024-09-04-Fagradalsfjall-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Fagradalsfjall-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Fagradalsfjall-a/geo-watch-2024-09-04-Fagradalsfjall-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-206-f7996520dc15).

## [`Jasper`](./targets/md/Jasper.md)
 - [Google Maps](https://maps.app.goo.gl/o5tGW4tH5S6j4vso9): `lat: 52.8734"N`, `lon: 118.0814"W`.
 - [Parks Canada](https://parks.canada.ca/pn-np/ab/jasper/visit/feu-alert-fire/feudeforet-wildfire): Wildfire status, Jasper Wildfire Complex.
 - [Wikipedia](https://en.wikipedia.org/wiki/2024_Jasper_wildfire)

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-06-Jasper-a/geo-watch-2024-09-06-Jasper-a-2X.gif?raw=true&random=EEOLX3hsCfHvzQtn)
- [`geo-watch-2024-09-06-Jasper-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-06-Jasper-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-06-Jasper-a/geo-watch-2024-09-06-Jasper-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-208-7063fca1423b).

## [`Leonardo`](./targets/md/Leonardo.md)
 - [Google Maps](https://maps.app.goo.gl/Zpnj53kVcQQ4fNA17): `lat: 41.8150"N`, `lon: 12.2550"E`.
 - [Wikipedia](https://en.wikipedia.org/wiki/Rome_Fiumicino_Airport): The 9th busiest airport in Europe and the world's 46th-busiest airport with over 40.5 million passengers served in 2023.

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Leonardo-2024-10-06-a/geo-watch-Leonardo-2024-10-06-a-4X.gif?raw=true&random=36t9hfK87xtHPVOT)
- [`test_blue_geo_watch_v4-Leonardo-test`](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v4-Leonardo-test.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v4-Leonardo-test/test_blue_geo_watch_v4-Leonardo-test.gif), [![bashtest](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml).
- [`geo-watch-2024-09-30-Leonardo-g`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-30-Leonardo-g.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-30-Leonardo-g/geo-watch-2024-09-30-Leonardo-g.gif), [dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-237-99db71023445).
- [`geo-watch-Leonardo-2024-10-05-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Leonardo-2024-10-05-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Leonardo-2024-10-05-a/geo-watch-Leonardo-2024-10-05-a.gif), [dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-249-44ba1dcd2321).
- [`geo-watch-Leonardo-2024-10-06-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Leonardo-2024-10-06-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Leonardo-2024-10-06-a/geo-watch-Leonardo-2024-10-06-a.gif), [dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-255-1f2a8f1ccef5).

## [`Mount-Etna`](./targets/md/Mount-Etna.md)
 - [Google Maps](https://maps.app.goo.gl/vcCRk16tHBPxB3a47): `lat: 37.7510"N`, `lon: 14.9934"E`.
 - [Wikipedia](https://en.wikipedia.org/wiki/Mount_Etna): An active stratovolcano on the east coast of Sicily, Italy.

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Mount-Etna-a/geo-watch-2024-09-04-Mount-Etna-a-2X.gif?raw=true&random=gNnsrMkH0hQOgVJm)
- [`geo-watch-2024-09-04-Mount-Etna-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Mount-Etna-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Mount-Etna-a/geo-watch-2024-09-04-Mount-Etna-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-205-c272a95ce266).

## `bellingcat-2024-09-27-nagorno-karabakh`
 - [Bellingcat](https://www.bellingcat.com/news/mena/2024/09/27/nagorno-karabakh-satellite-imagery-shows-city-wide-ransacking/): In the regional capital of Nagorno-Karabakh, satellite imagery reveals hundreds of incidents of what appears to be ransacking across the city of Khankendi, known as Stepanakert to Armenians.

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a-4X.gif?raw=true&random=uhDIEpoS2ayLgU8V)
- [`bellingcat-2024-09-27-nagorno-karabakh-2024-10-01-c-b`](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-2024-10-01-c-b.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-2024-10-01-c-b/bellingcat-2024-09-27-nagorno-karabakh-2024-10-01-c-b.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-241-3e25857747a5).
- [`bellingcat-2024-09-27-nagorno-karabakh-b`](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-b.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-b/bellingcat-2024-09-27-nagorno-karabakh-b.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-244-a5f9b7959748).
- [`bellingcat-2024-09-27-nagorno-karabakh-6X-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-6X-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-6X-a/bellingcat-2024-09-27-nagorno-karabakh-6X-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-245-18f6d15e5fbd).
- [`geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b.gif), [dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-250-847d3d5f0d6e).
- [`geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a.gif), [dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-255-1f2a8f1ccef5).

## [`burning-man-2024`](./targets/md/burning-man-2024.md)
 - [Google Maps](https://maps.app.goo.gl/e58UsDThr8ryqCRa8): `lat: 40.7864"N`, `lon: 119.2065"W`.

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-burning-man-2024-a/geo-watch-2024-09-04-burning-man-2024-a-2X.gif?raw=true&random=mehrwQNZ24Sz29ck)
- [`geo-watch-2024-09-04-burning-man-2024-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-burning-man-2024-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-burning-man-2024-a/geo-watch-2024-09-04-burning-man-2024-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-205-c272a95ce266).

## [`chilcotin-river-landslide`](./targets/md/chilcotin-river-landslide.md)
 - [Google Maps](https://maps.app.goo.gl/WHTNCDsFNoZAAnzX8): `lat: 51.8472"N`, `lon: 122.7903"W`.
 - [Nasa](https://www.bluemarble.nasa.gov/images/153195/chilcotin-rivers-landslide-lake-begins-draining): Chilcotin River’s Landslide Lake Begins Draining.
 - [Reddit](https://www.reddit.com/r/britishcolumbia/comments/1eh9eql/before_and_after_satellite_images_of_the/): Before and after satellite images of the Chilcotin River landslide.
 - [portal](https://chilcotin-river-landslide-2024-bcgov03.hub.arcgis.com/): Chilcotin River Landslide Information Portal, source of ⬆️ image.

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-c/geo-watch-2024-09-01-chilcotin-c-2X.gif?raw=true&random=0GiNdOiRXwFb1PHW)
- [`test_blue_geo_watch_v4-chilcotin-river-landslide-test`](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v4-chilcotin-river-landslide-test.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v4-chilcotin-river-landslide-test/test_blue_geo_watch_v4-chilcotin-river-landslide-test.gif), [![bashtest](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml).
- [`geo-watch-2024-08-31-chilcotin-c`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-08-31-chilcotin-c.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-08-31-chilcotin-c/geo-watch-2024-08-31-chilcotin-c.gif), L1C and L2A mixed, `2024-07-30/2024-08-09`, [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-199-11f9b5497ef0).
- [`geo-watch-2024-09-01-chilcotin-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-a/geo-watch-2024-09-01-chilcotin-a.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-201-d64e9bb3716b).
- [`geo-watch-2024-09-01-chilcotin-c`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-c.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-c/geo-watch-2024-09-01-chilcotin-c.gif), [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-202-d59ba811398b), [on reddit](https://www.reddit.com/r/bash/comments/1f9cvyx/a_bash_python_tool_to_watch_a_target_in_satellite/)..

## `elkhema ⛺️`

![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-elkhema-2024-2024-10-05-a-b/geo-watch-elkhema-2024-2024-10-05-a-b-4X.gif?raw=true&random=dL9ZhCEfVqRAOPNS)
- [`geo-watch-elkhema-2024-2024-10-05-a-b`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-elkhema-2024-2024-10-05-a-b.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-elkhema-2024-2024-10-05-a-b/geo-watch-elkhema-2024-2024-10-05-a-b.gif), [dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-251-a68fab7f52b8).


