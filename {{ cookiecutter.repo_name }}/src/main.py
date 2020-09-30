#!/usr/bin/env python3

import datetime
from util import load_config, setup_logger

import click


@click.command()
@click.option('--conf', '-c', default="./config/config.yaml")
@click.option('--log', '-l', default='../logs/{0}.log'.format(datetime.date.today()))
def main(conf: str,
         log: str,):
    # 設定を読み込み
    conf = load_config(conf)
    # 保存するファイル名を指定
    log_file = log
    # ログの初期設定を行う
    logger = setup_logger(log_file)
    logger.debug("test")


if __name__ == '__main__':
    main()
