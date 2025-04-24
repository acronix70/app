import os
import server
from aiohttp import web
from aiohttp_cors import CorsConfig, setup as setup_cors

# HOME_APPS
WEBROOT_APPS = os.path.join(os.path.dirname(os.path.realpath(__file__)), "docs")

# Inicializar servidor
app = web.Application()

# Configuración de CORS
cors = setup_cors(app, defaults={
    "https://acronix70.github.io": {  # Dominio permitido
        "allow_credentials": True,   # Permitir cookies y autenticación
        "allow_headers": "*",        # Permitir cualquier encabezado
        "allow_methods": "*",        # Permitir todos los métodos (GET, POST, etc.)
    }
})

# Ruta principal para servir index.html
@app.get("/")
async def apps_entrance(request):
    return web.FileResponse(os.path.join(WEBROOT_APPS, "index.html"))

# Servir archivos estáticos en la ruta raíz
app.router.add_static("/", WEBROOT_APPS)

# Registrar rutas con soporte de CORS
entrance_route = app.router.add_get("/", apps_entrance)
cors.add(entrance_route)

# Ejecutar el servidor
web.run_app(app, port=8188)
