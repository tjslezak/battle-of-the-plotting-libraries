

```python
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import bokeh

import altair
import seaborn
import plotly
import holoviews as hv
import hvplot.pandas
```





<link rel="stylesheet" href="https://code.jquery.com/ui/1.10.4/themes/smoothness/jquery-ui.css">
<style>div.bk-hbox {
    display: flex;
    justify-content: center;
}

div.bk-hbox div.bk-plot {
    padding: 8px;
}

div.bk-hbox div.bk-data-table {
    padding: 20px;
}

div.hololayout {
  display: flex;
  align-items: center;
  margin: 0;
}

div.holoframe {
  width: 75%;
}

div.holowell {
  display: flex;
  align-items: center;
}

form.holoform {
  background-color: #fafafa;
  border-radius: 5px;
  overflow: hidden;
  padding-left: 0.8em;
  padding-right: 0.8em;
  padding-top: 0.4em;
  padding-bottom: 0.4em;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  margin-bottom: 20px;
  border: 1px solid #e3e3e3;
}

div.holowidgets {
  padding-right: 0;
  width: 25%;
}

div.holoslider {
  min-height: 0 !important;
  height: 0.8em;
  width: 100%;
}

div.holoformgroup {
  padding-top: 0.5em;
  margin-bottom: 0.5em;
}

div.hologroup {
  padding-left: 0;
  padding-right: 0.8em;
  width: 100%;
}

.holoselect {
  width: 92%;
  margin-left: 0;
  margin-right: 0;
}

.holotext {
  padding-left:  0.5em;
  padding-right: 0;
  width: 100%;
}

.holowidgets .ui-resizable-se {
  visibility: hidden
}

.holoframe > .ui-resizable-se {
  visibility: hidden
}

.holowidgets .ui-resizable-s {
  visibility: hidden
}


/* CSS rules for noUISlider based slider used by JupyterLab extension  */

.noUi-handle {
  width: 20px !important;
  height: 20px !important;
  left: -5px !important;
  top: -5px !important;
}

.noUi-handle:before, .noUi-handle:after {
  visibility: hidden;
  height: 0px;
}

.noUi-target {
  margin-left: 0.5em;
  margin-right: 0.5em;
}
</style>






### Plot a Time Series


```python
from bokeh.sampledata import stocks 
```


