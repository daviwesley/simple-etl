from typing import List

from .object import rgetattr


def set_dot_notation(obj: dict, key: str, value: str) -> dict:
    """Set a value in a dictionary given a dot notation key."""
    keys = key.split(".")
    for key in keys[:-1]:
        obj = obj.setdefault(key, {})
    obj[keys[-1]] = value
    return obj


def remove_none(input: dict) -> dict:
    """Remove None values from a dictionary."""
    try:
        for k, v in input.items():
            if isinstance(v, dict):
                remove_none(v)
            elif v is None:
                del input[k]
    except RuntimeError:
        remove_none(input)
    return input


def rename_keys(input: dict, mapping: dict, exclude_none=False) -> dict:
    """Rename keys in a dictionary given a mapping structure."""
    output = {}
    for key, value in input.items():
        if isinstance(value, dict):
            value = rename_keys(value, mapping, exclude_none)
        output[mapping.get(key, key)] = value
    if exclude_none:
        output = remove_none(output)
    return output


def transform_data(input: dict, mapping: List[dict], exclude_none=False) -> dict:
    """Transform data given a mapping structure."""
    output = {}

    for item in mapping:
        if item.get("transform"):
            value = rgetattr(input, item["from"])
            value = (
                item["transform"](value)
                if item["transform"].__code__.co_argcount == 1
                else item["transform"](value, input)
            )
        else:
            value = rgetattr(input, item["from"])
        set_dot_notation(output, item["to"], value)
    if exclude_none:
        output = remove_none(output)
    return output
