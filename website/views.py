import os

from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.forms import ModelForm, Textarea, TextInput
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django import forms
from tjbaoan import settings
from tjbaoan.settings import CONTACT_TEL, COMPANY_NAME, ABOUT_US, STATIC_FOR_VIEW
from tools.itools import itools
from website.models import Info, User, New


class LogForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '用户名', 'required': 'required', }),
                               max_length=50, error_messages={'required': 'username不能为空', })
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '密 码', 'required': 'required', }),
        max_length=20, error_messages={'required': 'password不能为空', })


# class RegistForm(forms.Form):
class RegistForm(ModelForm):
    class Meta:
        model = Info
        fields = "__all__"
        exclude = ('create_date', 'uuid')
        widgets = {
            'name': TextInput(attrs={'requeird': 'required'}),
            # 'name': TextInput(attrs={'placeholder': 'name'}),
        }




        # username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '姓名', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # sex = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '性别', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # age = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '年龄', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # ethnic = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '民族', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # political_role = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '政治面貌', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # native_place = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '籍贯', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # health = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '身体状况', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # PID = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '身份证号', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # marital_status = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '婚姻状况', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # graduate_institutions = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '毕业院校', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # education_background = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '学历', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # major = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '专业', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # timeofwork = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '参加工作时间', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # wished_salary = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '希望薪金/月', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # contact = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '联系方式', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # addr = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '家庭住址', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # addr = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '家庭住址', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })
    # wanttosay = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '我想说', 'required': 'required', }),max_length=50, error_messages={'required': 'username不能为空', })





# 定义检测登录的装饰器
def check_login(func):
    def wrapper(request, *args, **kwargs):
        # print('in wrapper')
        if request.user.is_authenticated():
            # return HttpResponseRedirect('/login/')
            # print('shi')
            return func(request, *args, **kwargs)
        else:
            # print('fou')
            return redirect('/login/')
    return wrapper


def adduser(request):
    username = 'tjbaoan'
    password = 'tjbaoan'
    try:
        flag = User.objects.get(username=username)
        return HttpResponse("<script>alert('用户已存在');window.location.href='/login/';</script>")

    except Exception as e:
        User.objects.create(password=make_password(username),
                            username=password)
        return HttpResponse("<script>alert('成功');window.location.href='/login/';</script>")




def global_settings(request):
    '''
    此函数用来提供给模板中直接调用settings中的全局变量
    需要在settings TEMPLATES 中添加此函数
    'security.views.global_settings',
    :param request:
    :return:
    '''
    return {
        'CONTACT_TEL': settings.CONTACT_TEL,
    }

def do_logout(request):
    try:
        if request.user.is_authenticated():
            logout(request)
            return HttpResponseRedirect('/index/')
        else:
            return HttpResponse("<script>alert('你还没有登录');window.history.back(-1);</script>")
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/index/')
@csrf_exempt
def do_login(request):
    login_user = request.user.username
    ret = {
        'title': '登录',
        'login_user': login_user,
        'error': '',
    }



    lf = LogForm()
    ret['lf'] = lf

    if request.method == 'POST':
        checkForm = LogForm(request.POST)
        if checkForm.is_valid():
            print(checkForm.cleaned_data['username'], checkForm.cleaned_data['password'])
            try:
                user = User.objects.get(username=checkForm.cleaned_data['username'])
                if user.check_password(checkForm.cleaned_data['password']):
                    print('passwd:{}'.format(checkForm.cleaned_data['password']))
                    login(request, user)
                    return HttpResponse("<script>alert('登录成功');window.location.href='/userfuncs/';</script>")
                else:
                    ret['error'] = '帐号或密码错误，请重新输入。'
                    ret['lf'] = checkForm

            except Exception as e:
                print(e)
                ret['error'] = '帐号或密码错误，请重新输入。'
                ret['lf'] = checkForm

        else:
            errobj = checkForm.errors
            print(type(errobj))

            es = checkForm.errors.as_json()
            print(type(es))
            err = es.split('"')[-2]
            print(err)
            ret['error'] = err
            ret['lf'] = checkForm


    if request.method == 'POST':
        print(request.POST)




    return render(request, 'login.html', ret)


#后台管理页面
def admins(request):

    ret = {}

    return render(request, 'admins/index.html', ret)





#news页面
@csrf_exempt
def news(request):

    #获得所有新闻返回到页面
    news = New.objects.all().order_by('-create_date')
    ret = {
        'news': news,
    }

    return render(request, 'admins/news.html', ret)

#添加news页面
def addNews(request):

    ret = {
    }

    return render(request, 'admins/news/add.html', ret)

#test页面
def testpage(request, a1, a2):
    print("in testpage!")
    ret = {}
    print(a1, a2)
    return render(request, 'admins/test.html', ret)

