from django.db import models

# Create your models here.
#  使用ORM框架，创建数据库，对象映射成表。
class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        "以字符串的形式输出模型类"
        return self.name


class PeopleInfo(models.Model):

    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