```python
index = pd.DatetimeIndex(stocks.AAPL['date'])
stock_df = pd.DataFrame({'IBM': stocks.IBM['close'], 'AAPL': stocks.AAPL['close']}, index=index)
stock_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>IBM</th>
      <th>AAPL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-03-01</th>
      <td>100.25</td>
      <td>130.31</td>
    </tr>
    <tr>
      <th>2000-03-02</th>
      <td>103.12</td>
      <td>122.00</td>
    </tr>
    <tr>
      <th>2000-03-03</th>
      <td>108.00</td>
      <td>128.00</td>
    </tr>
    <tr>
      <th>2000-03-06</th>
      <td>103.06</td>
      <td>125.69</td>
    </tr>
    <tr>
      <th>2000-03-07</th>
      <td>103.00</td>
      <td>122.87</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

### Plot Categorical Data


```python
from toolkit import get_mesa_cfs
```


```python
%%time
df = get_mesa_cfs()
```

    Collected 356004 records, from 1/2017 up to 7/2019.
    CPU times: user 51.8 s, sys: 645 ms, total: 52.5 s
    Wall time: 1min 7s



```python
accidents = df[df['Event Type Description'].str.contains('ACCIDENT')].reset_index()
accidents = accidents.groupby(['Event Type Description', pd.DatetimeIndex(accidents.call_dt).day_name()]).size().reset_index(name='counts')
accidents.head(15)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Event Type Description</th>
      <th>call_dt</th>
      <th>counts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ACCIDENT</td>
      <td>Friday</td>
      <td>2347</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ACCIDENT</td>
      <td>Monday</td>
      <td>2060</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ACCIDENT</td>
      <td>Saturday</td>
      <td>1617</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ACCIDENT</td>
      <td>Sunday</td>
      <td>980</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ACCIDENT</td>
      <td>Thursday</td>
      <td>2256</td>
    </tr>
    <tr>
      <th>5</th>
      <td>ACCIDENT</td>
      <td>Tuesday</td>
      <td>2286</td>
    </tr>
    <tr>
      <th>6</th>
      <td>ACCIDENT</td>
      <td>Wednesday</td>
      <td>2313</td>
    </tr>
    <tr>
      <th>7</th>
      <td>ACCIDENT W/INJURIES</td>
      <td>Friday</td>
      <td>753</td>
    </tr>
    <tr>
      <th>8</th>
      <td>ACCIDENT W/INJURIES</td>
      <td>Monday</td>
      <td>649</td>
    </tr>
    <tr>
      <th>9</th>
      <td>ACCIDENT W/INJURIES</td>
      <td>Saturday</td>
      <td>634</td>
    </tr>
    <tr>
      <th>10</th>
      <td>ACCIDENT W/INJURIES</td>
      <td>Sunday</td>
      <td>411</td>
    </tr>
    <tr>
      <th>11</th>
      <td>ACCIDENT W/INJURIES</td>
      <td>Thursday</td>
      <td>734</td>
    </tr>
    <tr>
      <th>12</th>
      <td>ACCIDENT W/INJURIES</td>
      <td>Tuesday</td>
      <td>655</td>
    </tr>
    <tr>
      <th>13</th>
      <td>ACCIDENT W/INJURIES</td>
      <td>Wednesday</td>
      <td>719</td>
    </tr>
    <tr>
      <th>14</th>
      <td>HIT and RUN ACCIDENT</td>
      <td>Friday</td>
      <td>894</td>
    </tr>
  </tbody>
</table>
</div>



Task: Plot frequency of different accident calls by day of the week.


```python

```

### Geographical Data


```python
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.unemployment import data as unemployment

counties = [dict(county, Unemployment=unemployment[cid])
            for cid, county in counties.items()
            if county["state"] == "az"]
```


```python
df = pd.DataFrame(counties)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unemployment</th>
      <th>detailed name</th>
      <th>lats</th>
      <th>lons</th>
      <th>name</th>
      <th>state</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>14.8</td>
      <td>Apache County, Arizona</td>
      <td>[36.37512, 36.32282, 36.29451, 36.26437, 36.24...</td>
      <td>[-109.04594, -109.0458, -109.04574, -109.04579...</td>
      <td>Apache</td>
      <td>az</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7.4</td>
      <td>Cochise County, Arizona</td>
      <td>[31.33431, 31.33402, 31.33408, 31.33399, 31.33...</td>
      <td>[-109.56635, -109.56866, -109.62562, -109.6471...</td>
      <td>Cochise</td>
      <td>az</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.7</td>
      <td>Coconino County, Arizona</td>
      <td>[35.52914, 35.52804, 35.52807, 35.88495, 35.97...</td>
      <td>[-113.2791, -113.33416, -113.33416, -113.30946...</td>
      <td>Coconino</td>
      <td>az</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10.9</td>
      <td>Gila County, Arizona</td>
      <td>[33.17492, 33.17482, 33.16345, 33.16311, 33.15...</td>
      <td>[-110.52778, -110.52781, -110.52759, -110.5387...</td>
      <td>Gila</td>
      <td>az</td>
    </tr>
    <tr>
      <th>4</th>
      <td>14.4</td>
      <td>Graham County, Arizona</td>
      <td>[32.48193, 32.4821, 32.48546, 32.48632, 32.491...</td>
      <td>[-110.45155, -110.45155, -110.45156, -110.4515...</td>
      <td>Graham</td>
      <td>az</td>
    </tr>
  </tbody>
</table>
</div>



Task: Plot Arizona Unemployment by County


```python

```


```python

```


```python

```
