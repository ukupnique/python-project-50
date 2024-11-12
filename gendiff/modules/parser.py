import json
import yaml


def parser(data, format: str):
    if format == 'json':
        return json.load(data)
    if format == 'yaml':
        return yaml.safe_load(data)
