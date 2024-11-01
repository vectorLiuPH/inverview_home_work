import requests

from src.tools import api_exception_handler


@api_exception_handler
def call_wxinfo_json_api():
    url = 'https://www.hko.gov.hk/wxinfo/json/one_json.xml'
    resp = requests.get(url)
    return resp.json()

@api_exception_handler
def call_wxinfo_json_uc_api():
    url = 'https://www.hko.gov.hk/wxinfo/json/one_json_uc.xml'
    resp = requests.get(url)
    return resp.json()

@api_exception_handler
def call_FND_json():
    url = 'https://www.hko.gov.hk/json/DYN_DAT_MINDS_FND.json'
    resp = requests.get(url)
    return resp.json()

@api_exception_handler
def call_ocf_data_hko_v2():
    url='https://pda.weather.gov.hk/locspc/data/ocf_data/HKO.v2.xml'
    resp=requests.get(url)
    return resp

if __name__ == '__main__':
    call_FND_json()
