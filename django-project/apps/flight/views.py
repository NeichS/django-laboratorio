from django.shortcuts import render

class SearchFlight:
    
    def template(request):
        return render(request, "searchFlight.html")
