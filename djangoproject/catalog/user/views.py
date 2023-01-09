from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.

def login(request):
    #VERİLERİ ALMA
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #sorgu yapma
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)#sesionid alma
            messages.add_message(request,messages.SUCCESS,'Oturum Açıldı.')
            return redirect('index')
        else:
            messages.add_message(request,messages.ERROR,'Hatalı Kullanıcı adı ve Şifre')
            return redirect('login')
    else:
        return render(request,'user/login.html')

def register(request):
    if request.method == 'POST':

        #form bilgilerini alma
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            #username kontrolu
            if User.objects.filter(username == username).exists():
                messages.add_message(request,messages.WARNING,'Bu kullanıcı adı daha önce alındı')
                return redirect('register')
            else:
                if User.objects.filter(email == email).exists():
                    messages.add_message(request,messages.WARNING,'Bu email daha önce alındı')
                    return redirect('register')
                else:
                    #hersey yi
                    user = User.objects.create_user(username=username,password=password,email=email)
                    user.save()
                    messages.add_message(request,messages.SUCCESS,'Kullanıcı başarılı şekilde')
                    return redirect('login')
        else:
            messages.add_message(request,messages.WARNING,'Şifreniz yanlış')
            return redirect('register')
    
        
    else:
        return render(request,'user/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request,messages.SUCCESS,'Oturum Kapatıldı.')
        return redirect('index')