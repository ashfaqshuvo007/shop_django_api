"""
    Created by tareq on ২৭/৬/১৯
"""
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from sol_factory.users.models import UserVerificationLink

__author__ = "Tareq"


class UserVerificationView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            verification_code = kwargs.get('verification_code', None)
            verified_user = UserVerificationLink.verify_user_via_verification_link(verification_uid=verification_code)
            data = {
                'user_id': verified_user.pk,
                'message': "Verification successful",
                'success': True
            }
            return Response(
                data=data, status=status.HTTP_200_OK, content_type="application/json"
            )
        except Exception as exp:
            data = {
                'message': str(exp), 'success': False
            }
            return Response(
                data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR, content_type="application/json"
            )
