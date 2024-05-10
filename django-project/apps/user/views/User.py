from django.shortcuts import render

class User:
    def login(request):
        return render(request, 'login.html')
