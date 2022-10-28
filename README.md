# Simple ETL

#### Instalation

- `pip install simple-etl`

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
    "iels": "Guido",
    "reliz": "python",
    "coie": "Netherlands"
}
etl_config = [
    {"from": "iels", "to": "name"},
    {"from": "reliz", "to": "language"},
    {"from": "coie", "to": "country"},
]

output = transform_data(original_data, etl_config)
print(output)
# {'name': 'Guido', 'language': 'python', 'country': 'Netherlands'}
```
