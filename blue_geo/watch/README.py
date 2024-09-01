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
        ],
        [
            f"[![bashtest](https://github.com/kamangir/{REPO_NAME}/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/{REPO_NAME}/actions/workflows/bashtest.yml)",
            "[Chilcotin River-Landslide](./targets/chilcotin-river-landslide.md), L1C and L2A mixed, `2024-07-30/2024-08-09`, ([dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-199-11f9b5497ef0)).",
        ],
    )
] + [
    " ".join(
        [
            f"![image]({url_prefix}/{object_name}/{object_name}-2X.gif?raw=true&random={string.random_()})",
            f"{description} [`{object_name}`]({url_prefix}/{object_name}.tar.gz) [🔗]({url_prefix}/{object_name}/{object_name}.gif)",
        ]
    )
    for object_name, description in zip(
        [
            "geo-watch-2024-09-01-chilcotin-a",
        ],
        [
            "[Chilcotin River-Landslide](./targets/chilcotin-river-landslide.md), ([dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-201-d64e9bb3716b)).",
        ],
    )
]
