from abc import abstractmethod

class WeatherApi:

    def __init__(self):
        pass

    @abstractmethod
    def take_forecast_for(self, name : str) -> []:
        pass