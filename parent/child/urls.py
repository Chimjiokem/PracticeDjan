from . import views
from django.urls import path
app_name = 'child'
urlpatterns = [
    path('',views.index,name='index'),
]
