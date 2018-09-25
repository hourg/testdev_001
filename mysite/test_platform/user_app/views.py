from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#主要代码逻辑


def index(request):

    return render(request, "index.html")

#处理登录请求
def login_action(request):
    if request.method == "GET":
     username = request.GET.get("username","")
     password = request.GET.get("password","")
     if username == "" or password == "":
         return render(request, "index.html",
                       {"error":"请输入用户名和密码"})
     if username=='aaa' and password=='bbb':
         return HttpResponse('{},欢迎！'.format(username))
     if username !='aaa' or password!='bbb':
         return render(request,"index.html",
                       {"error": "用户名或密码错误,请重新输入"})


