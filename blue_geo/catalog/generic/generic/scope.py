class DatacubeScope:
    def __init__(self, what: str):
        self.all = what == "all"

        self.quick = what == "quick"

        self.metadata = what == "metadata"

        self.suffix = (
            []
            if self.all or self.quick or self.metadata
            else [suffix for suffix in what.split("+") if suffix]
        )
