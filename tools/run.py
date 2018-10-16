import os, django
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tjbaoan.settings")# project_name 项目名称
django.setup()

from django.contrib.auth.hashers import make_password

from website.models import User
from tjbaoan.settings import BASE_DIR, STATIC_FOR_VIEW

if __name__ == '__main__':


    path = STATIC_FOR_VIEW + '/docs/zhaopin.txt'

    with open(path, 'r+') as f:
        lines = f.readlines()
        pattern = r"^\\t$"
        for line in lines:
            a = re.compile(pattern=pattern)
            print(a.sub('&nbsp;', line))

        print(lines)



    pass

    # with open(STATICFILES_DIRS[0] + '/docs/zhaopin.txt') as f:
    #     lines = f.readlines()
    #
    #
    # for i in lines:
    #     print(i)
    # rootdir = STATICFILES_DIRS[0] + '/images/xuanchuan/'  # 指明被遍历的文件夹
    # print(rootdir)
    #
    # print(os.path.exists(rootdir))
    # file_names = []
    # file_names = itools.retrive(rootdir=rootdir)['files']
    #
    # print(file_names)
