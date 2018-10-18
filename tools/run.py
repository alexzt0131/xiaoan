import os, django
import re

import time

from tools.itools import itools

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tjbaoan.settings")# project_name 项目名称
django.setup()

from django.contrib.auth.hashers import make_password

from website.models import User, Photo
from tjbaoan.settings import BASE_DIR, STATIC_FOR_VIEW

if __name__ == '__main__':

    # def synStaticDircaseDemoPic2DB():
    #     filePaths = []
    #     # rootdir = STATIC_FOR_VIEW + '/images/xuanchuan/'  # 指明被遍历的文件夹
    #     caseShowPicsDir = STATIC_FOR_VIEW + '/images/caseshow/'  # 指明被遍历的文件夹
    #     # rootdir = STATIC_ROOT + '/images/xuanchuan/'  # 指明被遍历的文件夹
    #     # print(rootdir)
    #     # print(os.path.exists(rootdir))
    #     # file_names = itools.retrive(rootdir=rootdir)['files']
    #     caseShowPics = itools.retrive(rootdir=caseShowPicsDir)['files']
    #     print(caseShowPics)
    #     #遍历所有案例展示的图片地址存入到集合中
    #     for filename in caseShowPics:
    #         filePaths.append(caseShowPicsDir + filename)
    #
    #     for i in filePaths:
    #         # print(i)
    #
    #         photo = Photo()
    #         photo.file_path = i
    #         photo.file_name = i.split('/')[-1]
    #         photo.save()
    #
    # synStaticDircaseDemoPic2DB()



    pass
