
from wsgiref.simple_server import make_server

import falcon

import domains.weather.app

class What:
    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        resp.media = {
            "rand": "1"
        }

def main():
    app = falcon.App()
    app.add_route("/test", What())
    with make_server('', 61111, app) as httpd:
        print("Serving 8081")
        httpd.serve_forever()

main()
