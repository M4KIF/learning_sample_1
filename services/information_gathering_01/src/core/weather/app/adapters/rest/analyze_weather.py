from core.weather.use_cases.analyze_weather.domain import Weather
from core.weather.use_cases.analyze_weather.adapters import WeatherApi

import falcon

class AnalyzeWeatherRest:

    def __init__(self):
        self.weather = Weather()

    def on_get(self, req: falcon.Request, resp: falcon.Response):
        resp.media({"value":"eulav"})