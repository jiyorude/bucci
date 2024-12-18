from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import os
from utilities import Utilities

app = FastAPI()
api = Utilities()

try:
    api.iterate(0.8, 0.025, *"BUWDA (Bucci Unified Weather Database Application)")
    api.wait(1)
    IMAGES_DIR = Path(__file__).parent / "icons"
    if not IMAGES_DIR.exists():
        raise NotADirectoryError
except NotADirectoryError:
    api.iterate(0.8, 0.025, *"ERROR: Could not start BUWDA. Icons folder does not exist. Create a icons folder in the weather_data folder.")