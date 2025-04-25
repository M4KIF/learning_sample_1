
import adapters
import falcon

class Weather:

    # The Weather can potentially provide support for two types of apis
    # one technical and synced rest, so returns the response only after finishing the job.
    # second one async and bidirectional utilizing grpc intended for webapp usage
    def __init__(self, app: falcon.App):
        app.add_route("/analyze_weather", adapters.AnalyzeWeather())
