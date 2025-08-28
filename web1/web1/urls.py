from django.contrib import admin
from django.urls import path
from core import views 

urlpatterns = [
    path('',views.home,name="home"),
    path('gallery/',views.gallery,name="gallery"),
    path('whyplay/',views.whyplay,name="whyplay"),
    path('admin/', admin.site.urls),
]
