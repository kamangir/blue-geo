import os

if not QGIS_is_live:
    from .logger import Q_log
    from .layer import Q_layer
    from .path import Q_open_path
    from .project import Q_project
    from .seed import Q_seed

    ABCLI_OBJECT_ROOT = ""


def Q_get_thing_name_or_path(thing, property: str) -> str:
    assert property in ["name", "path"], f"invalid property: {property}"

    return_project: bool = True
    if thing in ["project", "qgz", Q_project, "object", object]:
        pass
    elif thing in ["layer", Q_layer]:
        return_project = False
    elif isinstance(thing, str) and thing:
        return thing

    if return_project:
        return Q_project.name if property == "name" else Q_project.path

    return Q_layer.object_name if property == "name" else Q_layer.path


def Q_get_thing_name(thing) -> str:
    return Q_get_thing_name_or_path(
        thing,
        property="name",
    )


def Q_get_thing_path(thing) -> str:
    return Q_get_thing_name_or_path(
        thing,
        property="path",
    )


def Q_object_path(
    object_name: str,
    create: bool = True,
) -> str:
    output = os.path.join(ABCLI_OBJECT_ROOT, object_name)

    if create:
        os.makedirs(output, exist_ok=True)

    return output


def Q_file_path_in_object(
    filename,
    object_name="",
    create: bool = True,
) -> str:
    return os.path.join(
        Q_object_path(
            object_name=object_name,
            create=create,
        ),
        filename,
    )


def Q_open(
    thing="object",
    dryrun: bool = False,
):
    Q_open_path(
        Q_get_thing_path(thing=thing),
        dryrun=dryrun,
    )


def Q_upload(
    thing="object",
    dryrun: bool = False,
):
    Q_seed(
        command=[
            "abcli_upload",
            f"filename={Q_project.name}.qgz" if thing == "qgz" else "-",
            Q_get_thing_name(thing),
        ],
        dryrun=dryrun,
    )
