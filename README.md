# battle-of-the-plotting-libraries


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
<style>div.hololayout {
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

div.bk-hbox {
    display: flex;
    justify-content: center;
}

div.bk-hbox div.bk-plot {
    padding: 8px;
}

div.bk-hbox div.bk-data-table {
    padding: 20px;
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
    CPU times: user 48.1 s, sys: 654 ms, total: 48.8 s
    Wall time: 1min 4s



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

### Plot Multivariate


```python
from bokeh.sampledata.iris import flowers
iris_df = pd.DataFrame(flowers)
iris_df.head()
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

### Phoenix maximum daily temperatures by month over the past century


```python
phx_df = pd.read_csv('data/phoenix_maximum_daily_temps.csv')
phx_df.head()
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
      <th>Year</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
      <th>Apr</th>
      <th>May</th>
      <th>Jun</th>
      <th>Jul</th>
      <th>Aug</th>
      <th>Sep</th>
      <th>Oct</th>
      <th>Nov</th>
      <th>Dec</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1919</td>
      <td>74</td>
      <td>74</td>
      <td>86</td>
      <td>97</td>
      <td>101</td>
      <td>113</td>
      <td>110</td>
      <td>110</td>
      <td>106</td>
      <td>90</td>
      <td>84</td>
      <td>76</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1920</td>
      <td>79</td>
      <td>76</td>
      <td>83</td>
      <td>94</td>
      <td>105</td>
      <td>110</td>
      <td>114</td>
      <td>108</td>
      <td>105</td>
      <td>98</td>
      <td>79</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1921</td>
      <td>77</td>
      <td>92</td>
      <td>95</td>
      <td>96</td>
      <td>101</td>
      <td>110</td>
      <td>110</td>
      <td>107</td>
      <td>105</td>
      <td>100</td>
      <td>89</td>
      <td>76</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1922</td>
      <td>69</td>
      <td>80</td>
      <td>83</td>
      <td>92</td>
      <td>105</td>
      <td>114</td>
      <td>112</td>
      <td>110</td>
      <td>107</td>
      <td>100</td>
      <td>80</td>
      <td>74</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1923</td>
      <td>84</td>
      <td>82</td>
      <td>84</td>
      <td>92</td>
      <td>104</td>
      <td>112</td>
      <td>111</td>
      <td>105</td>
      <td>105</td>
      <td>92</td>
      <td>80</td>
      <td>71</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

### Gridded Data


```python
x, y = np.meshgrid(range(-5, 5), range(-5, 5))
z = x ** 2 + y ** 2
src = np.stack((x, y, z))
src
```




    array([[[-5, -4, -3, -2, -1,  0,  1,  2,  3,  4],
            [-5, -4, -3, -2, -1,  0,  1,  2,  3,  4],
            [-5, -4, -3, -2, -1,  0,  1,  2,  3,  4],
            [-5, -4, -3, -2, -1,  0,  1,  2,  3,  4],
            [-5, -4, -3, -2, -1,  0,  1,  2,  3,  4],
            [-5, -4, -3, -2, -1,  0,  1,  2,  3,  4],
            [-5, -4, -3, -2, -1,  0,  1,  2,  3,  4],
            [-5, -4, -3, -2, -1,  0,  1,  2,  3,  4],
            [-5, -4, -3, -2, -1,  0,  1,  2,  3,  4],
            [-5, -4, -3, -2, -1,  0,  1,  2,  3,  4]],
    
           [[-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],
            [-4, -4, -4, -4, -4, -4, -4, -4, -4, -4],
            [-3, -3, -3, -3, -3, -3, -3, -3, -3, -3],
            [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
            [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
            [ 2,  2,  2,  2,  2,  2,  2,  2,  2,  2],
            [ 3,  3,  3,  3,  3,  3,  3,  3,  3,  3],
            [ 4,  4,  4,  4,  4,  4,  4,  4,  4,  4]],
    
           [[50, 41, 34, 29, 26, 25, 26, 29, 34, 41],
            [41, 32, 25, 20, 17, 16, 17, 20, 25, 32],
            [34, 25, 18, 13, 10,  9, 10, 13, 18, 25],
            [29, 20, 13,  8,  5,  4,  5,  8, 13, 20],
            [26, 17, 10,  5,  2,  1,  2,  5, 10, 17],
            [25, 16,  9,  4,  1,  0,  1,  4,  9, 16],
            [26, 17, 10,  5,  2,  1,  2,  5, 10, 17],
            [29, 20, 13,  8,  5,  4,  5,  8, 13, 20],
            [34, 25, 18, 13, 10,  9, 10, 13, 18, 25],
            [41, 32, 25, 20, 17, 16, 17, 20, 25, 32]]])




```python

```
