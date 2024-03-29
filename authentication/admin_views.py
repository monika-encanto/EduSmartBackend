from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.permissions import IsSuperAdminUser, IsAdminUser, IsManagementUser, IsPayRollManagementUser, \
    IsBoardingUser, IsStaffUser
from authentication.serializers import UserSignupSerializer, UsersListSerializer, UpdateProfileSerializer, \
    UserLoginSerializer, StaffProfileSerializer, StaffUpdateProfileSerializer, StaffSignupSerializer
from pagination import CustomPagination
from utils import create_response_data, create_response_list_data
from django.db import IntegrityError
from rest_framework import status, permissions, response
from rest_framework.exceptions import ValidationError
from authentication.models import User, AddressDetails
from constants import UserLoginMessage, UserResponseMessage
from rest_framework.response import Response


class AdminStaffLoginView(APIView):
    permission_classes = [permissions.AllowAny, ]
    """
    This class is used to login user's.
    """

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            resposne = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=UserLoginMessage.USER_DOES_NOT_EXISTS,
                data={}
            )
            return Response(resposne, status=status.HTTP_400_BAD_REQUEST)
        if not user.check_password(password):
            response = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=UserLoginMessage.INCORRECT_PASSWORD,
                data={}
            )
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        refresh = RefreshToken.for_user(user)
        response_data = create_response_data(
            status=status.HTTP_201_CREATED,
            message=UserLoginMessage.SIGNUP_SUCCESSFUL,
            data={
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id,
                'name': user.name,
                'email': user.email,
                'phone': str(user.phone),
                'is_email_verified': user.is_email_verified
            }
        )
        return Response(response_data, status=status.HTTP_201_CREATED)


class StaffListView(APIView):
    permission_classes = [IsAdminUser, ]

    def get(self, request):
        serializer = StaffProfileSerializer(User.objects.filter(is_staff=True, is_active=True), many=True)
        response_data = create_response_data(
            status=status.HTTP_200_OK,
            message="",
            data=serializer.data
        )
        return Response(response_data, status=status.HTTP_200_OK)


class StaffProfileView(APIView):
    permission_classes = [IsStaffUser, ]

    def get(self, request):
        serializer = StaffProfileSerializer(request.user)
        response_data = create_response_data(
            status=status.HTTP_200_OK,
            message="",
            data=serializer.data
        )
        return Response(response_data, status=status.HTTP_200_OK)


class GetStaffView(APIView):
    permission_classes = [IsStaffUser, ]

    def get(self, request, pk):
        instance = User.objects.get(id=pk)
        if instance.is_staff == False:
            response_data = create_response_data(
                status=status.HTTP_200_OK,
                message=UserLoginMessage.NOT_STAFF_USER,
                data={}
            )
            return Response(response_data, status=status.HTTP_200_OK)
        serializer = StaffProfileSerializer(instance)
        response_data = create_response_data(
            status=status.HTTP_200_OK,
            message=UserResponseMessage.USER_DETAIL_MESSAGE,
            data=serializer.data
        )
        return Response(response_data, status=status.HTTP_200_OK)


class StaffUpdateProfileView(APIView):
    permission_classes = [IsStaffUser, ]

    def patch(self, request, pk):
        user = User.objects.get(id=pk, is_staff=True)
        if not user:
            response_data = create_response_data(
                status=status.HTTP_404_NOT_FOUND,
                message=UserResponseMessage.USER_NOT_FOUND,
                data={}
            )
            return response.Response(response_data, status=status.HTTP_404_NOT_FOUND)

        serializer = StaffUpdateProfileSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response_data = create_response_data(
            status=status.HTTP_200_OK,
            message=UserResponseMessage.PROFILE_UPDATED_SUCCESSFULLY,
            data=StaffProfileSerializer(user).data
        )
        return Response(response_data, status=status.HTTP_200_OK)


class AdminStaffDeleteView(APIView):
    permission_classes = [IsAdminUser, ]

    def delete(self, request, pk):
        user = User.objects.get(id=pk, is_staff=True)
        resp_status = status.HTTP_404_NOT_FOUND
        message = UserResponseMessage.USER_NOT_FOUND
        if user:
            user.is_active = False
            user.save()
            resp_status = status.HTTP_200_OK
            message = UserResponseMessage.USER_DELETE_MESSAGE

        response_data = create_response_data(
            status=resp_status,
            message=message,
            data={}
        )
        return Response(response_data, status=resp_status)


class AdminStaffCreateView(APIView):
    permission_classes = [IsAdminUser, ]

    def post(self, request):
        serializer = StaffSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['name']
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        phone = serializer.validated_data['phone']
        user_type = serializer.validated_data['user_type']
        try:
            user = User.objects.create_admin_user(
                name=name, email=email, password=password, phone=phone, user_type=user_type, is_staff=True
            )
        except IntegrityError:
            response_data = create_response_data(
                status=status.HTTP_400_BAD_REQUEST,
                message=UserLoginMessage.STAFF_ALREADY_EXISTS,
                data={}
            )
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        response_data = create_response_data(
            status=status.HTTP_201_CREATED,
            message=UserLoginMessage.SIGNUP_SUCCESSFUL,
            data={
                'user_id': user.id,
                'name': user.name,
                'email': user.email,
                'phone': str(user.phone),
                'is_email_verified': user.is_email_verified
            }
        )
        return Response(response_data, status=status.HTTP_201_CREATED)
