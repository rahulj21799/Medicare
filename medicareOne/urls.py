"""Medicare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('administration/',views.aboutadministration,name='administration'),
    path('leadership/',views.aboutleadership,name='leadership'),
    path('iaag/',views.abouthistory,name='history'),
    path('cch/',views.aboutwhymims,name='whymims'),
    path('courses/',views.courses,name='courses'),
    path('faculty/',views.faculty,name='faculty'),
    path('elitest/',views.elitest,name='elitest'),
    path('Description/<int:myid>',views.description,name='Description'),
    path('ati',views.ati,name='ati'),
    ]
