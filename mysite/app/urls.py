from django.urls import path, include
from .views import ContactRequestCreateView, ClassImageViewSet, ImgViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'class_image', ClassImageViewSet, basename='class_image-detail'),
router.register(r'img', ImgViewSet, basename='img-list')


urlpatterns = [
    path('', include(router.urls)),
    path('api/contact/', ContactRequestCreateView.as_view(), name='contact-api'),

]