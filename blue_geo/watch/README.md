# 🌐 `@geo watch`

watch the planet's story unfold.


```bash
@geo watch help
```
<details>
<summary></summary>

```bash
@geo \
	watch \
	[batch,dryrun,name=<job-name>] \
	[<query-object-name> | target=<target>] \
	[algo=<algo>,<algo-options>] \
	[~submit | dryrun,to=<runner>] \
	[dryrun,<map-options>] \
	[content=<0.5>,dryrun,~gif,publish,<reduce-options>] \
	[-|<object-name>]
 . watch target -> <object-name>.
   algo: diff | modality
   <algo-options>:
      diff: modality=<modality>,range=<100.0>
      modality: modality=<modality>
   modality: rgb[@<keyword>]
   runner: aws_batch | generic | local
   target: Altadena | Altadena-test | Brown-Mountain-Truck-Trail | Brown-Mountain-Truck-Trail-all | Brown-Mountain-Truck-Trail-test | Cache-Creek | Cache-Creek-2x-wider | Cache-Creek-test | DrugSuperLab | DrugSuperLab-200 | DrugSuperLab-test | Fagradalsfjall | Hurricane-Idalia-2023 | Jasper | LA | LA-250 | LA-test | Leonardo | Leonardo-test | Leonardo-test-focus | Mount-Etna | Noto | Noto-250 | Noto-test | Palisades-Maxar | Palisades-Maxar-test | Palisades-Sentinel-2 | Palisades-Sentinel-2-test | Sheerness | Sheerness-10x | Sheerness-20x | Sheerness-test | Silver-Peak | Silver-Peak-test | bellingcat-2024-09-27-nagorno-karabakh | bellingcat-2024-09-27-nagorno-karabakh-2X | bellingcat-2024-09-27-nagorno-karabakh-6X | bellingcat-2024-09-27-nagorno-karabakh-6X-test | bellingcat-2024-09-27-nagorno-karabakh-test | burning-man-2024 | chilcotin-river-landslide | chilcotin-river-landslide-test | elkhema | elkhema-2024
@geo \
	watch \
	batch,dryrun,name=<job-name> \
	[<query-object-name> | target=<target>] \
	[algo=<algo>,<algo-options>] \
	[~submit | dryrun,to=<runner>] \
	[dryrun,<map-options>] \
	[content=<0.5>,dryrun,~gif,publish,<reduce-options>] \
	[-|<object-name>]
 . watch target -aws-batch-> <object-name>.
   algo: diff | modality
   <algo-options>:
      diff: modality=<modality>,range=<100.0>
      modality: modality=<modality>
   modality: rgb[@<keyword>]
   runner: aws_batch | generic | local
   target: Altadena | Altadena-test | Brown-Mountain-Truck-Trail | Brown-Mountain-Truck-Trail-all | Brown-Mountain-Truck-Trail-test | Cache-Creek | Cache-Creek-2x-wider | Cache-Creek-test | DrugSuperLab | DrugSuperLab-200 | DrugSuperLab-test | Fagradalsfjall | Hurricane-Idalia-2023 | Jasper | LA | LA-250 | LA-test | Leonardo | Leonardo-test | Leonardo-test-focus | Mount-Etna | Noto | Noto-250 | Noto-test | Palisades-Maxar | Palisades-Maxar-test | Palisades-Sentinel-2 | Palisades-Sentinel-2-test | Sheerness | Sheerness-10x | Sheerness-20x | Sheerness-test | Silver-Peak | Silver-Peak-test | bellingcat-2024-09-27-nagorno-karabakh | bellingcat-2024-09-27-nagorno-karabakh-2X | bellingcat-2024-09-27-nagorno-karabakh-6X | bellingcat-2024-09-27-nagorno-karabakh-6X-test | bellingcat-2024-09-27-nagorno-karabakh-test | burning-man-2024 | chilcotin-river-landslide | chilcotin-river-landslide-test | elkhema | elkhema-2024
@geo \
	watch \
	map \
	[algo=<algo>,dryrun,~download,modality=<modality>,offset=<offset>,suffix=<suffix>,~upload] \
	[.|<query-object-name>]
 . @geo watch map <query-object-name> @ <offset> -> /<suffix>.
@geo \
	watch \
	query \
	[dryrun,target=<target>,~upload] \
	[.|<object-name>]
 . query target -> <object-name>.
@geo \
	watch \
	reduce \
	[algo=<algo>dryrun,~download,publish,suffix=<suffix>,~upload] \
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
   object: $BLUE_GEO_WATCH_TARGET_LIST
@targets edit
 . edit watch targets.
   /Users/kamangir/storage/abcli/blue-geo-target-list-v1/metadata.yaml
   object: $BLUE_GEO_WATCH_TARGET_LIST
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
	[~QGIS,template]
 . open targets.
@targets publish \
	[template]
 . publish watch targets.
@targets save \
	[target=all|<target-name>] \
	[.|<object-name>]
 . save target(s) -> <object-name>.
   template: $BLUE_GEO_QGIS_TEMPLATE_WATCH
@targets test
 . test watch targets.
@targets update_template \
	[~download,target=all|<target-name>,~upload]
 . update target template.
@targets upload
 . upload watch targets.
   object: $BLUE_GEO_WATCH_TARGET_LIST
```

