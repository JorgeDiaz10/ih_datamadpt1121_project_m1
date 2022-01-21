<p align="centre"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

# __ih_datamadpt1121_project_m1__

Ironhack Madrid - Data Analytics Part Time - Janaury 2022 - Project Module 1

---

# BiciMad Stations distance to catholic temples or non catholic temples


Proeyect 1 is a Python App for checking the distance between the catholic temples or non catholic temples to the closer BiciMAD Station. The final output is an email with a csv file with the information above.

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
import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
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
    1. Activate the appropiate environment. In our case, conda activate proyecto1
    2. Go to the project folder
    3. Type python main.py --type / -t CloserStation or AllStations 
    4. Write your email credentials
    5. You will get a csv file send by gmail
```

Here is an example of what you would get in the csv file:

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
[Gmail] (https://mail.google.com/mail/u/0/#inbox)

---

## **Project Main Stack**

- [Azure SQL Database](https://portal.azure.com/)

- [Azure Data Studio](https://docs.microsoft.com/es-es/sql/azure-data-studio/download-azure-data-studio?view=sql-server-ver15) 

- [Requests](https://requests.readthedocs.io/)

- [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)

-  Module `geo_calculations.py`

- [Argparse](https://docs.python.org/3.7/library/argparse.html)

- [smtplib](https://docs.python.org/3/library/smtplib.html)












 


 

