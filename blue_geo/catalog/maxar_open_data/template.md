# 🌐 Maxar Open Data (`maxar_open_data`)

The `maxar_open_data` catalog covers [Maxar's Open Data program](https://www.maxar.com/open-data/).

--urls--

## query

```bash
@catalog query maxar_open_data help
```
--help-- blue_geo catalog query maxar_open_data

## example use

```bash
@catalog query maxar_open_data select ingest - \
    --collection_id WildFires-LosAngeles-Jan-2025 \
    --start_date 2025-01-10 \
    --end_date 2025-01-13

@open QGIS .
@publish tar .
```

![image](https://github.com/kamangir/assets/blob/main/blue-geo/Maxar-Open-Datacube.png?raw=true)

[datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103030-1050010040277300.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/datacube-maxar_open_data-WildFires-LosAngeles-Jan-2025-11-031311103030-1050010040277300.tar.gz)