import os
import server
from aiohttp import web

# Servir desde la carpeta actual donde está este script
WEBROOT_APPS = os.path.dirname(os.path.realpath(__file__))

@server.PromptServer.instance.routes.get("/")
def apps_entrance(request):
    return web.FileResponse(os.path.join(WEBROOT_APPS, "index.html"))

# Ruta estática para servir archivos (JS, CSS, imágenes, etc.)
server.PromptServer.instance.routes.static("/", path=WEBROOT_APPS)