#test页面
def testpage1(request, module, method):
    print("in testpage111111!")
    print(module, method)
    ret = {}
    return HttpResponse("ok")

#test页面
def adminsModulesDispathcer(request, module=None, method=None):
    print("in adminsModulesDispathcer!")
    print(module, method)
    ret = {}


    if module == "news":
        if method == "add":
            return render(request, "admins/news/add.html", ret)


    return HttpResponse("ok")


@csrf_exempt
def regist(request):
    ret ={}
    rf = RegistForm()


    attrs = (
        '姓名',
        '性别',
        '年龄',
        '民族',
        '政治面貌',
        '籍贯',
        '身体状况',
        '身份证号',
        '婚姻状况',
        '毕业院校',
        '学历',
        '专业',
        '参加工作时间',
        '希望薪金/月',
        '联系方式',
        '家庭住址',
    )
    reg_user_attrs = {
        'education_background': '',
        'marital_status': '',
        'timeofwork': '',
        'age': '',
        'PID': '',
        'health': '',
        'contact': '',
        'ethnic': '',
        'wished_salary': '',
        'wanttosay': '',
        'graduate_institutions': '',
        'political_role': '',
        'sex': '',
        'name': '',
        'major': '',
        'addr': '',
        'native_place': '',
    }
    ret['attrs'] = attrs
    ret['rf'] = rf


    if request.method == 'POST':
        # print(request.POST)
        request_attrs = request.POST
        checkForm = RegistForm(request.POST)
        # print(checkForm.is_valid())
        if checkForm.is_valid():
            # print(checkForm.__dict__['cleaned_data'])
            ret_dict = checkForm.__dict__['cleaned_data']

            for key, val in ret_dict.items():
                for reg_key, reg_val in reg_user_attrs.items():
                    if reg_key == key:
                        reg_user_attrs[reg_key] = val
                        continue

            print(reg_user_attrs)
            try:
                Info.objects.create(
                    name=reg_user_attrs['name'].strip(),
                    sex=reg_user_attrs['sex'].strip(),
                    age=reg_user_attrs['age'].strip(),
                    ethnic=reg_user_attrs['ethnic'].strip(),
                    political_role=reg_user_attrs['political_role'].strip(),
                    native_place=reg_user_attrs['native_place'].strip(),
                    health=reg_user_attrs['health'].strip(),
                    PID=reg_user_attrs['PID'].strip(),
                    marital_status=reg_user_attrs['marital_status'].strip(),
                    graduate_institutions=reg_user_attrs['graduate_institutions'].strip(),
                    education_background=reg_user_attrs['education_background'].strip(),
                    major=reg_user_attrs['major'].strip(),
                    timeofwork=reg_user_attrs['timeofwork'].strip(),
                    wished_salary=reg_user_attrs['wished_salary'].strip(),
                    contact=reg_user_attrs['contact'].strip(),
                    addr=reg_user_attrs['addr'].strip(),
                    wanttosay=reg_user_attrs['wanttosay'],
                )
                return HttpResponse("<script>alert('信息已成功提交.');window.location.href='/index';</script>")
            except Exception as e:
                return HttpResponse("<script>alert('{}');window.location.href='/index';</script>".format(str(e)))
            # print(checkForm.cleaned_data['username'], checkForm.cleaned_data['password'])
            # try:
            #     user = User.objects.get(username=checkForm.cleaned_data['username'])
            #     if user.check_password(checkForm.cleaned_data['password']):
            #         print('passwd:{}'.format(checkForm.cleaned_data['password']))
            #         login(request, user)
            #         return HttpResponse("<script>alert('登录成功');window.location.href='/userfuncs/';</script>")
            #     else:
            #         ret['error'] = '帐号或密码错误，请重新输入。'
            #         ret['lf'] = checkForm
            #
            # except Exception as e:
            #     print(e)
            #     ret['error'] = '帐号或密码错误，请重新输入。'
            #     ret['lf'] = checkForm
        # attrs = {
        #     '姓名': '',
        #     '性别': '',
        #     '年龄': '',
        #     '民族': '',
        #     '政治面貌': '',
        #     '籍贯': '',
        #     '身体状况': '',
        #     '身份证号': '',
        #     '婚姻状况': '',
        #     '毕业院校': '',
        #     '学历': '',
        #     '专业': '',
        #     '参加工作时间': '',
        #     '希望薪金/月': '',
        #     '联系方式': '',
        #     '家庭住址': '',
        # }
        #
        # result = []
        # for key, val in attrs.items():
        #     attrs[key] = request_attrs[key]


        # Info.objects.create(
        #     name=attrs['姓名'].strip(),
        #     sex=attrs['性别'].strip(),
        #     age=attrs['年龄'].strip(),
        #     ethnic=attrs['民族'].strip(),
        #     political_role=attrs['政治面貌'].strip(),
        #     native_place=attrs['籍贯'].strip(),
        #     health=attrs['身体状况'].strip(),
        #     PID=attrs['身份证号'].strip(),
        #     marital_status=attrs['婚姻状况'].strip(),
        #     graduate_institutions=attrs['毕业院校'].strip(),
        #     education_background=attrs['学历'].strip(),
        #     major=attrs['专业'].strip(),
        #     timeofwork=attrs['参加工作时间'].strip(),
        #     wished_salary=attrs['希望薪金/月'].strip(),
        #     contact=attrs['联系方式'].strip(),
        #     addr=attrs['家庭住址'].strip(),
        # )
        #
        # return HttpResponse("<script>alert('信息已成功提交');window.location.href='/index';</script>")

        return HttpResponse('信息已成功提交。(js未启用)')




    return render(request, 'regist.html', ret)
