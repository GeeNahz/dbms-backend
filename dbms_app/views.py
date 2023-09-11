# from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer, LogoutSerializer

# Create your views here.

class RegisterView(generics.GenericAPIView):
    """
    Generic view to register any user.
    Needs to be polished to serve our usecase.
    """
    serializer_class = RegisterSerializer
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        
        return Response(user_data, status=status.HTTP_201_CREATED)
    

class LoginAPIView(generics.GenericAPIView):
    """
    View to handle user login.
    """
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    """
    View to handle logout user from session.
    """
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
