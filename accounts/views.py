from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login, logout, get_user_model



User = get_user_model()

def register_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not username or not email or not password1:
            return render(request, 'accounts/register.html', {'error':'All fields are necessary.'})

        if password1!=password2:
            return render(request, 'accounts/register.html', {'error':'Passwords do not match.'})
        elif User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error':'Username already exists.'})
        elif User.objects.filter(email=email).exists():
            return render(request, 'accounts/register.html', {'error':'Email already exists.'})

        User.objects.create_user(
            username=username,
            email=email,
            password=password2,
        )
        return redirect('login')
            
    return render(request, 'accounts/register.html')






def login_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')    

        user = authenticate(request, username=username, password=password)

        if not user:
            return render(request, 'accounts/login.html', {'error':'Username or password is not correct.'})

        login(request, user=user) 
        return redirect('products')
     
    return render(request, 'accounts/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')

