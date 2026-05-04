import json

from fastarchx.schema.arch_schema import ArchitectureConfig
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ARCH_CONFIG_JSON_FILE = BASE_DIR / "architectures" / "arch.json"

def get_architectures(file_path: str) -> ArchitectureConfig:
    with open(file_path, 'r') as f:
        raw_data = json.load(f)
    
    # This validates the JSON against your classes above
    return ArchitectureConfig(**raw_data)


def read_arch_config_json() -> ArchitectureConfig:
    return get_architectures(ARCH_CONFIG_JSON_FILE.__str__())

