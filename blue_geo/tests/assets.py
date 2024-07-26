# last datacube-id must be valid.

datacube_generic_parse_datacube_id = [
    ["void", False],
    ["void-void-void-void-void-void-void-void", False],
    ["datacube-void-void-void", False],
    ["datacube-generic", True],
]

datacube_firms_area_parse_datacube_id = [
    ["datacube-firms_void-void-void-void-void", False],
    ["datacube-firms_area-void-void-void-void", False],
    ["datacube-firms-area-void-void-void-void", False],
    ["datacube-firms-area-world-void-2024-07-20-1", False],
    ["datacube-firms-area-void-MODIS_NRT-2024-07-20-1", False],
    ["datacube-firms-area-world-MODIS_NRT-2024-07-20-1", True],
]
