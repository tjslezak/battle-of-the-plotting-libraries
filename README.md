# Battle of the Data Visualization (Plotting) Libraries


### 1 - Plot a Time Series

```python
import pandas as pd
import numpy as np

from bokeh.sampledata import stocks

index = pd.DatetimeIndex(stocks.AAPL['date'])
df1 = pd.DataFrame({'IBM': stocks.IBM['close'], 'AAPL': stocks.AAPL['close']}, index=index)
df1.head()
```

### 2 - Plot Categorical
#### Data Retrieval

```python
%%time
url = 'https://www.phoenixopendata.com/dataset/cc08aace-9ca9-467f-b6c1-f0879ab1a358/resource/0ce3411a-2fc6-4302-a33f-167f68608a20/download/crime-data_crime-data_crimestat.csv'

dtypes = {"INC NUMBER": object, "UCR CRIME CATEGORY": object,
          "100 BLOCK ADDR": object, "ZIP": float, "PREMISE TYPE": object} 

phx_crimes = pd.read_csv(url, parse_dates=['OCCURRED ON', 'OCCURRED TO'], dtype=dtypes)
```
#### Data Wrangling

```python
phx_crimes.columns = ['inc_no', 'dt_start', 'dt_end', 'crime_type', 'hundred_block', 'zip', 'premise']
phx_crimes.dropna(subset=['dt_start'], inplace=True)
crimes = ['ARSON', 'MOTOR VEHICLE THEFT', 'DRUG OFFENSE']
crimes_df = phx_crimes[phx_crimes.crime_type.isin(crimes)].reset_index(drop=True).copy()
crimes_df['dow'] = crimes_df['dt_start'].apply(lambda x: x.weekday())
crimes_df['hour'] = crimes_df['dt_start'].apply(lambda x: x.hour)

arson = crimes_df[crimes_df.crime_type == 'ARSON'].groupby(['dow', 'hour']).size()
gta = crimes_df[crimes_df.crime_type == 'MOTOR VEHICLE THEFT'].groupby(['dow', 'hour']).size()
drug = crimes_df[crimes_df.crime_type == 'DRUG OFFENSE'].groupby(['dow', 'hour']).size()
df2 = pd.concat((arson, gta, drug), axis=1, keys=['ARSON', 'MOTOR_VEHICLE_THEFT', 'DRUG_OFFENSE'])
df2.head()
```

### 3 - Plot Multi-categorical
#### Task: Plot frequency of different accident calls each day by day of the week.

```python
%%time
from toolkit import get_mesa_cfs

data3 = get_mesa_cfs()

df3 = data3[data3['Event Type Description'].str.contains('ACCIDENT')].reset_index()
df3 = df3.groupby(['Event Type Description', pd.DatetimeIndex(df3.call_dt).day_name()]).size().reset_index(name='counts')

dows = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 0}

df3['call_dt'] = df3['call_dt'].astype('category').apply(lambda x: dows.get(x))

df3.head(15)
```

### 4 - Geographical Data
#### Task: Plot Unemployment Rate in AZ by County

```python
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.unemployment import data as unemployment

azcounties = [dict(county, Unemployment=unemployment[cid])
            for cid, county in counties.items()
            if county["state"] == "az"]

df4 = pd.DataFrame(azcounties)
df4.head()
```

### 5 - Plot Multivariate
#### Task - compare relationships among multiple variates

```python
from bokeh.sampledata.iris import flowers
df5 = pd.DataFrame(flowers)
df5.head()
```


### 6 - Multiple Distributions
#### Task: Plot Phoenix maximum daily temperatures by month over the past century

```python
df6 = pd.read_csv('data/phoenix_maximum_daily_temps.csv').set_index('Year')
df6.replace(to_replace='M', value=np.nan, inplace=True)
df6 = df6.astype(np.float)
df6.columns = [month for month in range(1, 13)]
df6.head()
```


### 7 - Gridded Data
#### Task: Display an image

```python
url = 'https://desertpy.com/images/new-desertpy-logo/Logo_DesertPy_ico.png'
data7 = plt.imread(url, format='png')
data7.shape
```


### 8 - Ridge Plot
#### Show how the marriage rate varies over the year throughout the state.

```python
df8 = pd.read_excel("https://pub.azdhs.gov/health-stats/mu/mars/mars2019.xlsx", header=1).iloc[:-3, :-1]
df8 = df8.set_index('County').replace('*', np.nan)
df8.head()
```

### 9 - Show off a few notable features of your library 
