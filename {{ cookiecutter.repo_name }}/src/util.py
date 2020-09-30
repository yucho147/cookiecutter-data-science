#!/usr/bin/env python3

from attrdict import AttrDict
from logging import getLogger, StreamHandler, Formatter, FileHandler, DEBUG
import yaml


def load_config(config_path: str) -> AttrDict:
    """config(yaml)ファイルを読み込む

    Parameters
    ----------
    config_path : string
        config fileのパスを指定する

    Returns
    -------
    config : attrdict.AttrDict
        configを読み込んでattrdictにしたもの
    """
    with open(config_path, 'r', encoding='utf-8') as fi_:
        return AttrDict(yaml.load(fi_, Loader=yaml.SafeLoader))


def setup_logger(log_file, modname=__name__):
    """loggerの設定

    Parameters
    ----------
    log_file : string
        出力logファイル

    Returns
    -------
    logger
        logger
    """
    logger = getLogger(modname)
    logger.setLevel(DEBUG)

    sh = StreamHandler()
    sh.setLevel(DEBUG)
    formatter = Formatter(('%(asctime)s - '
                           '%(name)s - '
                           '%(levelname)s - '
                           '%(message)s'))
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    fh = FileHandler(log_file)  # fh = file handler
    fh.setLevel(DEBUG)
    fh_formatter = Formatter(('%(asctime)s - '
                              '%(filename)s - '
                              '%(name)s - '
                              '%(lineno)d - '
                              '%(levelname)s - '
                              '%(message)s'))
    fh.setFormatter(fh_formatter)
    logger.addHandler(fh)
    return logger
