<p align="centre"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

# __ih_datamadpt1121_project_m1__

Ironhack Madrid - Data Analytics Part Time - Janaury 2022 - Project Module 1

---

# BiciMad Stations distance to catholic temples or non catholic temples


Proeyect 1 is a Python App for checking the distance between the catholic temples or non catholic temples to the closer BiciMAD Station.

---

## Installation


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the libraries.

```bash
import pandas as pd
import requests
import numpy as np
import os
from shapely.geometry import Point
import geopandas as gpd
```

---

## Usage

```python
def min_distance():
    x = str(input('Enter the Place of Interest: '))
    y = merge()[merge()['Place of interest']== x]
    return y.sort_values(by='Distance', ascending=True).head(1).drop(['City', 'lat_start', 'long_start', 'start', 'geometry_coordinates', 'long_finish', 'lat_finish', 'final'], axis = 1)


def all_min_stations():
    return merge().sort_values(by = "Distance", ascending = True).groupby('Place of interest')['Type of place','Place address','BiciMAD station', 'Station location','Distance'].nth(0).drop(["Distance"], axis = "columns")
```

## Use in Terminal

```python
Once you open the terminal:
    1. Activate the appropiate environment. In our case, **conda activate proyecto1**
    2. Go to the project folder
    3. Type **python main.py** --tipo CloserStation or AllStations to get a csv file
```

|  Place of interest      |  Place address | Type of place | BiciMAD Station |  Station location  |  Distance  |
| ----------------------- |:--------------:|:-------------:|:---------------:|:------------------:|-----------:|
|  Comunidad Cristi...    | CALLE ...      | no_catolicas  | Gutierre de C...| Calle Gutierr...   | 4436.41386 |

---

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.   

---

## License
[BICIMAD] (https://www.bicimad.com/)
[Datasets] (https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json#/)

---

## **Project Main Stack**

- [Azure SQL Database](https://portal.azure.com/)

- [SQL Alchemy](https://docs.sqlalchemy.org/en/13/intro.html) (alternatively you can use _Azure Data Studio_)

- [Requests](https://requests.readthedocs.io/)

- [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)

- Module `geo_calculations.py`

- [Argparse](https://docs.python.org/3.7/library/argparse.html)












 


 

