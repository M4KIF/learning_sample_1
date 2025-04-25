import pytest
import falcon

from . import AnalyzeWeather

def test_instantiate_controller_class():
    controller = AnalyzeWeather()

    mock_req = falcon.Request(
        method="GET",
        uri="/analyze_weather",
        params={}
    )

    mock_resp = falcon.Response()
    controller.on_get(mock_req, mock_resp)
    assert mock_resp.media == '{"value":"eulav"}'
