from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .messages import UsersMessages
from .serializers import UserSerializer


class RegisterView(APIView):
    """ This view is use for the register user details"""
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"message": UsersMessages.USER_REGISTER_SUCCESSFULLY}, status=status.HTTP_201_CREATED)

