"""
    Created by tareq on ২৮/৬/১৯
"""
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

__author__ = "Tareq"


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            response = {
                "token": str(token),
                "user": user.pk,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "user_type": user.user_type,
                "profile_info": user.profile_info_id,
                "verification_status": user.verification_status,
                "success": True
            }
            return Response(
                data=response, status=status.HTTP_200_OK, content_type="application/json"
            )
        else:
            response = {
                "success": False
            }
            return Response(
                data=response, status=status.HTTP_400_BAD_REQUEST, content_type="application/json"
            )
