from django.urls import path
from . import views


urlpatterns=[
    path('details/<int:id>',views.detail, name='detail'),
    path('index',views.index, name= 'index'),
    path('new_url',views., name= 'index'),

]