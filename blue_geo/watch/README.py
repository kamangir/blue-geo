from abcli import string
from blue_geo import REPO_NAME

url_prefix = "https://kamangir-public.s3.ca-central-1.amazonaws.com"


items = [
    " ".join(
        [
            f"![image]({url_prefix}/{object_name}/{object_name}.gif?raw=true&random={string.random_()})",
            f"{description} [`{object_name}`]({url_prefix}/{object_name}.tar.gz) [🔗]({url_prefix}/{object_name}/{object_name}.gif)",
        ]
    )
    for object_name, description in zip(
        [
            "test_blue_geo_watch",
            "geo-watch-2024-08-31-chilcotin-c",
            "geo-watch-2024-09-01-chilcotin-a",
        ],
        [
            f"[![bashtest](https://github.com/kamangir/{REPO_NAME}/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/{REPO_NAME}/actions/workflows/bashtest.yml)",
            "[Chilcotin River-Landslide](./targets/chilcotin-river-landslide.md), 🛰️ Sentinel-2, ([details](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-199-11f9b5497ef0)).",
            "L1C, `2024-07-15/2024-08-24`.",
        ],
    )
]
