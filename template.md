# 🌐 Blue-GEO (`@geo`)

🌐 AI for a Blue Planet.

```bash
pip install blue-geo
```

```mermaid
graph LR
    catalog_browse["@catalog browse <catalog-name> <resource>"]

    catalog_get["@catalog get~~<thing> --catalog~~<catalog>"]

    catalog_list_catalogs["@catalog list~~catalogs"]

    catalog_list["@catalog list~~collections|datacube_classes --catalog~~<catalog>"]

    catalog_query["@catalog query <catalog-name> <collection-name>~~- <query-object-name>"]

    catalog_query_ingest["@catalog query <catalog-name> <collection-name> ingest,scope=<scope> <query-object-name>"]

    catalog_query_read["@catalog query read~~- <query-object-name>"]

    catalog_query_ingest["@catalog query ingest~~- <query-object-name> scope=<scope>"]

    datacube_crop["@datacube crop~~- <object-name> <datacube-id>"]

    datacube_get["@datacube get catalog <datacube-id>"]

    datacube_ingest["@datacube ingest scope=<scope> <datacube-id>"]

    datacube_label["@datacube label~~- <datacube-id>"]

    datacube_list["@datacube list <datacube-id> --scope~~<scope>"]

    geo_watch["@geo~~watch batch <query-object-name>|target=<target>~~- to=<runner>~~-~~- <object-name>"]

    catalog["🌐 catalog"]:::folder
    datacube["🧊 datacube"]:::folder
    terminal["💻 terminal"]:::folder
    QGIS["🖼️ QGIS"]:::folder
    query_object["📂 query object"]:::folder
    object["📂 object"]:::folder
    target["🎯 target"]:::folder

    catalog_list_catalogs --> terminal

    catalog --> catalog_browse
    catalog_browse --> terminal

    catalog --> catalog_get
    catalog_get --> terminal

    catalog --> catalog_list
    catalog_list --> terminal

    catalog --> catalog_query
    catalog_query --> query_object

    catalog --> catalog_query_ingest
    catalog_query_ingest --> query_object
    catalog_query_ingest --> datacube

    query_object --> catalog_query_read
    catalog_query_read --> datacube

    query_object --> catalog_query_ingest
    catalog_query_ingest --> datacube

    datacube --> datacube_crop
    target --> datacube_crop
    datacube_crop --> datacube

    datacube --> datacube_get
    datacube_get --> terminal

    datacube --> datacube_ingest
    datacube_ingest --> datacube

    datacube --> datacube_list
    datacube_list --> terminal

    datacube --> datacube_label
    datacube_label --> QGIS
    datacube_label --> datacube

    query_object --> geo_watch
    target --> geo_watch
    geo_watch --> object

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

--table--

---

📜 [metadata](./metadata.yaml)

🎁 [wish list and bugs](https://github.com/kamangir/blue-geo/issues/8)

--signature--