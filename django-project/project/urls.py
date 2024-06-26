"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from apps.map import views
from apps.map.views import index
from apps.landing_page.views import landing
from apps.user.views import User
from apps.flight.views import SearchFlight, FlightQuery

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", landing),
    path("login/", User.login),
    path("map/", index),
    path("searchflight/", SearchFlight.template),
    path("flightquery/", FlightQuery.template)
    
]
