import logging
import typing

from baseplate import Baseplate
from baseplate.clients.sqlalchemy import SQLAlchemySession
from baseplate.frameworks.pyramid import BaseplateConfigurator
from baseplate.frameworks.pyramid import BaseplateRequest
from baseplate.lib import config
from pyramid.config import Configurator
from pyramid.response import Response

from . import models

if typing.TYPE_CHECKING:
    from wsgiref.types import WSGIApplication  # noqa: F401


logger = logging.getLogger(__name__)


class GalaxyExpressService:
    def is_healthy(self, _request: BaseplateRequest) -> Response:
        return True

    # TODO: implement your service's endpoints here

    def example(self, request: BaseplateRequest) -> None:
        """Handle example endpoint.

        This just shows off how to query from the database. Feel free to
        delete it or repurpose it as desired.

        """
        request.database.query(models.ExampleModel).all()


def make_wsgi_app(app_config: config.RawConfig) -> "WSGIApplication":
    baseplate = Baseplate(app_config)
    baseplate.configure_observers()
    baseplate.configure_context({
        "database": SQLAlchemySession(),
    })

    configurator = Configurator(settings=app_config)
    baseplate_configurator = BaseplateConfigurator(baseplate)
    configurator.include(baseplate_configurator.includeme)

    controller = GalaxyExpressService()

    # Wire up the health endpoint
    configurator.add_route("health", "/health", request_method="GET")
    configurator.add_view(controller.is_healthy, route_name="health", renderer="json")
    
    # TODO: add more routes and views here

    return configurator.make_wsgi_app()
