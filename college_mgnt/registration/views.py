from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class HomeView(View):
    def get(self, request):
       
        return render(request, "index.html")

# Create your views here.
class StudentAddView(View):
    def get(self, request):
       
        return render(request, "registration/student_add.html")
