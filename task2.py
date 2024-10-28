import datetime

from src.apis import call_FND_json


def extract_humidity_on_the_day_after_tomorrow():
    the_day_after_tomorrow=(datetime.datetime.now()+datetime.timedelta(days=2)).strftime('%Y%m%d')
    daily_forecast=call_FND_json()['DYN_DAT_MINDS_FND']
    for k,v in list(daily_forecast.items()):
        if the_day_after_tomorrow in v.values():
            key=k[:4]
            max_humidity_key=f'{key}MaxRH'
            min_humidity_key=f'{key}MinRH'
            return f'{daily_forecast[min_humidity_key]['Val_Eng']} - {daily_forecast[max_humidity_key]['Val_Eng']}%'
if __name__=='__main__':
    print(extract_humidity_on_the_day_after_tomorrow())
