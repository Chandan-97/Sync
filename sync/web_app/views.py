from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.


class WebAppView(APIView):
    def perform_authentication(self, request):
        pass

    def get(self, request):
        return render(request, 'website/home.html')
