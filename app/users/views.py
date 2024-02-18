from django.db import IntegrityError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserRegistrationSerializer
from .services import UserRegistrationService


class UserRegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=UserRegistrationSerializer,
        responses={
            201: '{}',
            400: '{}',
            401: '{}',
        },
        operation_id='Register User And Get Token',
        operation_description='Register User And Get Token',
    )
    def post(self, request: Request) -> Response:
        request_serializer = UserRegistrationSerializer(data=request.data)
        if not request_serializer.is_valid():
            return Response(
                {'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            user_token = UserRegistrationService().create_user_and_get_token(
                user_data=request_serializer.data
            )
            return Response({'token': user_token}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response(
                {'message': 'Possibly email already exists'},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserAuthToken(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=UserRegistrationSerializer,
        responses={
            201: '{}',
            400: '{}',
            401: '{}',
        },
        operation_id='Get Token For User',
        operation_description='Get Token For User',
    )
    def post(self, request: Request) -> Response:
        '''
        Token auth gives for api more speed than Basic auth
        We can do jwt too:)
        '''
        request_serializer = UserRegistrationSerializer(data=request.data)
        if not request_serializer.is_valid():
            return Response(
                {'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST
            )
        user_token = UserRegistrationService().get_auth_token_by_user_data(
            user_data=request_serializer.data
        )
        return Response({'token': user_token}, status=status.HTTP_200_OK)
