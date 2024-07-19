from aiohttp import web

RENAME_PRO = web.RouteTableDef()

@RENAME_PRO.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("HxBots Developer")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(RENAME_PRO)
    return web_app

