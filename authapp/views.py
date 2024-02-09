from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else:
            messages.info(request,'invalid')
            return render(request, 'login.html', {'error': 'username or password incorrect'})
    else:
        messages.info(request, 'something went wrong')
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'username is alredy taken')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is alredy taken')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=user_name, email=email, password=password1,first_name=first_name,last_name=last_name)
                user.save()
                print('user created welcome')
                messages.info(request, 'user created...welcome')


            return render(request, 'login.html')
        else:
            messages.info(request, 'user not created')
            return render(request, 'register.html')

    else:
        return render(request, 'register.html')
   


def logout(request):
    auth.logout(request)
    return redirect("/")
