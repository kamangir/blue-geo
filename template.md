# 🌐 Blue-GEO (`@geo`)

🌐 AI for a Blue Planet.

```bash
pip install blue-geo
```

```mermaid
graph LR
    catalog_browse["@catalog browse <catalog-name> <resource>"]
    catalog_get["@catalog get <thing> --catalog <catalog>"]

    catalog["🌐 catalog"]:::folder
    datacube_id["🧊 datacube"]:::folder
    UI["🖥️ UI"]:::folder

    catalog --> catalog_browse
    catalog_browse --> UI

    catalog --> catalog_get
    catalog_get --> UI

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

--table--

---

📜 [metadata](./metadata.yaml)

🎁 [wish list and bugs](https://github.com/kamangir/blue-geo/issues/8)

--signature--