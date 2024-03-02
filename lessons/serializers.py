from rest_framework import serializers

from .models import Group, Lesson, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'creator', 'name', 'start_datetime', 'cost']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'product', 'title', 'video_link']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'product', 'name', 'min_users', 'max_users', 'users']
