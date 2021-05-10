"""meeting_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from website.views import welcome
from website.views import date
from website.views import about
from meetings.views import detail

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('welcome.html', welcome),
   # path('', welcome), # '' makes it starting page , first is url, second is view function
    path('date',date),
    path('about', about),
   # path('meetings/<int:id>',detail)
   # path('meetings/<int:id>', detail, name='detail'),   # name is for {% url 'detail' meeting.id %}
    path('adddifferentthingsstillworks/meetings/<int:id>', detail, name='detail'),
    path('', welcome, name='welcome'),
]
