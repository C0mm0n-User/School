from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('students', views.students, name='students'),
    path('parents', views.parents, name='parents'),
    path('gallery', views.gallery, name='gallery'),
    path('files', views.files, name='files'),
    path('achievements', views.achievements, name='achievements'),
]
