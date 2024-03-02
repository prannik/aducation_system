from datetime import timezone

from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Group, Lesson, Product
from .serializers import GroupSerializer, LessonSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)

        for product in queryset:
            product.num_lessons = product.lesson_set.count()

        return Response(serializer.data)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def list(self, request):
        queryset = self.get_queryset()
        user = request.user

        if user.is_authenticated:
            queryset = queryset.filter(product__group__users=user)

        serializer = LessonSerializer(queryset, many=True)
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def distribute_users_to_groups(self, request, pk=None):
        group = self.get_object()
        product = group.product

        if product.start_datetime <= timezone.now():
            group.distribute_users()
            return Response({"message": "Users distributed to group successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Product has not started yet."}, status=status.HTTP_400_BAD_REQUEST)

    def product_statistics(self, request):
        return Response({"message": "Product statistics"}, status=status.HTTP_200_OK)

    def user_has_access_to_product(self, request, pk=None):
        group = self.get_object()
        user = request.user
        if group.user_has_access(user):
            return Response({"message": "User has access to product."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "User does not have access to product."}, status=status.HTTP_403_FORBIDDEN)
