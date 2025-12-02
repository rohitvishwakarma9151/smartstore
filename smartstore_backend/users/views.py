from django.shortcuts import render, Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from .models import User

# Create Amin views here.

def get_token(request):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh' : str(refresh),
        'access' : str(refresh.access_token),
    }

@api_view(['POST'])
def admin_register(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_Valid():
        user = serializer.save(is_Admin=True)
        tokens = get_token(user)
        return Response({"msg":"Admin registered successfully", "tokens":tokens})
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def admin_Login(request):
    username = request.data.get('username')
    passord = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user and user.is_Admin:
        tokens = get_token(user)
        return Response({"msg" : "Admin logged in successfully", "tokens":tokens})
    return Response({"error":"Invalid credentials or not an admin"}, status=401)