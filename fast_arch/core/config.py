from typing import List
from dataclasses import dataclass

@dataclass
class ProjectConfig:
    name: str
    arch: str
    features: List[str]


