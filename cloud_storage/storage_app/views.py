from django.shortcuts import render
from rest_framework import views
from rest_framework.permissions import AllowAny


# Create your views here.

class LoginView(views.APIView):
    permission_classes = [AllowAny]