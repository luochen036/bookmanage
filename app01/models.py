from django.db import models


# 图书管理系统
# book书
# author 作者
# publish 出版社
# author_detail 作者详情
# user 用户

class Books(models.Model):
    title = models.CharField(max_length=50, verbose_name='书名')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='价格')
    publish_date = models.DateField(auto_now_add=True, verbose_name='出版日期')
    # 与出版社建立一对多关系
    publish = models.ForeignKey(related_name='books', to='Publish', on_delete=models.CASCADE, verbose_name='出版社')
    # 与作者建立多对多关系
    authors = models.ManyToManyField(related_name='books', to='Author', verbose_name='作者')


class Author(models.Model):
    name = models.CharField(max_length=25, verbose_name='作者名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(verbose_name='邮箱')
    # 与作者详情建立一对一关系
    detail = models.OneToOneField(related_name='author', to='AuthorDetail', on_delete=models.CASCADE, verbose_name='作者详情')


class Publish(models.Model):
    name = models.CharField(max_length=50, verbose_name='出版社名')
    address = models.CharField(max_length=50, verbose_name='出版社地址')


class AuthorDetail(models.Model):
    phone = models.CharField(max_length=25, verbose_name='电话')
    address = models.CharField(max_length=50, verbose_name='地址')


class User(models.Model):
    username = models.CharField(max_length=25, verbose_name='用户名')
    password = models.CharField(max_length=25, verbose_name='密码')
