from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .messages import CommonMessages
from .models import Event
from .purchase_ticket_service import PurchaseTicketService
from .serializers import UserSerializer, EventDetailsSerializer


class RegisterView(APIView):
    """ This view is use for the register user details"""
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"message": CommonMessages.USER_REGISTER_SUCCESSFULLY}, status=status.HTTP_201_CREATED)


class EventDetailsApiView(ModelViewSet):
    """ This view is used for the  add and view event details"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventDetailsSerializer

    def post(self, request):
        """This method is used for the add event details"""
        if request.user.role != 'Admin':
            return Response({"message": CommonMessages.ONLY_ADMIN_CAN_CREATE_EVENT}, status=status.HTTP_403_FORBIDDEN)

        serializer = EventDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": CommonMessages.DATA_RETRIEVE_SUCCESSFULLY, "data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"], url_path='purchase-ticket')
    def purchase_ticket(self, request, pk=None):
        """ This method is used for the purchase ticket"""
        if request.user.role != 'User':
            return Response({"message": CommonMessages.ONLY_USER_CAN_PURCHASE_TICKET}, status=status.HTTP_403_FORBIDDEN)
        payload = PurchaseTicketService().execute(request, pk)
        return Response({"message": CommonMessages.TICKET_PURCHASE_SUCCESSFULLY.format(ticket=payload)}, status=status.HTTP_201_CREATED)


