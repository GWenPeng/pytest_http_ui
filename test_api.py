import pytest


def test_api_Get(api, sql):
    res = api.Get(url="/api/document-domain-management/v1/domain/self")
    print(res.status_code, res.content)
    assert res.status_code == 200
    with sql as sql_cli:
        sql_cli.execute(query="SELECT  * FROM domain_mgnt.t_domain_self ;")
        result = sql_cli.fetchone()
        print(result)


def test_api_Put(api):
    json = {
        "encryption_algorithm": "DES"
    }
    res = api.Put(url="/api/read-policy/v1/encrypted/template/eb7ed425-ed4e-4045-9498-05be3b56fbaf", json=json)
    print(res.status_code, res.content)
    assert res.status_code == 200


@pytest.mark.asyncio
async def test_aio_get(aioapi, aiosql):
    """
    异步http Get方法
    #https://www.cntofu.com/book/127/aiohttp%E6%96%87%E6%A1%A3/StreamingAPI.md
    :param aioapi:
    :return:
    """

    StreamReader = await aioapi.get(url="/api/document-domain-management/v1/domain/self")
    jsondata = await StreamReader.json()
    # context = await StreamReader.content.read()
    print(StreamReader.status, jsondata)
    # async with aioapi as session:
    #     StreamReader = await session.get(url="/api/document-domain-management/v1/domain/self")
    #     jsondata = await StreamReader.json()
    #     print(StreamReader.status, jsondata)

    async with aiosql.cursor() as cursor:
        await cursor.execute("SELECT  * FROM domain_mgnt.t_domain_self ;")
        resl = await cursor.fetchone()
        print(resl)
