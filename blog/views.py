
#from django.template import RequestContext
# Create your views here.
from django.http import HttpResponseRedirect
import datetime
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
import datetime
from django.contrib.auth import authenticate,login,logout
from blog.forms import SignupForm,MessageForm
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
from blog.models import models
from . import models
from .models import Article, Category
from comments.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
import markdown

def home(request):
    now=datetime.datetime.now()

    #教程里用的是context_instance报错
    return render(request,'index.html',locals())
    #locals()会渲染函数中定义的所有变量

def message(request):
    messages=models.Message.objects.all()
    return render(request,'message.html',{'messages':messages})

def save(request):
    username = request.POST.get("username")
    body = request.POST.get("body")
    created_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = models.Message(body=body, username=username, created_time=created_time)
    message.save()

    return HttpResponseRedirect('/message.html')

def signup(request):
	path=request.get_full_path()
	if request.method=='POST':
		form=SignupForm(data=request.POST,auto_id="%s")

		if form.is_valid():

			UserModel=get_user_model()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user=UserModel.objects.create_user(username=username,password=password)
			user.save()
			auth_user = authenticate(username=username,password=password)
			login(request,auth_user)

			return redirect("/")
	else:
		form=SignupForm(auto_id="%s")
	return render(request,'signup.html',locals())


'''
实际上登陆界面采用django自带，故不必再写
def login_view(request):
    if request.method=='POST':
        print('1')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print('2')
        if user is not None:
            if user.is_active:
                login(request, user)
                print('3')
                return redirect("/")
            else:
                return render(request, 'login.html', {'status': 'ERROR Incorrect username or password'})

    return render(request, '/login')
'''


def logout_view(request):
	logout(request)
	return redirect('home')

def myblog(request):
	article_list=Article.objects.all().order_by('-created_time')
	return render(request,'myblog.html',context={'article_list':article_list})
'''
class MyblogView(ListView):
    model = Article
    template_name = 'myblog.html'
    context_object_name = 'article_list'
    # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 2

def listing(request):
    contact_list = Article.objects.all()
    paginator = Paginator(contact_list, 2) # 每页显示 2 个联系人

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'myblog.html', {'contacts': contacts})
'''
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.content = markdown.markdown(article.content,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    # 获取这篇 article 下的全部评论
    comment_list = article.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'article': article,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'detail.html', context=context)

def archives(request, year, month):
    article_list = Article.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'myblog.html', context={'article_list': article_list})

def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'myblog.html', context={'article_list': article_list})

