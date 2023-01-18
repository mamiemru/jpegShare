#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import stat
import shutil
import tempfile

from PIL import Image

from typing import List
from typing import Dict

from repository.imagesRepository import ImageRepository

from utils.constant         import FOLDER_BASE_PATH
class ImagesService():

    tmp_file = tempfile.TemporaryFile(mode='w', suffix='.png')

    @staticmethod
    def getTicketImageLink(imageName, extention=".png", folder="tickets"):
        return ImageRepository.getImageLink(imageName, extention, folder=folder)

    @staticmethod
    def getIconsImageLink(imageName, extention=".png", folder="icons"):
        return ImageRepository.getImageLink(imageName, extention, folder=folder)

    @staticmethod
    def getArticlesImageLink(imageName, extention=".png", folder="articles"):
        return ImageRepository.getImageLink(imageName, extention, folder=folder)
    
    @staticmethod
    def getImageLink(imageName, extention=".png", folder=""):
        return ImageRepository.getImageLink(imageName, extention, folder=folder)

    @staticmethod
    def getListOfArticles():
        return ImageRepository.listDir("images/articles")
    
    @staticmethod
    def resize(imageName, width=1000, height=1500, extention=".png"):
        fileImage = ImagesService.getImageLink(imageName, extention=extention)
        file : Image = Image.open(fileImage)
        file = file.resize((width, height))
        file.save(fileImage, extention)

    @staticmethod
    def exist(imageName, extention=".png", folder="tickets"):
        fileImage = ImagesService.getImageLink(imageName, extention=extention, folder=folder)
        return ImagesService.locationExist(fileImage)

    @staticmethod
    def locationExist(filename):
        return os.path.exists(filename)

    @staticmethod
    def convertAndSave(src, dest):
        img : Image = Image.open(src)
        img.save(dest)

    @staticmethod
    def rotate(src, deg=90):
        img : Image = Image.open(src)
        img = img.rotate(deg, Image.NEAREST, expand=1)
        img.save(src)

    @staticmethod
    def copy(src, dest):
        shutil.copy2(src, dest)

    @staticmethod
    def move(src, dest):
        shutil.move(src, dest)
