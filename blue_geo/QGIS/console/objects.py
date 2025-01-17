import os

if not QGIS_is_live:
    from .layer import layer
    from .path import Q_open_path
    from .project import project
    from .seed import Q_seed

    ABCLI_OBJECT_ROOT = ""


def Q_get_thing_name_or_path(thing, property: str) -> str:
    assert property in ["name", "path"]

    return_project: bool = True
    if thing in ["project", "qgz", project, "object", object]:
        pass
    elif thing in ["layer", layer]:
        return_project = False
    elif isinstance(thing, str) and thing:
        return thing

    if return_project:
        return project.name if property == "name" else project.path

    return layer.object_name if property == "name" else layer.path


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


def Q_open(thing="object"):
    Q_open_path(Q_get_thing_path(thing))


def Q_upload(
    thing="object",
    dryrun: bool = False,
):
    Q_seed(
        command=[
            "abcli_upload",
            f"filename={project.name}.qgz" if thing == "qgz" else "-",
            Q_get_thing_name(thing),
        ],
        dryrun=dryrun,
    )
