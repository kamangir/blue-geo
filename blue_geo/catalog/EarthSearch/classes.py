from blue_geo.catalog.generic.stac.classes import STACCatalog


class EarthSearchCatalog(STACCatalog):
    name = "EarthSearch"

    url = {
        "api": "https://earth-search.aws.element84.com/v1/",
        "aws_open_data": "https://registry.opendata.aws/sentinel-2/",
        "stac_api": "https://stacindex.org/catalogs/earth-search#/",
        "ui": "https://viewer.aws.element84.com/",
    }