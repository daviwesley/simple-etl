from simple_etl import transform_data


def test_with_simple_data():
    data = {"foo": {"bar": ["one", "two"]}}

    parser = [{"from": "foo.bar", "to": "baz"}]

    result = transform_data(data, parser)
    excpected = {"baz": ["one", "two"]}

    assert result == excpected
