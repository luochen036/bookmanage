from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from app01.models import Books, Publish, Author, User, AuthorDetail
import json


# 首页
class Index(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        pass


# 图书管理
class Book(View):
    def get(self, request):
        books = Books.objects.all()
        return render(request, 'book_list.html', locals())

    def post(self, request):
        pass


# 图书编辑
class EditBook(View):
    def get(self, request, id):
        book = Books.objects.filter(id=id).first()
        authors = Author.objects.all()
        publishes = Publish.objects.all()
        return render(request, 'edit_book.html', locals())

    def post(self, request, id):
        title = request.POST.get('title')
        price = request.POST.get('price')
        author = request.POST.getlist('author')
        publish = request.POST.get('publish')
        publish_date = request.POST.get('publish_date')
        if not all([title, price, author, publish, publish_date]):
            error = '所填信息不能为空！'
            book = Books.objects.filter(id=id).first()
            authors = Author.objects.all()
            publishes = Publish.objects.all()
            return render(request, 'edit_book.html', locals())
        if float(price) > 1000:
            error = '价格不能超过1000！'
            book = Books.objects.filter(id=id).first()
            authors = Author.objects.all()
            publishes = Publish.objects.all()
            return render(request, 'edit_book.html', locals())
        book = Books.objects.filter(id=id).first()
        book.title = title
        book.price = price
        book.publish_date = publish_date
        book.publish_id = publish
        for i in author:
            book.authors.add(i)
        book.save()
        return redirect('manage')


# 图书添加
class Addbook(View):
    def get(self, request):
        authors = Author.objects.all()
        publishes = Publish.objects.all()
        return render(request, 'add_book.html', locals())

    def post(self, request):
        title = request.POST.get('title')
        price = request.POST.get('price')
        author = request.POST.getlist('author')
        publish = request.POST.get('publish')
        publish_date = request.POST.get('publish_date')
        print(type(price))
        if not all([title, price, author, publish]):
            error = '所填信息不能为空！'
            authors = Author.objects.all()
            publishes = Publish.objects.all()
            return render(request, 'add_book.html', locals())

        if Books.objects.filter(title=title).exists():
            error = '图书已存在！'
            authors = Author.objects.all()
            publishes = Publish.objects.all()
            return render(request, 'add_book.html', locals())

        if float(price) > 1000:
            error = '价格不能超过1000！'
            authors = Author.objects.all()
            publishes = Publish.objects.all()
            return render(request, 'add_book.html', locals())

        book = Books()
        book.title = title
        book.price = price
        book.publish_date = publish_date
        book.publish_id = publish
        book.save()
        book = Books.objects.filter(title=title).first()
        book.authors.add(*author)
        return redirect('manage')


# 删除图书
class Deletebook(View):
    def get(self, request):
        pass;

    def post(self, request):
        book_id = request.POST.get('book_id')
        book = Books.objects.filter(id=book_id).first()
        book.delete()
        data = {
            'book_id': book_id,
            'code': 200,
            'msg': '删除成功'
        }
        return JsonResponse(data)


# 出版社管理
class Publishmanage(View):
    def get(self, request):
        publishes = Publish.objects.all()
        return render(request, 'publish_list.html', locals())

    def post(self, request):
        pass


# 出版社添加
class Addpublish(View):
    def get(self, request):
        return render(request, 'add_publish.html')

    def post(self, request):
        name = request.POST.get('name')
        address = request.POST.get('address')
        if not all([name, address]):
            error = '所填信息不能为空！'
            return render(request, 'add_publish.html', locals())
        if Publish.objects.filter(name=name).exists():
            error = '出版社已存在！'
            return render(request, 'add_publish.html', locals())

        publish = Publish()
        publish.name = name
        publish.address = address
        publish.save()
        return redirect('publish')


# 出版社编辑
class Editpublish(View):
    def get(self, request, id):
        publish = Publish.objects.filter(id=id).first()
        return render(request, 'edit_publish.html', locals())

    def post(self, request, id):
        name = request.POST.get('name')
        address = request.POST.get('address')
        if not all([name, address]):
            error = '所填信息不能为空！'
            publish = Publish.objects.filter(id=id).first()
            return render(request, 'edit_publish.html', locals())
        publish = Publish.objects.filter(id=id).first()
        publish.name = name
        publish.address = address
        publish.save()
        return redirect('publish')


# 删除出版社
class Deletepublish(View):
    def get(self, request):
        pass;

    def post(self, request):
        publish_id = request.POST.get('publish_id')
        publish = Publish.objects.filter(id=publish_id).first()
        publish.delete()
        data = {
            'publish_id': publish_id,
            'code': 200,
            'msg': '删除成功'
        }
        return JsonResponse(data)


# 作者管理
class Authormanage(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'author_list.html', locals())

    def post(self, request):
        pass


# 作者添加
class Addauthor(View):
    def get(self, request):
        return render(request, 'add_author.html')

    def post(self, request):
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        if not all([name, age, email, phone, address]):
            error = '所填信息不能为空！'
            authors = Author.objects.all()
            return render(request, 'add_author.html', locals())

        if User.objects.filter(name=name).exists():
            error = '作者已存在！'
            authors = Author.objects.all()
            return render(request, 'add_author.html', locals())

        if int(age) < 0 or int(age) > 120:
            error = '年龄必须在0-120岁之间！'
            authors = Author.objects.all()
            return render(request, 'add_author.html', locals())

        detail = AuthorDetail.objects.create(
            phone=phone,
            address=address,
        )
        author = Author.objects.create(
            name=name,
            age=age,
            email=email,
            detail=detail,
        )
        return redirect('author')


# 作者编辑
class Editauthor(View):
    def get(self, request, id):
        author = Author.objects.filter(id=id).first()
        return render(request, 'edit_author.html', locals())

    def post(self, request, id):
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        if not all([name, age, email, phone, address]):
            error = '所填信息不能为空！'
            author = Author.objects.filter(id=id).first()
            return render(request, 'edit_author.html', locals())

        if int(age) < 0 or int(age) > 120:
            error = '年龄必须在0-120岁之间！'
            author = Author.objects.filter(id=id).first()
            return render(request, 'edit_author.html', locals())

        detail = AuthorDetail.objects.filter(id=id).first()
        detail.phone = phone
        detail.address = address
        detail.save()
        author = Author.objects.filter(id=id).first()
        author.name = name
        author.age = age
        author.email = email
        author.save()
        return redirect('author')


# 删除作者
class Deleteauthor(View):
    def get(self, request):
        pass;

    def post(self, request):
        author_id = request.POST.get('author_id')
        author = Author.objects.filter(id=author_id).first()
        author.delete()
        data = {
            'author_id': author_id,
            'code': 200,
            'msg': '删除成功'
        }
        return JsonResponse(data)


# 登录
class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            error = '用户名或密码不能为空！'
            return render(request, 'login.html', locals())
        flag = User.objects.filter(username=username).exists()
        flag1 = User.objects.filter(username=username, password=password).exists()
        if not flag:
            error = '该用户名未注册！'
            return render(request, 'login.html', locals())

        if flag1:
            return render(request, 'index.html')
        else:
            error = '用户名与密码不匹配！'
            return render(request, 'login.html', locals())


# 注册
class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        if not all([username, password, repassword]):
            error = '所填信息不能为空！'
            return render(request, 'register.html', locals())
        if password != repassword:
            error = '两次输入密码不一致！'
            return render(request, 'register.html', locals())

        flag = User.objects.filter(username=username).exists()
        if flag:
            error = '该用户名已被注册！'
            return render(request, 'register.html', locals())

        user = User()
        user.username = username
        user.password = password
        user.save()
        return render(request, 'login.html')
