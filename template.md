# 🌐 Blue-GEO (`@geo`)

🌐 AI for a Blue Planet.

```bash
pip install blue-geo
```

```mermaid
graph LR
    catalog_browse["@catalog browse <catalog-name> <resource>"]
    catalog_get["@catalog get~<thing> --catalog~<catalog>"]
    catalog_list_catalogs["@catalog list~catalogs"]
    catalog_list["@catalog list~collections|datacube_classes --catalog~<catalog>"]
    catalog_query["@catalog query <catalog-name> <collection-name> scope=<scope> <query-object-name>"]
    catalog_query_read["@catalog query read~- <query-object-name>"]

    datacube_crop["@datacube crop~- <object-name> <datacube-id>"]
    datacube_get["@datacube get catalog <datacube-id>"]
    datacube_ingest["@datacube ingest scope=<scope> <datacube-id>"]
    datacube_list["@datacube list <datacube-id> --scope~<scope>"]

    catalog["🌐 catalog"]:::folder
    datacube_id["🧊 datacube_id"]:::folder
    datacube["📂 datacube"]:::folder
    UI["🖥️ UI"]:::folder
    query_object["📂 query object"]:::folder
    target["🎯 target"]:::folder

    catalog --> catalog_browse
    catalog_browse --> UI

    catalog --> catalog_get
    catalog_get --> UI

    catalog_list_catalogs --> UI

    catalog --> catalog_list
    catalog_list --> UI

    catalog --> catalog_query
    catalog_query --> query_object

    query_object --> catalog_query_read
    catalog_query_read --> datacube_id

    datacube_id --> datacube_crop
    target --> datacube_crop
    datacube_crop --> datacube

    datacube_id --> datacube_get
    datacube_get --> UI

    datacube_id --> datacube_ingest
    datacube_ingest --> datacube

    datacube_id --> datacube_list
    datacube_list --> UI

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

--table--

---

📜 [metadata](./metadata.yaml)

🎁 [wish list and bugs](https://github.com/kamangir/blue-geo/issues/8)

--signature--