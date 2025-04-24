import os
import server
from aiohttp import web

# Configuración del directorio raíz (donde están css, js, etc.)
WEBROOT_APPS = os.path.join(os.path.dirname(os.path.realpath(__file__)), "docs")

# Ruta principal para servir index.html
@server.PromptServer.instance.routes.get("/")
async def apps_entrance(request):
    return web.FileResponse(os.path.join(WEBROOT_APPS, "index.html"))

# Configurar rutas estáticas para css, js, e imágenes
server.PromptServer.instance.routes.static("/css", path=os.path.join(WEBROOT_APPS, "css"))
server.PromptServer.instance.routes.static("/js", path=os.path.join(WEBROOT_APPS, "js"))
server.PromptServer.instance.routes.static("/images", path=os.path.join(WEBROOT_APPS, "images"))  # Ejemplo para imágenes

# Rutas adicionales para otros archivos (como JSON o documentos)
@server.PromptServer.instance.routes.get("/{filename}")
async def serve_files(request):
    filename = request.match_info['filename']  # Obtener el nombre del archivo solicitado
    file_path = os.path.join(WEBROOT_APPS, filename)  # Construir la ruta completa
    if os.path.exists(file_path):  # Verificar que el archivo existe
        return web.FileResponse(file_path)
    else:
        return web.json_response({"error": "Archivo no encontrado"}, status=404)
