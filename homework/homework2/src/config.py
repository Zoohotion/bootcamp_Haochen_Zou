from dotenv import load_dotenv
import os
from pathlib import Path
from typing import Optional

def load_env():
    load_dotenv()

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)

PROJECT_ROOT = Path.cwd()
DATA_DIR = PROJECT_ROOT / "data"

