from typing import Any
from pathlib import Path
from constants.constants import FILE_PATH
import json
from dataclasses import asdict
from datetime import datetime
from enum import Enum

def json_default(obj:Any):
    if isinstance(obj,datetime):
        return obj.isoformat()

    if isinstance(obj,Enum):
        return obj.value

    raise TypeError(f"Cannot serialize {obj}")

def save(objects: Any, file_path: str | None = None):
    if file_path is None:
        file_path = str(Path(__file__).resolve().parent.parent / "data" / FILE_PATH)

    with open(file_path, "w") as file:
        json.dump([asdict(obj) for obj in objects], file, indent=4, default=json_default)

    return True

def load(file_path:str | None = None):
    if file_path is None:
        file_path = str(Path(__file__).resolve().parent.parent / "data" / FILE_PATH)

    with open(file_path) as file:
        records = json.load(file)

    return records

    



