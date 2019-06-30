import pandas as pd

def get_phoenix_cfs(dt_id='CALL_RECEIVED'):
    url = 'https://www.phoenixopendata.com/dataset/64a60154-3b2d-4583-8fb5-6d5e1b469c28/resource/1d536ee6-7ffb-49c3-bffe-5cdd98a3c97e/download/calls-for-service_calls-for-service_callsforservice.csv'
    df = pd.read_csv(url, parse_dates=[dt_id])
    print(status_cfs(df[dt_id]))
    df.rename(columns={dt_id: 'call_dt'}, inplace=True)
    
    return df