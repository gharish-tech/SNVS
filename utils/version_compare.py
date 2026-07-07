def version_to_tuple(version):
    """
    Convert version string to tuple.
    Example:
    '2.4.49' -> (2,4,49)
    """

    try:
        return tuple(map(int, version.split(".")))
    except:
        return (0,)


def compare_versions(v1, operator, v2):

    v1 = version_to_tuple(v1)
    v2 = version_to_tuple(v2)

    if operator == ">":
        return v1 > v2

    elif operator == ">=":
        return v1 >= v2

    elif operator == "<":
        return v1 < v2

    elif operator == "<=":
        return v1 <= v2

    elif operator == "==":
        return v1 == v2

    return False


def is_version_vulnerable(current_version, version_start, version_end):
    """
    Returns True if:
    version_start <= current_version <= version_end
    """

    if not current_version:
        return False

    # No limits -> assume vulnerable
    if version_start == "" and version_end == "":
        return True

    if version_start:
        if compare_versions(current_version, "<", version_start):
            return False

    if version_end:
        if version_end == "*":
            return True

        if compare_versions(current_version, ">", version_end):
            return False

    return True

