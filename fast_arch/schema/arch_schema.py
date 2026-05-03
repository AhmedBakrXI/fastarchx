from typing import List, Dict
from pydantic import BaseModel
import json

# 1. Define the "Shape" of your data
class Feature(BaseModel):
    description: str
    files: List[str]

class Architecture(BaseModel):
    name: str
    description: str
    folders: List[str]
    files: List[str]
    features: Dict[str, Feature] # Maps "auth" to a Feature object

class ArchitectureConfig(BaseModel):
    architectures: List[Architecture]

