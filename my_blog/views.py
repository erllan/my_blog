from django.shortcuts import render, redirect, HttpResponse
from .models import Blog, User, Comment


def login(request):
    error = ''
    if request.method == 'POST':
        try:
            login = request.POST['email']
            password = request.POST['password']
        except:
            login = None
            password = None
            pass
        if login and password and login != '' and password != '':
            try:
                user = User.objects.get(email=login)
            except:
                user = None
            if user and user.password == password:
                userData = {'email': user.email, 'id': user.id, 'name': user.name}
                request.session['User'] = userData
                return redirect('index')
            error = 'неверный логин или пароль'
        else:
            error = 'Заполните все поля'
    return render(request, 'my_blog/login.html', {'error': error})


def logout(request):
    del request.session['User']
    return redirect('index')


def register(request):
    if request.method == 'POST':
        createUser = User(name=request.POST['name'],
                          email=request.POST['email'],
                          password=request.POST['password'])
        createUser.save()
        userData = {'email': createUser.email, 'id': createUser.id, 'name': createUser.name}
        request.session['User'] = userData
        if createUser:
            return redirect('index')
    return render(request, 'my_blog/register.html')


def index(request):
    blogs = Blog.objects.all().order_by('-date')
    return render(request, 'my_blog/index.html', {'blogs': blogs})


def addBlog(request):
    if request.method == "POST":
        user = request.session['User']
        blog = Blog(user_id=user['id'],
                    Title=request.POST['title'],
                    blog=request.POST['blog'])
        blog.save()
        return redirect('index')
    return render(request, 'my_blog/addblog.html')



def like():
    pass


def blog(request, id_blog):
    blog = Blog.objects.get(id=id_blog)
    try:
        user = User.objects.get(id=request.session['User']['id'])
    except:
        user = False
    if user:
        if request.method == 'POST':
            comment = Comment(comment=request.POST['comment'],
                              user=user,
                              toBlog=blog)
            comment.save()
    return render(request, 'my_blog/blog.html', {'blog': blog})
