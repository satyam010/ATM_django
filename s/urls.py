"""s URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home1, name='login'),
    url(r'^home/$', views.home2, name='home2'),
    url(r'^viewBalance/$', views.home3, name='home3'),
    url(r'^Deposit/$', views.home4, name='home4'),
    url(r'^processDeposit/$', views.home5, name='home5'),
    url(r'^Withdraw/$', views.home6, name='home6'),
    url(r'^processWithdraw/$', views.home7, name='home7'),
    url(r'^editPassword/$', views.home8, name='home8'),
    url(r'^processPassword/$', views.home9, name='home9'),
    url(r'^mini/$', views.home10, name='home10'),
]

