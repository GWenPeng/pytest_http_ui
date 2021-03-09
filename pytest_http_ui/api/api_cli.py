import requests
import warnings
import aiohttp
from urllib3.exceptions import InsecureRequestWarning

warnings.filterwarnings(action='ignore', category=InsecureRequestWarning)


class api_cli:
    def __init__(self, protocol, host, port, headers, verify, timeout):
        self.protocol = protocol
        self.port = port
        self.host = host
        self.headers = headers
        self.timeout = timeout
        self.verify = verify

    def Get(self, url, params=None, **kwargs):
        url = ''.join([self.protocol, "://", self.host, ':', self.port, url])
        res = requests.get(url=url, params=params, headers=self.headers, timeout=float(self.timeout),
                           verify=self.verify, **kwargs)
        return res

    def Post(self, url, params=None, json=None, **kwargs):
        url = ''.join([self.protocol, "://", self.host, ':', self.port, url])
        res = requests.post(url=url, params=params, json=json, headers=self.headers, timeout=float(self.timeout),
                            verify=self.verify, **kwargs)
        return res

    def Put(self, url, data=None, json=None, **kwargs):
        url = ''.join([self.protocol, "://", self.host, ':', self.port, url])
        res = requests.put(url=url, data=data, json=json, headers=self.headers, timeout=float(self.timeout),
                           verify=self.verify, **kwargs)
        return res

    def Delete(self, url, **kwargs):
        url = ''.join([self.protocol, "://", self.host, ':', self.port, url])
        res = requests.delete(url=url, headers=self.headers, timeout=float(self.timeout),
                              verify=self.verify, **kwargs)
        return res

    def Path(self, url, data=None, **kwargs):
        url = ''.join([self.protocol, "://", self.host, ':', self.port, url])
        res = requests.patch(url=url, data=data, headers=self.headers, timeout=float(self.timeout),
                             verify=self.verify, **kwargs)
        return res

    def Request(self, method, url, **kwargs):
        url = ''.join([self.protocol, "://", self.host, ':', self.port, url])
        res = requests.request(method=method, url=url, **kwargs)
        return res


class aioApi_cli(object):
    def __init__(self, protocol, host, port, headers, verify, timeout):
        self.protocol = protocol
        self.port = port
        self.host = host
        self.headers = headers
        self.timeout = timeout
        self.verify = verify

    async def get(self, url, **kwargs):
        url = ''.join([self.protocol, "://", self.host, ':', self.port, url])
        async with aiohttp.ClientSession() as session:
            StreamReader = await session.get(url, headers=self.headers, ssl=self.verify, **kwargs)
        return StreamReader

    # async def __aenter__(self):
    #     return self
    #
    # async def __aexit__(self, exc_type, exc_val, exc_tb):
    #     pass
