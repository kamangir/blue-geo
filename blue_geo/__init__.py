# to avoid import complications.
# from blue_objects.env import ABCLI_PUBLIC_PREFIX
ABCLI_PUBLIC_PREFIX = "https://kamangir-public.s3.ca-central-1.amazonaws.com"


NAME = "blue_geo"

ICON = "🌐"

DESCRIPTION = f"{ICON} AI for a Blue Planet."

VERSION = "4.777.1"

REPO_NAME = "blue-geo"

MARQUEE = f"{ABCLI_PUBLIC_PREFIX}/2024-01-06-20-39-46-73614/2024-01-06-20-39-46-73614-2X.gif?raw=true"

ALIAS = "@geo"


def fullname() -> str:
    return f"{NAME}-{VERSION}"
