import os
import server
from aiohttp import web

# HOME_APPS
WEBROOT_APPS = os.path.dirname(os.path.realpath(__file__))

@server.PromptServer.instance.routes.get("/")
def apps_entrance(request):
    return web.FileResponse(os.path.join(WEBROOT_APPS, "index.html"))

# Sirve las carpetas estáticas necesarias
server.PromptServer.instance.routes.static("/", path=WEBROOT_APPS)

