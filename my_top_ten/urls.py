"""my_top_ten URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import movie_detail
from .views import signin_view
from .views import signup_view
from .views import reorder_top_ten
from .views import add_to_top_ten
from movies.views import MovieListCreateAPIView





urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', MovieListCreateAPIView.as_view(), name='my_app_view'),
    # path('signup/', signup_view, name='signup'),
    # path('signin/', signin_view, name='signin'),
    path('add_to_top_ten/<int:movie_id>/', add_to_top_ten, name='add_to_top_ten'),
    path('reorder_top_ten/', reorder_top_ten, name='reorder_top_ten'),
     path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),


]
