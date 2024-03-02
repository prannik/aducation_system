from django.contrib import admin

from .models import Group, Lesson, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creator', 'start_datetime', 'cost')
    list_filter = ('creator', 'start_datetime')
    search_fields = ('name', 'creator__username')
    date_hierarchy = 'start_datetime'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'product', 'video_link')
    list_filter = ('product',)
    search_fields = ('title', 'product__name')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'min_users', 'max_users')
    list_filter = ('product',)
    search_fields = ('name', 'product__name')
