import falcon

class AnalyzeWeather:

    def __init__(self):
        pass

    def on_get(self, req: falcon.Request, resp: falcon.Response):
        resp.media({"value":"eulav"})