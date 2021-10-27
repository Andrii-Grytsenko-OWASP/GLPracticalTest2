from pytest import *

from gorest import config as cfg
from gorest.api.gorest_api import *


@fixture(scope="class")
def api():
    gorestapi = GoRestApi(cfg.API_BASE_URL, cfg.API_TOKEN)
    yield gorestapi
    del gorestapi
