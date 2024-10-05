# 🌐 adding catalogs and datacubes

to add a new [catalog](../catalog/) or [datacube](../datacube/) follow these steps,

0️⃣ copy and refactor [`notebooks/EarthSearch.ipynb`](../../notebooks/EarthSearch.ipynb).

1️⃣ clone [`catalog/EarthSearch`](../catalog/EarthSearch/) and define `NovelCatalog`.

2️⃣ clone [`catalog/EarthSearch/sentinel_2_l1c`](../catalog/EarthSearch/sentinel_2_l1c/) and define `NovelDatacube`.

3️⃣ add `NovelCatalog` and `NovelDatacube` to [`catalog/classes.py`](../catalog/classes.py).

4️⃣ add the package extensions to [`setup.py`](../../setup.py).

5️⃣ add the relevant secrets to,
- [`workflows/pytest.yml`](../../.github/workflows/pytest.yml)
- [`env.py`](../../blue_geo/env.py)
- [`sample.env`](../../blue_geo/sample.env)
- [`tests/test_env.py`](../../blue_geo/tests/test_env.py)

6️⃣ add the relevant config variables to,
- [`config.env`](../../blue_geo/config.env)
- [`env.py`](../../blue_geo/env.py)
- [`tests/test_env.py`](../../blue_geo/tests/test_env.py)

7️⃣ add the relevant test cases to,
- [`tests/datacube_get.sh`](../../blue_geo/.abcli/tests/datacube_get.sh)
- [`tests/datacube_list.sh`](../../blue_geo/.abcli/tests/datacube_list.sh)
- [`tests/help.sh`](../../blue_geo/.abcli/tests/help.sh)
- [`tests/assets.py`](../../blue_geo/tests/assets.py)

8️⃣ copy and refactor [`tests/test_catalog_EarthSearch_sentinel_1_l1C.py`](../../blue_geo/tests/test_catalog_EarthSearch_sentinel_1_l1C.py).

9️⃣ add a relevant target,
```bash
@targets edit
```

🔟 copy and refactor [`targets/Jasper-template.md`](../../blue_geo/watch/targets/Jasper-template.md).

1️⃣ 1️⃣ add references to,
- [`README.py`](../../blue_geo/README.py).
- [`catalog/README.md`](../../blue_geo/catalog/README.md).
- [`catalog/README.py`](../../blue_geo/catalog/README.py).
- [`targets/README.py`](../../blue_geo/watch/targets/README.py)