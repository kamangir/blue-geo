from . import NAME


class GenericDatacube:
    def __init__(self):
        self.type = "generic"

    @property
    def datacube_id(self) -> str:
        return "blue-geo"

    @property
    def description(self) -> str:
        return "{}.{}".format(
            NAME,
            self.__class__.__name__,
        )
