
import os
from pathlib import Path

from utils.constant import FOLDER_BASE_PATH

class ImageRepository():

    @staticmethod
    def listDir(folder=""):
        p : Path = Path(FOLDER_BASE_PATH) / folder 
        return os.listdir(str(p.absolute()))

    @staticmethod
    def getImageLink(imageName, extention=".png", folder=""):
        if type(imageName) is str:
            imageName = imageName.replace('/', '-')
        p : Path = Path(FOLDER_BASE_PATH) / folder / imageName
        p : Path = p.with_suffix(extention)
        return str(p.absolute())