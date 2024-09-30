# 🌐 SkyFox

the `SkyFox` catalog covers [EDS (Earth Data Store)](https://earthdaily.github.io/EDA-Documentation/). see [datacube](../) for usage instructions.

 - [account](https://console.earthdaily.com/account)
 - [api use example](https://github.com/earthdaily/EDA-Documentation/blob/gh-pages/API/APIUsage/earthplatform_stac_api_examples.py)
 - [api](https://api.earthdaily.com/platform/v1/stac)
 - [doc](https://earthdaily.github.io/EDA-Documentation/)
 - [platform](https://console.earthdaily.com/platform)
 - [signin](https://console.earthdaily.com/mosaics/signin)
 - [venus bands](https://un-regard-sur-la-terre.org/2017/08/les-premieres-images-du-satellite-ven-s-sont-arrivees.html)
 - [venus mission](https://www.eoportal.org/satellite-missions/venus)
 - [venus on aws open data](https://registry.opendata.aws/venus-l2a-cogs/)
 - [venus wikipedia](https://en.wikipedia.org/wiki/VEN%CE%BCS)

## query

```bash
@catalog query SkyFox help
```
❗️ not found!

## case study: Leonardo da Vinci International Airport

- [ ] add example image 🔥

 - [Google Map](https://maps.app.goo.gl/Zpnj53kVcQQ4fNA17): `lat: 41.8003"N`, `lon: 12.2389"E`.
 - [Wikipedia](https://en.wikipedia.org/wiki/Rome_Fiumicino_Airport): The 9th busiest airport in Europe and the world's 46th-busiest airport with over 40.5 million passengers served in 2023.

---

details: [targets.yaml](../targets.yaml).


using [Leonardo](../../watch/targets/Leonardo.md).

## example run

🔥

```bash
@select
@catalog query SkyFox Venus - . \
  --count 10 \
  --datetime 2019-12-13/2020-10-28 \
  --lat  41.8003 \
  --lon 12.2389

@select $(@catalog query read - . --count 1 --offset 3)
@datacube ingest scope=metadata+rgbx .

@publish tar .
```

![image](...)

[....tar.gz](...)

- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-234-7ffa6d34230b)
