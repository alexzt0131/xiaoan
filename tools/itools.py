import os

from django.shortcuts import render


class itools():

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

        # for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        #     # for dirname in dirnames:  # 输出文件夹信息
        #     #     print("parent is:" + parent)
        #     #     print("dirname is" + dirname)
        #     print(filenames)
        #     for filename in filenames:  # 输出文件信息
        #
        #         # print("parent is:" + parent)
        #         print("in retrive_filename is:" + filename)
        #
        #         # full_path = os.path.join(parent, filename)# 输出文件路径信息

        return ret