def index(request):

    ret = {
        'tel': CONTACT_TEL,
        'com_name': COMPANY_NAME,
        'about_us': ABOUT_US,
        'title': 'title'
    }

    rootdir = STATIC_FOR_VIEW + '/images/xuanchuan/'  # 指明被遍历的文件夹
    caseShowPicsDir = STATIC_FOR_VIEW + '/images/caseshow/'  # 指明被遍历的文件夹
    # rootdir = STATIC_ROOT + '/images/xuanchuan/'  # 指明被遍历的文件夹
    # print(rootdir)
    # print(os.path.exists(rootdir))
    file_names = itools.retrive(rootdir=rootdir)['files']
    caseShowPics = itools.retrive(rootdir=caseShowPicsDir)['files']

    ret['file_names'] = file_names
    ret['caseShowPics'] = caseShowPics
    return render(request, 'index.html', ret)

def join_us(request):
    # return HttpResponse('asdf')
    ret = {}
    with open(STATIC_FOR_VIEW + '/docs/zhaopin.txt') as f:
        lines = f.readlines()
    ret['lines'] = lines
    return render(request, 'joinus.html', ret)

@check_login
def info(request):
    login_user = request.user.username
    ret = {
        'title': '信息列表',
        'login_user': login_user,
    }

    if request.method == 'GET':
        act = request.GET.get('act')
        if act == 'del':
            try:
                uuid = request.GET.get('uuid')
                Info.objects.get(uuid=uuid).delete()
                return HttpResponse("<script>alert('ID为：{}的信息已成功删除.');window.location.href='/info/';</script>".format(uuid))
            except Exception as e:
                print(e)








    infos = Info.objects.all().order_by('-create_date')

    paginator = Paginator(infos, 10)

    try:
        page = int(request.GET.get('page', 1))  # 1是没有数据的默认值
        print('page = {}'.format(page))
        infos = paginator.page(page)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        infos = paginator.page(1)

    ret['pages'] = infos.paginator.num_pages
    ret['count'] = infos.paginator.count


    ret['infos'] = infos
    return render(request, 'infos.html', ret)



def rongyu(request):
    ret = {
        'title': '荣誉资质',
        'pic': None
    }

    ids = ['images/certificate/certificate1 - 副本.jpg',
           'images/certificate/certificate2 - 副本.jpg',
           'images/certificate/certificate3 - 副本.jpg'
           ]
    if request.GET:
        if request.GET.get('id'):
            id = request.GET.get('id')
            ret['pic'] = ids[int(id) - 1]



    return render(request, 'rongyu.html', ret)

@check_login
def detail(request):
    ret = {
        'title': '详细信息'
    }
    if request.method == 'GET':
        uuid = request.GET.get('uuid')
        information = Info.objects.get(uuid=uuid)

        retinfo = (
            ('姓名', information.name),
            ('性别', information.sex),
            ('年龄', information.age),
            ('民族', information.ethnic),
            ('政治面貌', information.political_role),
            ('籍贯', information.native_place),
            ('身体状况', information.health),
            ('身份证号', information.PID),
            ('婚姻状况', information.marital_status),
            ('毕业院校', information.graduate_institutions),
            ('学历', information.education_background),
            ('参加工作时间', information.timeofwork),
            ('希望薪金 / 月', information.wished_salary),
            ('联系方式', information.contact),
            ('家庭住址', information.addr),
            ('自我描述', information.wanttosay),
        )



        ret['info'] = retinfo

    return render(request, 'detail.html', ret)


@check_login
def userfuncs(request):
    login_user = request.user.username
    ret = {
        'title': '用户页面',
        'login_user': login_user,
    }


    if request.method == 'GET':
        act = request.GET.get('act')
        if act == 'logout':
            do_logout(request)
            return HttpResponseRedirect('/index/')
            # return HttpResponse('logout')



    return render(request, 'userfuncs.html', ret)
