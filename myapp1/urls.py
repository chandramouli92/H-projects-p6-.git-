from django.urls import path
from myapp1 import views
app_name="myapp1"

urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('child/',views.child,name="child"),
    path('base',views.base,name="base"),
]
