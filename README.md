<div align="center">
    <h1>Simple ETL</h1>
</div>

#### Instalation

- `pip install simple-etl`

#### Using poetry

    poetry add simple-etl

#### Description

- Simple ETL is a transformation tool to convert data with a friendly configuration into a specific data structure usually a simple dictionary .

#### Usage

Imagine you have a dictionary containing your data like this:

```
{
    "iels": "Guido",
    "reliz": "python",
    "coie": "Netherlands"
}
```

As you can see this data has weird column names and we'd like to rename this columns properly.

```python
from simple_etl import transform_data

original_data = {
    "iels": "guido",
    "reliz": "python",
    "coie": "Netherlands"
}
etl_config = [
    {"from": "iels", "to": "name", "transform": lambda x: x.upper()},
    {"from": "reliz", "to": "language"},
    {"from": "coie", "to": "country"},
]

output = transform_data(original_data, etl_config)
print(output)
# {'name': 'Guido', 'language': 'python', 'country': 'Netherlands'}
```

#### Usage with custom functions

You can use a custom function to transform the given data using the "transform" key. this is the function signature that you must follow

```python
def transform_function(value: Any, data: Optional[dict] = OriginalData):
    # do your logic here with the value or the entire data
    pass
```

```python
from simple_etl import transform_data

original_data = {
    "iels": "guido",
    "kbug": "rossum",
    "reliz": "python",
    "coie": "Netherlands"
}
etl_config = [
    {"from": "iels", "to": "name", "transform": lambda x: x.upper()},
    {"from": "reliz", "to": "language"},
    {"from": "coie", "to": "country"},
    {"from": "kbug", "to": "full_name", "transform": lambda value, data: f"{data['iels']} {value}"}
]

output = transform_data(original_data, etl_config)
print(output)
# {'name': 'GUIDO', 'language': 'python', 'country': 'Netherlands'}
```

As the example above the variable `etl_config` receive a lambda function that capture the value and use the built-in upper function to transform the output
