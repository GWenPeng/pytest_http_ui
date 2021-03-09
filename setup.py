from setuptools import setup
setup(
    name="pytest_http_ui",
    author="gu.wenpeng",
    packages=["pytest_http_ui","pytest_http_ui.api","pytest_http_ui.ui"],
    version="0.1.0",
    author_email="gu.wenpeng@aishu.cn",
    entry_points={
        "pytest11":["pytest_http_ui = pytest_http_ui.plugin"] #pytest11 入口
    },
    classifilers=["Framework :: Pytest"],
    install_requires=[
        'pytest',"requests","selenium",'pymysql','aiomysql','aiohttp','pytest-asyncio','paramiko'
    ],
)

#安装 pip install .