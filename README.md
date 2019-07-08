# battle-of-the-plotting-libraries


### Plot a Time Series

```python
import pandas as pd
import numpy as np

from bokeh.sampledata import stocks 

index = pd.DatetimeIndex(stocks.AAPL['date'])
stock_df = pd.DataFrame({'IBM': stocks.IBM['close'], 'AAPL': stocks.AAPL['close']}, index=index)
stock_df.head()
```

Plot 1. Compare the time series

### Plot Categorical Data

```python
from toolkit import get_mesa_cfs

df = get_mesa_cfs()

accidents = df[df['Event Type Description'].str.contains('ACCIDENT')].reset_index()
accidents = accidents.groupby(['Event Type Description', pd.DatetimeIndex(accidents.call_dt).day_name()]).size().reset_index(name='counts')
accidents.head(15)
```

Plot 2. Compare frequency of different accident calls by day of the week


### Geographical Data

```python
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.unemployment import data as unemployment

counties = [dict(county, Unemployment=unemployment[cid])
            for cid, county in counties.items()
            if county["state"] == "az"]

df = pd.DataFrame(counties)
df.head()
```

Plot 3. Compare Arizona Unemployment by County using geographic coordinates.


### Plot Multivariate

```python
from bokeh.sampledata.iris import flowers

iris_df = pd.DataFrame(flowers)
iris_df.head()
```

Plot 4. Compare everything (Scatter Matrix)


### Phoenix maximum daily temperatures by month over the past century

```python
phx_df = pd.read_csv('data/phoenix_maximum_daily_temps.csv')
phx_df.head()
```

Plot 5. Make a Ridgeline plot or something comparable.

### Gridded Data

```python

x, y = np.meshgrid(range(-5, 5), range(-5, 5))
z = x ** 2 + y ** 2
src = np.stack((x, y, z))
src
```

Plot 6. Plot the image (n-d array).
