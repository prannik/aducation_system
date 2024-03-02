from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_link = models.URLField()


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    min_users = models.PositiveIntegerField()
    max_users = models.PositiveIntegerField()
    users = models.ManyToManyField(User)

    def distribute_users(self):
        while self.users.count() < self.max_users:
            user_to_add = User.objects.exclude(pk__in=self.users.all()).first()
            self.users.add(user_to_add)
        if self.users.count() > self.max_users:
            excess_users_count = self.users.count() - self.max_users
            excess_users = self.users.all()[:excess_users_count]
            self.users.remove(*excess_users)
