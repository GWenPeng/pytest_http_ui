import pytest
from .api.api_cli import api_cli
from .api.get_token import Token
from .api.sql_cli import sql_cli
from .api.sql_cli import aiomysql_cli
from .api.api_cli import aioApi_cli


def pytest_addoption(parser):
    parser.addini('protocol', type="string", default="https", help="http or https")
    parser.addini('host', type="string", default="127.0.0.1", help="接口访问地址")
    parser.addini('port', type=None, default=443, help="接口访问端口号")
    parser.addini('headers', type=None, default=None, help="默认headers")
    parser.addini('timeout', type=None, default=3000.00, help="超时时间")
    parser.addini('verify', type="bool", default=False, help="是否开启ssl验证")

    parser.addini('db_user', type="string", default='Anyshare', help="数据库账号")
    parser.addini('db_password', type="string", default="asAlqlTkWU0zqfxrLTed", help="数据库密码")
    parser.addini('db_database', type="string", default='domain_mgnt', help="数据库名")


@pytest.fixture(scope="session",autouse=False)
def session_token(pytestconfig):
    host = pytestconfig.getini("host").strip('"')
    token = Token(host=host).get_token()
    yield token["access_token"]


@pytest.fixture(scope="session",autouse=False)
def apiconfig(pytestconfig):
    host = pytestconfig.getini("host").strip('"')
    port = pytestconfig.getini("port").strip('"')
    headers = pytestconfig.getini("headers").strip('"')
    protocol = pytestconfig.getini("protocol").strip('"')
    timeout = pytestconfig.getini("timeout").strip('"')
    verify = pytestconfig.getini("verify")
    headers = eval(headers)
    yield host, port, headers, protocol, timeout, verify


@pytest.fixture(scope="session",autouse=False)
def sqlconfig(pytestconfig):
    host = pytestconfig.getini("host").strip('"')
    db_user = pytestconfig.getini("db_user").strip('"')
    db_password = pytestconfig.getini("db_password").strip('"')
    db_database = pytestconfig.getini("db_database").strip('"')
    yield host, db_user, db_password, db_database


@pytest.fixture(scope="function")
def api(session_token, apiconfig):
    host, port, headers, protocol, timeout, verify = apiconfig
    if "Authorization" not in headers:
        headers["Authorization"] = "Bearer " + session_token
    yield api_cli(protocol, host, port, headers, verify, timeout)


@pytest.fixture(scope="function")
def sql(sqlconfig):
    host, db_user, db_password, db_database = sqlconfig
    yield sql_cli(host=host, user=db_user, password=db_password, database=db_database)


@pytest.fixture(scope="function")
async def aiosql(sqlconfig):
    host, db_user, db_password, db_database = sqlconfig
    async with aiomysql_cli(host=host, user=db_user, password=db_password, database=db_database) as conn:
        yield conn


@pytest.fixture(scope="function")
async def aioapi(apiconfig, session_token):
    host, port, headers, protocol, timeout, verify = apiconfig
    if "Authorization" not in headers:
        headers["Authorization"] = "Bearer " + session_token
    yield aioApi_cli(protocol, host, port, headers, verify, timeout)
