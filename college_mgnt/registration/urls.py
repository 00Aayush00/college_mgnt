from django.urls import path
from registration.views import HomeView ,StudentAddView


urlpatterns = [
   path('home',HomeView.as_view(),name="HomeView"),
   path('student/add',StudentAddView.as_view(),name="StudentAddView"),
]