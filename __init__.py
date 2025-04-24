import os
import server
from aiohttp import web

# HOME_APPS
WEBROOT_APPS = os.path.join(os.path.dirname(os.path.realpath(__file__)), "docs")

@server.PromptServer.instance.routes.get("/")
def apps_entrance(request):
    return web.FileResponse(os.path.join(WEBROOT_APPS, "index.html"))

# Sirve las carpetas estáticas necesarias
server.PromptServer.instance.routes.static("/css", os.path.join(BASE_DIR, "css"))
server.PromptServer.instance.routes.static("/js", os.path.join(BASE_DIR, "js"))
server.PromptServer.instance.routes.static("/js", os.path.join(BASE_DIR, "workflow_api"))

