import inspect
import os
from enum import Enum
from types import MappingProxyType, ModuleType
from typing import Any, Mapping
from pythonrestapi import config_default

Config = Mapping[str, Any]

_config: dict = {}


class SpecNotFound(Exception):
    pass


def _read_configs(config_module: ModuleType) -> None:
    for config_key in dir(config_module):
        config_value = getattr(config_module, config_key)
        if not config_key.startswith("_") and not inspect.ismodule(config_value):
            _config[config_key] = config_value


_read_configs(config_default)

_config_file = os.getenv("PYTHON_REST_API_CONFIG_FILE")
if _config_file:
    from importlib import util

    spec = util.spec_from_file_location("restaurantapi_config_file", _config_file)
    if spec is None:
        raise SpecNotFound()
    config_module = util.module_from_spec(spec)
    spec.loader.exec_module(config_module)  # type: ignore
    _read_configs(config_module)

config: Config = MappingProxyType(_config)


class Env(str, Enum):
    PROD = "prod"
    MASTER = "master"
    TEST = "test"
    DEVELOPMENT = "development"
    DEFAULT = "default"


def get_env() -> Env:
    return Env(config.get("ENV_NAME"))


def env_is_prod() -> bool:
    return get_env() == Env.PROD


def env_is_test() -> bool:
    return get_env() == Env.TEST


def env_is_development() -> bool:
    return get_env() == Env.DEVELOPMENT
