from src.apis import call_ocf_data_hko_v2


def test_whether_forecast_api_call_successful():
    resp=call_ocf_data_hko_v2()
    assert resp.status_code==200