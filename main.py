from litestar import Litestar
from litestar.template import TemplateConfig
from litestar.static_files import StaticFilesConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from pathlib import Path

from app.home import HomeController

app = Litestar(
    route_handlers=[HomeController],
    template_config=TemplateConfig(
        directory=Path("templates"),
        engine=JinjaTemplateEngine,
    ),
    static_files_config=[
        StaticFilesConfig(directories=["static"], path="/static"),
    ],
)