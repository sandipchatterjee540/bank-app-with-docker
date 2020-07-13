from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from .models import CreateAcount

# Create your views here.
def createac(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        mobile=request.POST.get('mobile')
        money=request.POST.get('money')
        sax=request.POST.get('sax')
        date=datetime.now()
        check=CreateAcount.objects.filter(username=username)

        if username and password and password1 and mobile and money and sax:
            if password==password1:
                if check:
                    print("this account alredy exist")
                else:
                    ca=CreateAcount(username=username,password=password,mobile=mobile,money=money,sax=sax,date=date)
                    ca.save()
                    return render(request, "login.html")

            else:
                print("password can not match")
        else:
            print("fill up the from carefully all information are required")
                


        print(username,password,password1,mobile,money,sax,date)
    
    
    return render(request, "create_account.html")

def login(request):
    i=0
    if request.COOKIES.get('username'):
        i=i+1
        response= redirect("home")
        return response

    elif request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username and password:
            userdb=CreateAcount.objects.filter(username=username,password=password)
            if userdb:
                i=0
                response= redirect("home")
                response.set_cookie(key="username", value=username)
                response.set_cookie(key="date", value=datetime.now())
                response.set_cookie(key="id", value=i)
                return response
            else:
                return render(request, "login.html")


    return render(request, "login.html")


def home(request):
    if request.COOKIES.get('username') and request.COOKIES.get('id'):
        if request.method=="GET":
            withdraw=request.GET.get('withdraw')
            check=request.GET.get('check')
            deposite=request.GET.get('deposite')
            reset=request.GET.get('reset')
            logout=request.GET.get('logout')

            if withdraw=="true":
                return redirect("withdraw")

            if deposite=="true":
                return redirect("deposite")

            if check=="true":
                return redirect("sucess")

            if logout=="true":
                response=redirect("login")
                response.delete_cookie('username')
                response.delete_cookie('id')
                response.delete_cookie('date')
                return response

            if reset=="true":
                return redirect("reset")

        userdb=CreateAcount.objects.get(username=request.COOKIES.get('username'))
        return render(request,'home.html',{'user': userdb.username})

    return redirect('login')


def deposite(request):
    if request.COOKIES.get('username') and request.COOKIES.get('id'):
        if request.method=="POST":
            money=request.POST.get("deposite")
            password=request.POST.get('password')
            print(money)
            try:
                userdata=CreateAcount.objects.get(username=request.COOKIES.get('username'), password=password)
                print(userdata)
                if userdata:
                    print(userdata.money)
                    userdata.money=int(userdata.money)+int(money)
                    balance=userdata.money
                    userdata.save()
                    return redirect("sucess")
            except:
                return render(request, "erroe.html",{'status':"Password is not correct"})
        else:
            return render(request, "deposite.html")


    return redirect('login')
    


def withdraw(request):
    if request.COOKIES.get('username') and request.COOKIES.get('id'):
        if request.method=="POST":
            money=request.POST.get('withdraw')
            password=request.POST.get('password')
            try:
                userdata=CreateAcount.objects.get(username=request.COOKIES.get('username'), password=password)
            except:
                return render(request, "error.html",{'status':"Password is not correct"})
            if userdata:
                    balance=userdata.money
                    if int(money)<int(balance):
                        userdata.money=int(balance)-int(money)
                        userdata.save()
                        return redirect("sucess")
                    else:
                        return render(request, "error.html",{'status':"Balance is less then Withdraw"})
            # else:
            #     return render(request, "error.html",{'status':"Password is not correct"})
        else:
            return render(request, "withdraw.html")
    
    return redirect('login')


def sucess(request):
    if request.COOKIES.get('username') and request.COOKIES.get('id'):
        userdata=CreateAcount.objects.get(username=request.COOKIES.get('username'))
        return render(request, "sucess.html", {'balance':userdata.money})
    else:
        return redirect('login')



def reset(request):
    if request.COOKIES.get('username') and request.COOKIES.get('id'):
        if request.method=="POST":
            old_password=request.POST.get('old_password')
            new_password=request.POST.get('new_password')
            new1_password=request.POST.get('new1_password')

            try:
                db=CreateAcount.objects.get(username=request.COOKIES.get('username'), password=old_password)
                if db:
                    if new_password == new1_password:
                        db.password=new_password
                        db.save()
                        response = redirect("login")
                        response.delete_cookie('username')
                        response.delete_cookie('id')
                        response.delete_cookie('date')
                        return response
                    else:
                        return render(request, "error.html",{'status':"Password is not same"})
            except:
                return render(request, "error.html",{'status':"Old password is not currect"})


        return render(request, "reset_pass.html")
    return redirect('login')
    

            
