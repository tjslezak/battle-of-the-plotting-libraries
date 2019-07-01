import pandas as pd


def status_cfs(s):
    ti = min(s)
    tf = max(s)
    return 'Collected {} records, from {}/{} up to {}/{}.'.format(len(s), ti.month, ti.year, tf.month, tf.year)


def get_tempe_cfs(dt_id='occ_dt'):
    url = 'http://data-tempegov.opendata.arcgis.com/datasets/ba76da19a5274301bb8a010483aec14a_0.csv'
    df = pd.read_csv(url, parse_dates=[dt_id])
    print(status_cfs(df[dt_id]))
    df.rename(columns={dt_id: 'call_dt'}, inplace=True)
    
    return df


def get_mesa_cfs(dt_id='Creation Datetime'):
    url = 'https://data.mesaaz.gov/api/views/4k95-x7aw/rows.csv'
    df = pd.read_csv(url, parse_dates=[dt_id])
    print(status_cfs(df[dt_id]))
    df.rename(columns={dt_id: 'call_dt'}, inplace=True)
    
    return df

def get_phoenix_cfs(dt_id='CALL_RECEIVED'):
    url = 'https://www.phoenixopendata.com/dataset/64a60154-3b2d-4583-8fb5-6d5e1b469c28/resource/1d536ee6-7ffb-49c3-bffe-5cdd98a3c97e/download/calls-for-service_calls-for-service_callsforservice.csv'
    df = pd.read_csv(url, parse_dates=[dt_id])
    print(status_cfs(df[dt_id]))
    df.rename(columns={dt_id: 'call_dt'}, inplace=True)
    
    return df


def get_scottsdale_cfs(dt_id='Create Date', ext='csv'):
    base_url = 'http://data.scottsdaleaz.gov:8000/spd_PDCallsForServic_'
    i = 1
    for year in range(2017, 2020):
        for month in range(1, 13):
            yearmonth = '{year}_{month}.{ext}'.format(year=year, month=month, ext=ext)
            url = base_url + yearmonth
            if i:
                try:
                    df = pd.read_csv(url, parse_dates=[dt_id])
                    i -= 1
                    month0, year0 = month, year
                except:
                    print(url, 'seems to be invalid.')
            else:
                try:
                    df2 = pd.read_csv(url, parse_dates=[dt_id])
                    df = pd.concat([df, df2])
                except:
                    break
         
    print(status_cfs(df[dt_id]))
    df.rename(columns={dt_id: 'call_dt'}, inplace=True)
    
    return df