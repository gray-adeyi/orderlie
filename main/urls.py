from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('register/class/', views.RegisterClass.as_view(), name='create-class'),
    path('register/student/', views.RegisterStudent.as_view(), name='create-student'),
    path('class/<slug:slug>/', views.ClassInfo.as_view(), name='class-info'),
    path('classes/', views.ClassList.as_view(), name='class-list'),
    path('downloads/class-data/<slug:slug>/', views.download_class_data, name='download-data'),
]
