from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class MyUser(AbstractUser):
    jifen = models.IntegerField('积分', default=0)

    class Meta:
        db_table = 'MyUser'

    def __str__(self):
        return self.username

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    文章的数据库表稍微复杂一点，主要是涉及的字段更多。
    """
    title=models.CharField(max_length=70)#标题
    author=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    content=models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)#分类

    created_time=models.DateField()#日期
    modify_time=models.DateField()

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True)


    class Meta:
        db_table='article'
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})




class Message(models.Model):
    username=models.CharField(max_length=256)
    body=models.TextField(max_length=256)
    created_time=models.DateTimeField()

    def __str__(self):
        tpl = '<Message:[username={username}, body={body}, created_time={created_time}]>'
        return tpl.format(username=self.username,body=self.body, created_time=self.created_time)