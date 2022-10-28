import functools


def rgetattr(obj, attr, *args):
    """Use getattr on nested attributes like example below
    obj.davi.age
    getattr(obj, 'davi')
    getattr(davi, 'age')"""

    def _getattr(obj, attr):
        if isinstance(obj, dict):
            return obj.get(attr, *args)

        return getattr(obj, attr, *args)

    return functools.reduce(_getattr, [obj] + attr.split("."))
