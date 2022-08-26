from django.urls import path
from registration.views import HomeView


urlpatterns = [
   path('home',HomeView.as_view(),name="HomeView"),
]