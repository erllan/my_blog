from django.shortcuts import render, redirect, HttpResponse
from .models import Blog, User, Comment


def login(request):
    error = ''
    if request.method == 'POST':
        try:
            login = request.POST['mail']
            password = request.POST['password']
        except:
            login = None
            password = None
            pass
        if login and password and login != '' and password != '':
            try:
                user = User.objects.get(mail=login)
            except:
                user = None
            if user and user.password == password:
                userData = {'mail': user.mail, 'id': user.id, 'name': user.name}
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
                          mail=request.POST['mail'],
                          password=request.POST['password'])
        createUser.save()
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


def blog(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'my_blog/blog.html', {'blog': blog})


def like():
    pass


def comment(request, id_blog):
    blog = Blog.objects.get(id=id_blog)
    user = User.objects.get(id=request.session['User']['id'])
    if request.method == 'POST':
        comment = Comment(comment=request.POST['comment'],
                          user=user,
                          toBlog=blog)
        comment.save()
    return render(request, 'my_blog/comment.html', {'blog': blog})
