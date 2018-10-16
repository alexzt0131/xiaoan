import os
from django.test import TestCase

# Create your tests here.
from tjbaoan.settings import STATIC_FOR_VIEW
from tools import itools


def retrive(rootdir=''):
    '''
    #遍历特定文件夹内文件名
    '''
    ret = {
        'files': None
    }
    # rootdir = 'static/images'  # 指明被遍历的文件夹
    for parent, dirnames, file_names in os.walk(rootdir):
        ret['files'] = file_names


    return ret

caseShowPicsDir = r'D:\PycharmProjects\tjbaoan\static\images\caseshow'  # 指明被遍历的文件夹

caseShowPics = retrive(rootdir=caseShowPicsDir)['files']

for i in caseShowPics:
    print(i)