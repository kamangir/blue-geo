from typing import Dict
from types import ModuleType


from blue_geo.objects import global_power_plant_database

special_objects: Dict[str, ModuleType] = {
    "global-power-plant-database": global_power_plant_database,
}