</details>



## targets 🎯

- [`targets.geojson`](./targets.geojson)
- list of targets: [blue-geo-target-list-v1.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/blue-geo-target-list-v1.tar.gz)
- template: [blue_geo_watch_template_v1.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/blue_geo_watch_template_v1.tar.gz)

## example run

```bash
@geo watch \
  batch \
  target=elkhema-2024 - \
  to=aws_batch - \
  publish \
  geo-watch-elkhema-2024-2024-10-05-a-b
```

[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-252-2118326b1de2).

ℹ️ suffix published gif urls with `-2X` and `-4X` for different scales. example: [1X](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b.gif), [2X](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b-2X.gif), [4X](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b-4X.gif).

## `Cache-Creek`

<details>
<summary>🌐</summary>

[![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2x-wider-2024-11-05/geo-watch-Cache-Creek-2x-wider-2024-11-05-4X.gif?raw=true&random=ub2b5tkevkw0wd1q)](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2x-wider-2024-11-05/geo-watch-Cache-Creek-2x-wider-2024-11-05.gif)

</details>

 - [Google Maps](https://maps.app.goo.gl/kHypmxiEeqdVrBi77): `lat: 56.2036"N`, `lon: 120.8943"W`.
 - [reddit](https://www.reddit.com/r/britishcolumbia/comments/1fho5vq/10_days_of_reservoir_filling_at_cache_creek_site/): 10 Days of reservoir filling at Cache Creek - Site C Hydroelectric Project, British Columbia, Canada.
- [`geo-watch-Cache-Creek-2024-10-06-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2024-10-06-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2024-10-06-a/geo-watch-Cache-Creek-2024-10-06-a.gif).
- [`geo-watch-Cache-Creek-2x-wider-2024-10-06-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2x-wider-2024-10-06-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2x-wider-2024-10-06-a/geo-watch-Cache-Creek-2x-wider-2024-10-06-a.gif).
- [`geo-watch-Cache-Creek-2024-11-05`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2024-11-05.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2024-11-05/geo-watch-Cache-Creek-2024-11-05.gif).
- [`geo-watch-Cache-Creek-2x-wider-2024-11-05`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2x-wider-2024-11-05.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Cache-Creek-2x-wider-2024-11-05/geo-watch-Cache-Creek-2x-wider-2024-11-05.gif).

## [`DrugSuperLab`](./targets/md/DrugSuperLab.md)

<details>
<summary>🌐</summary>

[![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/DrugSuperLab-2024-12-09-ZnmC5L/DrugSuperLab-2024-12-09-ZnmC5L-4X.gif?raw=true&random=owtidqyb3uj902dj)](https://kamangir-public.s3.ca-central-1.amazonaws.com/DrugSuperLab-2024-12-09-ZnmC5L/DrugSuperLab-2024-12-09-ZnmC5L.gif)

</details>

 - [CBC](https://www.cbc.ca/news/canada/british-columbia/drug-superlab-rcmp-bust-falkland-1.7371488): Sleepy little Falkland, B.C., awakes to big news of superlab drug bust
 - [Google Maps](https://maps.app.goo.gl/errDohJAuedpNibs7): `lat: 50.4505"N`, `lon: 119.5060"W`.
 - [RCMP](https://bc-cb.rcmp-grc.gc.ca/ViewPage.action?siteNodeId=2087&languageId=1&contentId=85957): Federal Investigators take down the largest, most sophisticated drug superlab in Canada
 - [YouTube](https://youtu.be/t-POttDl8UQ?t=1876)
- [`geo-watch-DrugSuperLab-2024-11-19-13954`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-DrugSuperLab-2024-11-19-13954.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-DrugSuperLab-2024-11-19-13954/geo-watch-DrugSuperLab-2024-11-19-13954.gif), known issues: successive frames may have different projections..
- [`DrugSuperLab-2024-12-08-pGErp2`](https://kamangir-public.s3.ca-central-1.amazonaws.com/DrugSuperLab-2024-12-08-pGErp2.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/DrugSuperLab-2024-12-08-pGErp2/DrugSuperLab-2024-12-08-pGErp2.gif).
- [`DrugSuperLab-2024-12-09-ZnmC5L`](https://kamangir-public.s3.ca-central-1.amazonaws.com/DrugSuperLab-2024-12-09-ZnmC5L.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/DrugSuperLab-2024-12-09-ZnmC5L/DrugSuperLab-2024-12-09-ZnmC5L.gif).

## [`Fagradalsfjall`](./targets/md/Fagradalsfjall.md)

<details>
<summary>🌐</summary>

[![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Fagradalsfjall-a/geo-watch-2024-09-04-Fagradalsfjall-a-2X.gif?raw=true&random=2mee9hsdzssjemhn)](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Fagradalsfjall-a/geo-watch-2024-09-04-Fagradalsfjall-a.gif)

</details>

 - [Google Maps](https://maps.app.goo.gl/zkdc2DNLahc598k48): `lat: 63.9000"N`, `lon: 22.2667"W`.
 - [Wikipedia](https://en.wikipedia.org/wiki/Fagradalsfjall): An active tuya volcano formed in the Last Glacial Period on the Reykjanes Peninsula.
- [`geo-watch-2024-09-04-Fagradalsfjall-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Fagradalsfjall-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Fagradalsfjall-a/geo-watch-2024-09-04-Fagradalsfjall-a.gif).

## [`Jasper`](./targets/md/Jasper.md)

<details>
<summary>🌐</summary>

[![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Jasper-2024-11-03/geo-watch-Jasper-2024-11-03-2X.gif?raw=true&random=mwcl82z5boh2j6l1)](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Jasper-2024-11-03/geo-watch-Jasper-2024-11-03.gif)

</details>

 - [Google Maps](https://maps.app.goo.gl/o5tGW4tH5S6j4vso9): `lat: 52.8734"N`, `lon: 118.0814"W`.
 - [Parks Canada](https://parks.canada.ca/pn-np/ab/jasper/visit/feu-alert-fire/feudeforet-wildfire): Wildfire status, Jasper Wildfire Complex.
 - [Wikipedia](https://en.wikipedia.org/wiki/2024_Jasper_wildfire)
- [`geo-watch-2024-09-06-Jasper-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-06-Jasper-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-06-Jasper-a/geo-watch-2024-09-06-Jasper-a.gif).
- [`geo-watch-Jasper-2024-11-03`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Jasper-2024-11-03.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Jasper-2024-11-03/geo-watch-Jasper-2024-11-03.gif).

## [`Leonardo`](./targets/md/Leonardo.md)

<details>
<summary>🌐</summary>

[![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-10-27-16-17-36-12059/geo-watch-2024-10-27-16-17-36-12059-4X.gif?raw=true&random=e0npr3rb1xggqdql)](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-10-27-16-17-36-12059/geo-watch-2024-10-27-16-17-36-12059.gif)

</details>

 - [Google Maps](https://maps.app.goo.gl/Zpnj53kVcQQ4fNA17): `lat: 41.8150"N`, `lon: 12.2550"E`.
 - [Wikipedia](https://en.wikipedia.org/wiki/Rome_Fiumicino_Airport): The 9th busiest airport in Europe and the world's 46th-busiest airport with over 40.5 million passengers served in 2023.
- [`test_blue_geo_watch_v4-diff-Leonardo-test`](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v4-diff-Leonardo-test.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v4-diff-Leonardo-test/test_blue_geo_watch_v4-diff-Leonardo-test.gif), [![bashtest](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml).
- [`test_blue_geo_watch_v4-modality-Leonardo-test`](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v4-modality-Leonardo-test.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v4-modality-Leonardo-test/test_blue_geo_watch_v4-modality-Leonardo-test.gif), [![bashtest](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml).
- [`geo-watch-2024-09-30-Leonardo-g`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-30-Leonardo-g.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-30-Leonardo-g/geo-watch-2024-09-30-Leonardo-g.gif).
- [`geo-watch-Leonardo-2024-10-05-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Leonardo-2024-10-05-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Leonardo-2024-10-05-a/geo-watch-Leonardo-2024-10-05-a.gif).
- [`geo-watch-Leonardo-2024-10-06-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Leonardo-2024-10-06-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Leonardo-2024-10-06-a/geo-watch-Leonardo-2024-10-06-a.gif).
- [`geo-watch-2024-10-27-16-17-36-12059`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-10-27-16-17-36-12059.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-10-27-16-17-36-12059/geo-watch-2024-10-27-16-17-36-12059.gif).

## [`Mount-Etna`](./targets/md/Mount-Etna.md)

<details>
<summary>🌐</summary>

[![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Mount-Etna-a/geo-watch-2024-09-04-Mount-Etna-a-2X.gif?raw=true&random=hanajrp4v7zinngg)](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Mount-Etna-a/geo-watch-2024-09-04-Mount-Etna-a.gif)

</details>

 - [Google Maps](https://maps.app.goo.gl/vcCRk16tHBPxB3a47): `lat: 37.7510"N`, `lon: 14.9934"E`.
 - [Wikipedia](https://en.wikipedia.org/wiki/Mount_Etna): An active stratovolcano on the east coast of Sicily, Italy.
- [`geo-watch-2024-09-04-Mount-Etna-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Mount-Etna-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-Mount-Etna-a/geo-watch-2024-09-04-Mount-Etna-a.gif).

## [`Palisades`](./targets/md/Palisades.md)

<details>
<summary>🌐</summary>

[![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/Palisades-Sentinel-2-2025-01-15-16-50-38-vyjxu8/Palisades-Sentinel-2-2025-01-15-16-50-38-vyjxu8-2X.gif?raw=true&random=ffsij4plphetdzx1)](https://kamangir-public.s3.ca-central-1.amazonaws.com/Palisades-Sentinel-2-2025-01-15-16-50-38-vyjxu8/Palisades-Sentinel-2-2025-01-15-16-50-38-vyjxu8.gif)

</details>

 - [3d map](https://calfire-forestry.maps.arcgis.com/home/webscene/viewer.html?webscene=0a7381c8b46b4e26a057383424f32c06)
 - [calfire](https://www.fire.ca.gov/incidents/2025/1/7/palisades-fire)
 - [wikipedia](https://en.wikipedia.org/wiki/January_2025_Southern_California_wildfires): January 2025 Southern California wildfires
- [`Palisades-Sentinel-2-2025-01-15-16-50-38-vyjxu8`](https://kamangir-public.s3.ca-central-1.amazonaws.com/Palisades-Sentinel-2-2025-01-15-16-50-38-vyjxu8.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/Palisades-Sentinel-2-2025-01-15-16-50-38-vyjxu8/Palisades-Sentinel-2-2025-01-15-16-50-38-vyjxu8.gif).

## `Sheerness`

<details>
<summary>🌐</summary>

[![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/Sheerness-20x-2024-12-14-EDkXl0/Sheerness-20x-2024-12-14-EDkXl0-4X.gif?raw=true&random=58c49cppmeik5ofe)](https://kamangir-public.s3.ca-central-1.amazonaws.com/Sheerness-20x-2024-12-14-EDkXl0/Sheerness-20x-2024-12-14-EDkXl0.gif)

</details>

 - [source](https://datasets.wri.org/datasets/global-power-plant-database): Global Power Plant Database
- [`Sheerness-20x-2024-12-09-S8xKmn`](https://kamangir-public.s3.ca-central-1.amazonaws.com/Sheerness-20x-2024-12-09-S8xKmn.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/Sheerness-20x-2024-12-09-S8xKmn/Sheerness-20x-2024-12-09-S8xKmn.gif), half-blank frames, will rerun with content-ratio > 0.6..
- [`Sheerness-20x-2024-12-14-EDkXl0`](https://kamangir-public.s3.ca-central-1.amazonaws.com/Sheerness-20x-2024-12-14-EDkXl0.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/Sheerness-20x-2024-12-14-EDkXl0/Sheerness-20x-2024-12-14-EDkXl0.gif).

## `Silver-Peak`

<details>
<summary>🌐</summary>

[![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Silver-Peak-2024-10-12-a/geo-watch-Silver-Peak-2024-10-12-a-4X.gif?raw=true&random=vlb2fbo0vi7j79lt)](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Silver-Peak-2024-10-12-a/geo-watch-Silver-Peak-2024-10-12-a.gif)

</details>

 - [Google Maps](https://maps.app.goo.gl/SxT1z4LgLUTSVNp89): `lat: 46.1101"N`, `lon: 81.2822"W`.
 - [Wikipedia](https://en.wikipedia.org/wiki/Silver_Peak_(Ontario)): Silver Peak is a mountain located at Killarney Provincial Park, Ontario, Canada.
 - [pdf](https://files.ontario.ca/ndmnrf-geotours-1/ndmnrf-geotours-killarney-en-2021-12-13.pdf): Famous Canadian Shield White Mountains and Pink Shores.
- [`geo-watch-Silver-Peak-2024-10-12-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Silver-Peak-2024-10-12-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Silver-Peak-2024-10-12-a/geo-watch-Silver-Peak-2024-10-12-a.gif).

## `bellingcat-2024-09-27-nagorno-karabakh`

<details>
<summary>🌐</summary>

[![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-6X-2024-12-14-EUUpS1/bellingcat-2024-09-27-nagorno-karabakh-6X-2024-12-14-EUUpS1-4X.gif?raw=true&random=w7bedh3uvhknb9yr)](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-6X-2024-12-14-EUUpS1/bellingcat-2024-09-27-nagorno-karabakh-6X-2024-12-14-EUUpS1.gif)

</details>

 - [Bellingcat](https://www.bellingcat.com/news/mena/2024/09/27/nagorno-karabakh-satellite-imagery-shows-city-wide-ransacking/): In the regional capital of Nagorno-Karabakh, satellite imagery reveals hundreds of incidents of what appears to be ransacking across the city of Khankendi, known as Stepanakert to Armenians.
- [`bellingcat-2024-09-27-nagorno-karabakh-2024-10-01-c-b`](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-2024-10-01-c-b.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-2024-10-01-c-b/bellingcat-2024-09-27-nagorno-karabakh-2024-10-01-c-b.gif).
- [`bellingcat-2024-09-27-nagorno-karabakh-b`](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-b.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-b/bellingcat-2024-09-27-nagorno-karabakh-b.gif).
- [`bellingcat-2024-09-27-nagorno-karabakh-6X-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-6X-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-6X-a/bellingcat-2024-09-27-nagorno-karabakh-6X-a.gif).
- [`geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b.gif).
- [`geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a/geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a.gif).
- [`bellingcat-2024-09-27-nagorno-karabakh-6X-2024-12-14-EUUpS1`](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-6X-2024-12-14-EUUpS1.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/bellingcat-2024-09-27-nagorno-karabakh-6X-2024-12-14-EUUpS1/bellingcat-2024-09-27-nagorno-karabakh-6X-2024-12-14-EUUpS1.gif).

## [`burning-man-2024`](./targets/md/burning-man-2024.md)

<details>
<summary>🌐</summary>

[![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-burning-man-2024-a/geo-watch-2024-09-04-burning-man-2024-a-2X.gif?raw=true&random=n3xyblpkzubb2ika)](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-burning-man-2024-a/geo-watch-2024-09-04-burning-man-2024-a.gif)

</details>

 - [Google Maps](https://maps.app.goo.gl/e58UsDThr8ryqCRa8): `lat: 40.7864"N`, `lon: 119.2065"W`.
- [`geo-watch-2024-09-04-burning-man-2024-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-burning-man-2024-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-04-burning-man-2024-a/geo-watch-2024-09-04-burning-man-2024-a.gif).

## [`chilcotin-river-landslide`](./targets/md/chilcotin-river-landslide.md)

<details>
<summary>🌐</summary>

[![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Chilcotin-2024-11-03/geo-watch-Chilcotin-2024-11-03-4X.gif?raw=true&random=zg5ovzr8zuxdibei)](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Chilcotin-2024-11-03/geo-watch-Chilcotin-2024-11-03.gif)

</details>

 - [Google Maps](https://maps.app.goo.gl/WHTNCDsFNoZAAnzX8): `lat: 51.8472"N`, `lon: 122.7903"W`.
 - [Nasa](https://www.bluemarble.nasa.gov/images/153195/chilcotin-rivers-landslide-lake-begins-draining): Chilcotin River’s Landslide Lake Begins Draining.
 - [Reddit](https://www.reddit.com/r/britishcolumbia/comments/1eh9eql/before_and_after_satellite_images_of_the/): Before and after satellite images of the Chilcotin River landslide.
 - [portal](https://chilcotin-river-landslide-2024-bcgov03.hub.arcgis.com/): Chilcotin River Landslide Information Portal, source of ⬆️ image.
- [`test_blue_geo_watch_v4-diff-chilcotin-river-landslide-test`](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v4-diff-chilcotin-river-landslide-test.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v4-diff-chilcotin-river-landslide-test/test_blue_geo_watch_v4-diff-chilcotin-river-landslide-test.gif), [![bashtest](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml).
- [`test_blue_geo_watch_v4-modality-chilcotin-river-landslide-test`](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v4-modality-chilcotin-river-landslide-test.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_blue_geo_watch_v4-modality-chilcotin-river-landslide-test/test_blue_geo_watch_v4-modality-chilcotin-river-landslide-test.gif), [![bashtest](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/blue-geo/actions/workflows/bashtest.yml).
- [`geo-watch-2024-08-31-chilcotin-c`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-08-31-chilcotin-c.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-08-31-chilcotin-c/geo-watch-2024-08-31-chilcotin-c.gif), L1C and L2A mixed, `2024-07-30/2024-08-09`.
- [`geo-watch-2024-09-01-chilcotin-a`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-a.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-a/geo-watch-2024-09-01-chilcotin-a.gif).
- [`geo-watch-2024-09-01-chilcotin-c`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-c.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-2024-09-01-chilcotin-c/geo-watch-2024-09-01-chilcotin-c.gif), [on reddit](https://www.reddit.com/r/bash/comments/1f9cvyx/a_bash_python_tool_to_watch_a_target_in_satellite/)..
- [`geo-watch-Chilcotin-2024-11-03`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Chilcotin-2024-11-03.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-Chilcotin-2024-11-03/geo-watch-Chilcotin-2024-11-03.gif).

## `elkhema ⛺️`

<details>
<summary>🌐</summary>

[![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/elkhema-2024-12-15-8EqPXl/elkhema-2024-12-15-8EqPXl-4X.gif?raw=true&random=zekgscnn8pmwqqf8)](https://kamangir-public.s3.ca-central-1.amazonaws.com/elkhema-2024-12-15-8EqPXl/elkhema-2024-12-15-8EqPXl.gif)

</details>

- [`geo-watch-elkhema-2024-2024-10-05-a-b`](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-elkhema-2024-2024-10-05-a-b.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/geo-watch-elkhema-2024-2024-10-05-a-b/geo-watch-elkhema-2024-2024-10-05-a-b.gif).
- [`elkhema-2024-12-15-8EqPXl`](https://kamangir-public.s3.ca-central-1.amazonaws.com/elkhema-2024-12-15-8EqPXl.tar.gz), [gif](https://kamangir-public.s3.ca-central-1.amazonaws.com/elkhema-2024-12-15-8EqPXl/elkhema-2024-12-15-8EqPXl.gif).


