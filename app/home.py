from litestar import Controller, get
from litestar.response import Template


class HomeController(Controller):
    path = "/"

    @get()
    async def index(self) -> Template:
        return Template("home.html", context = {"title": "Добро пожаловать!"})