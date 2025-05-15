import json
from typing import Any


def json_configs_merge(*json_paths: str) -> dict[str, Any]:
    def merge_dicts(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        for key, value in b.items():
            if key in a and isinstance(a[key], dict) and isinstance(value, dict):
                a[key] = merge_dicts(a[key], value)
            else:
                a[key] = value
        return a

    merged_config = {}
    for path in json_paths:
        with open(path, 'r') as f:
            data = json.load(f)
            merged_config = merge_dicts(merged_config, data)
    return merged_config


if __name__ == '__main__':
    # Example usage; make sure the files exist for this to run.
    config = json_configs_merge('./katas/configs/default.json', './katas/configs/production.json', './katas/configs/us-east-1-production.json')
    print(config)

