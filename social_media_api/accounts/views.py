from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserProfileSerializer
)
from rest_framework import generics, permissions, status
from django.shortcuts import get_object_or_404
from .models import User
from .models import CustomUser




class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'message': 'User registered successfully',
            'token': user.auth_token.key
        })


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class ProfileView(APIView):
    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
    
class FollowUserView(generics.GenericAPIView):
permission_classes = [permissions.IsAuthenticated]
queryset = CustomUser.objects.all()

def post(self, request, user_id):
    user_to_follow = get_object_or_404(
        CustomUser.objects.all(), id=user_id
    )

    if user_to_follow == request.user:
        return Response(
            {"detail": "You cannot follow yourself."},
            status=status.HTTP_400_BAD_REQUEST
        )

    request.user.following.add(user_to_follow)
    return Response(
        {"detail": "User followed successfully."},
        status=status.HTTP_200_OK
    )


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(
            CustomUser.objects.all(), id=user_id
        )

        request.user.following.remove(user_to_unfollow)
        return Response(
            {"detail": "User unfollowed successfully."},
            status=status.HTTP_200_OK
        )

