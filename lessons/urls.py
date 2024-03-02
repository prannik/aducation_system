from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import GroupViewSet, LessonViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('groups/<int:pk>/distribute/', GroupViewSet.as_view({'post': 'distribute_users_to_groups'}),
         name='group-distribute'),
    path('products/statistics/', GroupViewSet.as_view({'get': 'product_statistics'}), name='product-statistics'),
]

urlpatterns += router.urls
