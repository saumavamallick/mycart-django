"""greatkart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from .views import *

app_name = 'store'
urlpatterns = [
    path('', store ,name='store'),
    path('<slug:category_slug>/', store ,name='product_by_category'),
    path('<slug:category_slug>/detail/<slug:product_slug>/', product_detail, name='product_detail'),
    #path('<slug:category_slug>/', product_category, name='product_by_category'),
]
