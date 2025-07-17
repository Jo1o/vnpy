"""
Global setting of the trading platform.
"""

from logging import CRITICAL
from tzlocal import get_localzone_name

from .utility import load_json


SETTINGS: dict = {
    "font.family": "微软雅黑",
    "font.size": 12,

    "log.active": True,
    "log.level": CRITICAL,
    "log.console": True,
    "log.file": True,

    "email.server": "smtp.qq.com",
    "email.port": 465,
    "email.username": "",
    "email.password": "",
    "email.sender": "",
    "email.receiver": "",

    "datafeed.name": "xt",
    "datafeed.username": "token",
    "datafeed.password": "319733dd62c87010e5fe61c0aacedf9d70ccdbe0",

    "database.timezone": get_localzone_name(),
    "database.name": "mysql",
    "database.database": "nvpy",
    "database.host": "127.0.0.1",
    "database.port": 3306,
    "database.user": "root",
    "database.password": "123456"
}


# Load global setting from json file.
SETTING_FILENAME: str = "vt_setting.json"
SETTINGS.update(load_json(SETTING_FILENAME))
