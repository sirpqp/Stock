from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import json
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate, login, logout
import logging
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
# 判断提交方式
    # post
        # 获取用户名密码，判断是否为空
        # 获取用户名密码，判断是否存在
    # get
# 获取前端用户名密码
# 判断用户名是否存在
# 密码加密
# 保存
# session
# cookie
# 返回
def register_(request):
    if request.method == "POST":
        new_user = UserInfo()
        new_user.username = request.POST.get('usernmae','')
        if not new_user.username:
            return HttpResponse(json.dumps({'result':False,'data':'','error':'用户名不能为空'}))
        elif UserInfo.objects.filter(username=new_user.username):
            return HttpResponse(json.dumps({'result':False,'data':'','error':'用户名已存在'}))
        password = request.POST.get('password','')
        if not password:
            return HttpResponse(json.dumps({'result': False, 'data': '', 'error': '密码不能为空'}))
        if password != request.POST.get('cpassword'):
            return HttpResponse(json.dumps({'result': False, 'data': '', 'error': '两次密码不一致'}))
        # make_password(明文,None,加密方式),返回值为密文
        # check_password(明文,密文),验证明文，密文是否一致,返回值为True/False
        new_user.password = make_password(password, None, 'pbkdf2_sha1')
        new_user.email = request.POST.get('email','')
        new_user.birth = request.POST.get('birth','')
        new_user.sex = request.POST.get('sex','')
        new_user.save()
        return HttpResponse(json.dumps({'result':True,'data':'注册成功','error':''}))
    elif request.method == "GET":
        return HttpResponse(json.dumps({'result':False,'data':'','error':'无该请求方式'}))


# 判断请求方式
    # GET
        # 获取用户名和密码
            # 判断用户名和密码是否为空，是否正确
            # 判断是否记住密码
                # 如果记住密码
                    # 存入session,cookie
    # POST
def login_(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        password = make_password(request.GET.get('password',''), None, 'pbkdf2_sha1')
        if (not username) or (not password):
            return HttpResponse(json.dumps({'result':False,'data':'','error':'用户名或密码不能为空'}))
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            print(user)
            login(request,user)
            # 如果用户从非主页或者登录页面进行登录，登录成功之后将会跳转至原页面url
            url = request.COOKIES.get('source_url','')
            return HttpResponse(json.dumps({'result':True,'data':url,'error':''}))
        else:
            return HttpResponse(json.dumps({'result': False, 'data': '', 'error': '用户名或密码错误'}))

    elif request.method == 'GET':
        return HttpResponse(json.dumps({'result': False, 'data': '', 'error': '403'}))


def logout_(request):
    try:
        logout(request)
    except Exception as e:
        logging(e)
    return HttpResponse(json.dumps({'reuslt':True,'data':'logout','error':''}))


def bankbg(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get('name','')
        start_time = request.POST.get('start_time','')
        cardNO = request.POST.get('cardNO','')
        bank = request.POST.get('bank','')
        trapwd = request.POST.get('trapwd','')
        trapwd = make_password(trapwd, None, 'pbkdf2_sha1')
        user = UserInfo.objects.filter(id=user.id)
        try:
            BankCard.objects.create(
                user=user[0].id,name=name,       start_time=start_time,status=0,cardNO=cardNO,bank=bank,trapwd=trapwd
            )
        except ObjectDoesNotExist as e:
            logging(e)
    elif request.method == "get":
        pass

















