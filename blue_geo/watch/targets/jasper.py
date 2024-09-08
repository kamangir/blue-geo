from typing import List, Dict
from blue_objects.env import ABCLI_PUBLIC_PREFIX

list_of_dates: List[str] = [
    "2024_7_20",
    "2024_7_22",
    "2024_7_27",
]

date_items: Dict[str, List[str]] = {
    date: [
        "`{}`".format(date.replace("_", "-")),
        f"![image]({ABCLI_PUBLIC_PREFIX}/geo-watch-2024-09-06-Jasper-a/11_U_MU_{date}_0_TCI.png)",
    ]
    for date in list_of_dates
}

items: List[str] = [
    date_items[date][index]
    for index in range(len(date_items[list_of_dates[0]]))
    for date in list_of_dates
]
