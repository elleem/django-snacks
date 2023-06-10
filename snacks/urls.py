#routes

from django.urls import path

from .views import HomePageView

#named specifically for django
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
