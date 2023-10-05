import re
import json
from contextlib import suppress
from json.decoder import JSONDecodeError
from typing import List, Optional

import requests
from scrapy.selector import Selector

json_template = re.compile(r"({[^}]+})")


def _extract(raw_data: str) -> List[Optional[dict]]:
    """Extract JSON data from html string"""
    script_list = Selector(text=raw_data).xpath("//script/text()").getall()

    data = []
    for script in script_list:
        with suppress(JSONDecodeError):
            data.append(json.loads(script))

    return data


def extract_from_html(raw_data: str) -> List[Optional[dict]]:
    """Extract JSON data from html string"""
    return _extract(raw_data)


def extract_from_url(url: str) -> List[Optional[dict]]:
    """Request html from url and Extract JSON data from this html"""
    resp = requests.get(url)
    if resp.status_code == 200:
        return _extract(resp.text)


def extract_from_file(file_path: str) -> List[Optional[dict]]:
    """Extract JSON data from html file"""
    with open(file_path, "r") as f:
        raw_data = f.read()

    return _extract(raw_data)
