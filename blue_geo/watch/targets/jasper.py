from functools import reduce
from typing import List
from blue_objects.env import ABCLI_PUBLIC_PREFIX

list_of_dates: List[str] = [
    "2024_7_20",
    "2024_7_22",
    "2024_7_27",
]

items = reduce(
    lambda x, y: x + y,
    [
        [
            "`{}`".format(date.replace("_", "-")),
            f"![image]({ABCLI_PUBLIC_PREFIX}/geo-watch-2024-09-06-Jasper-a/11_U_MU_{date}_0_TCI.png)",
        ]
        for date in list_of_dates
    ],
    [],
)
