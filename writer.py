from typing import Any, Callable

import json
from os import path, makedirs
from functools import partial

from api import BilibiliApi


def write_md(md_str: str, filepath:str) -> None:
    encoder = lambda x: x
    _write(md_str, encoder, filepath)


def write_raw_data(raw_videos: BilibiliApi.RAW_DATA_T, filepath:str) -> None:
    encoder = partial(json.dumps, ensure_ascii=False)

    _write(raw_videos, encoder, filepath)


def _write(raw_data: Any, encoder: Callable[[Any], str], filepath: str) -> None:
    makedirs(path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w+') as f:
        f.write(encoder(raw_data))
