from django.contrib import admin
from Book.models import BookInfo,PeopleInfo
# Register your models here.

class PeopleInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','gender','book']

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name']
# 注册书籍信息模型类

admin.site.register(BookInfo,BookInfoAdmin)

# 注册人物信息模型类
admin.site.register(PeopleInfo,PeopleInfoAdmin)
