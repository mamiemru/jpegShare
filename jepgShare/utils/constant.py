import os
from pathlib import Path

def getFolderBasePath():
    p = Path(os.curdir) / 'images'
    return str(p.absolute())

FOLDER_BASE_PATH=getFolderBasePath()