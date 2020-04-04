import os
import yaml

from typing import List


def _env_constructor(loader, node):
    key = str(loader.contruct.scalar(node))
    return os.getenv(key, None)


yaml.SafeLoader.add_constructor("!ENV", _env_constructor)


with open("config.yml", encoding="UTF-8") as f:
    _CONFIG = yaml.safe_load(f)


class YAMLMeta(type):
    subsection = None

    def __getattr__(cls, name):
        name = name.lower()

        if cls.subsection is not None:
            return _CONFIG[cls.section][cls.subsection][name]
        return _CONFIG[cls.section][name]

        def __getitem__(cls, name):
            return cls.__getattr__(name)

        def __iter__(cls):
            for name in cls.__annotations__:
                yield name, getattr(cls, name)


class Bot(metaclass=YAMLMeta):
    section = "bot"

    token: str
    prefix: str


class Datebase(metaclass=YAMLMeta):
    section = "database"

    connection_string: str


class IDS(metaclass=YAMLMeta):
    section = "ids"

    creators: List[int]
    benny: int


class Originator(metaclass=YAMLMeta):
    section = "originator"

    name: str


class Emoji(metaclass=YAMLMeta):
    section = "emoji"

    _0: str
    _1: str
    _2: str
    _3: str
    _4: str
    _5: str
    _6: str
    _7: str
    _8: str
    _9: str

    checkmark: str


class AdvConfig(metaclass=YAMLMeta):
    section = "adv_config"

    queue_size: str
