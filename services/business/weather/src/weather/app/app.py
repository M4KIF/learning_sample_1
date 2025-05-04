from .adapters.rest import AnalyzeWeatherRest

class WeatherApp:

    def __init__(self):
        self.Rest = AnalyzeWeatherRest()
        print(self.Rest)
