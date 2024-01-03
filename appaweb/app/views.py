from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Package,OnlineLearn,Sell,SellOnline,Comment,Order
from django.db.models import Q
from .forms import orderForm,SignUpForm,LoginForm,commentForm
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client
import random

#zarinpal
MERCHANT = '4e55c54a-f70f-11e9-962e-000c295eb8fc'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
 # Toman / Required
description = "خرید آموزش"  # Required
email = 'shivatz71@gmail.com'  # Optional
mobile = '09129487433'  # Optional
 # Important: need to edit for realy server.

def send_request(request,id=None,title=None):
    amount = request.POST['price']
    CallbackURL = 'http://localhost:8000/verify?id='+ id +'&price='+amount+'&title='+title
    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))

def verify(request):
    id=request.GET['id']
    amount=request.GET['price']
    title=request.GET['title']
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'],amount)
        if result.Status == 100:
            name=request.user.username
            sell=Sell(username=name,nameOfmyClass=title)
            sell.save()
            return redirect('appaweb:packageSell',id=id)
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')
def send_request2(request,id=None,title=None,price=None):
    CallbackURL = 'http://localhost:8000/verifyy?id='+id+'&price='+price+'&title='+title
    result = client.service.PaymentRequest(MERCHANT, price, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))

def verify2(request):
    id = request.GET['id']
    amount = request.GET['price']
    title = request.GET['title']
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'],amount)
        if result.Status == 100:
            name=request.user.username
            sell=SellOnline(username=name,nameOfmyClass=title)
            sell.save()
            return redirect('appaweb:rahgiri',id=id)
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')
# Create your views here.

def base(request):
     post = Post.objects.all().order_by('-id')[:6]
     context={'post': post}
     return render(request, 'index.html', context)

def about(request):
    return render(request,'about.html')

def searchposts(request):
    post = Post.objects.all().order_by('-id')
    context = {'post': post}
    return render(request, 'blog.html', context)


def searchposts_check(request):
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')
        if query is not None:
            # search in title and content field of Post table
            lookups = Q(title__icontains=query) | Q(content__icontains=query)
            results = Post.objects.filter(lookups).distinct()
            context = {'results': results,
                       'submitbutton': submitbutton}
            return render(request, 'blog.html', context)

def searchposts_result(request, id=None,title=None):
    post = get_object_or_404(Post, id=id)
    commentBlog = Comment.objects.filter(title=title)
    form=commentForm()
    context = {"post": post,"form":form,'commentBlog':commentBlog}
    return render(request, "searchposts_result.html", context)
def sendCm(request,id=None,title=None):
 form=commentForm()
 post = get_object_or_404(Post, id=id)
 commentBlog = Comment.objects.filter(title=title)
 if request.method == 'POST':
    cm = request.POST['comment']
    comment = Comment(comment=cm, title=title)
    comment.save()
    messages.success(request,'پیام شما ارسال شد')
    redirect('appaweb:searchposts_result', id=id, title=title)
 context = {"post": post,'commentBlog':commentBlog,"form":form}
 return render(request, "searchposts_result.html", context)

def onlinePackage(request):
    package=Package.objects.all()
    context = {'package': package}
    return render(request,'package.html',context)

def packageSell(request,id=None):
    package = Package.objects.filter(id=id)
    sell=Sell.objects.filter(username=request.user.username)
    if sell.count()>0:
        s=1
        context = {"package": package, 'idpack': id,'sell':sell,'s':s}
    else:
         s=0;
         context = {"package": package,'idpack':id,'sell':sell,'s':s}
    return render(request, "packageSell.html", context)

def onlineLearn(request):
    onlinelearn=OnlineLearn.objects.all()
    context = {'package': onlinelearn}
    return render(request,'online.html',context)


def learnSell(request, id=None):
    sell = SellOnline.objects.filter(username=request.user.username)
    onlinelearn = OnlineLearn.objects.filter(id=id)
    if sell.count()>0:
        s=1
        context = {"package": onlinelearn, 'idpack': id,'sell':sell,'s':s}
    else:
     s = 0;
     context = {"package": onlinelearn, 'idpack': id, 's': s}
    return render(request, "onlineSell.html", context)

def rahgiri(request,id=None):
    num=random.randint(1000000,999999999)
    sell = SellOnline.objects.filter(username=request.user.username)
    onlinelearn = OnlineLearn.objects.filter(id=id)
    if sell.count()>0:
        s=1
        context = {"package": onlinelearn, 'idpack': id,'sell':sell,'s':s,'num':num}
    else:
     s = 0;
     context = {"package": onlinelearn, 'idpack': id, 's': s,'num':num}
    return render(request,'rahgiri.html',context)
def order(request):
 if request.method == 'POST':
  form = orderForm(request.POST)
  name= request.POST['name']
  email= request.POST['email']
  phone= request.POST['phone']
  description= request.POST.get('descrip',False)
  order = Order(name=name, email=email,phone=phone,description=description)
  order.save()
  messages.success(request,'پیغام شما ارسال شد')
  return redirect('appaweb:Order')
 else:
  form = orderForm()
  return render(request,'order.html',{'form':form})


 # ==================sign up============
def searchposts(request):
     post = Post.objects.all().order_by('-id')
     if request.method == 'GET':
         query = request.GET.get('q')
         submitbutton = request.GET.get('submit')
         if query is not None:
             lookups = Q(title__icontains=query) | Q(content__icontains=query)
             results = Post.objects.filter(lookups).distinct()
             context = {'results': results,
                        'submitbutton': submitbutton}
             return render(request, 'blog.html', context)
         else:
             context = {'post': post}
             return render(request, 'blog.html', context)

     else:
         context = {'post': post}
         return render(request, 'blog.html', context)



def signup(request):
    form = SignUpForm()
    lform = LoginForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.email = form.cleaned_data.get('email')
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request,'ثبت نام شما با موفقیت انجام شد')
            return redirect('appaweb:Signup')

    else:
     return render(request, 'registration/signup.html', {'form': form, 'lform': lform})
    return render(request, 'registration/signup.html', {'form': form, 'lform': lform})

def Login(request):
 if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user.is_active:
           login(request, user)
           messages.success(request, 'به سایت ما خوش آمدید')
           return redirect('appaweb:Login')
      else:
           messages.error(request,'not login')
           return redirect('appaweb:Login')

 form = SignUpForm()
 lform = LoginForm()
 return render(request, 'registration/signup.html', {'form': form, 'lform': lform})


def signout(request):
    logout(request)
    return redirect('appaweb:base')