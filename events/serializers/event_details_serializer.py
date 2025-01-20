from django.utils import timezone
from rest_framework import serializers

from events.constant import UserConst
from events.messages import CommonMessages
from events.models import Event


class EventDetailsSerializer(serializers.ModelSerializer):
    """ This serializer is used for the add events details """
    name = serializers.CharField(
        max_length=128,
        required=True,
        error_messages={
            "required": CommonMessages.ENTITY_REQUIRED_FIELD,
            "max_length": CommonMessages.ENTITY_WITH_MAX_LENGTH_EXCEED.format(max_length=150)
        }
    )
    date = serializers.DateTimeField(
        format=UserConst.DATE_AND_TIME_FORMAT.value,
        input_formats=[UserConst.DATE_AND_TIME_FORMAT.value],
        required=True,
        error_messages={
            "required": CommonMessages.ENTITY_REQUIRED_FIELD,
            "null": CommonMessages.ENTITY_REQUIRED_FIELD,
        }
    )
    total_tickets = serializers.IntegerField(
        required=True,
        error_messages={
            "required": CommonMessages.ENTITY_REQUIRED_FIELD,
            "null": CommonMessages.ENTITY_REQUIRED_FIELD,
        }
    )
    tickets_sold = serializers.IntegerField(
        required=True,
        error_messages={
            "required": CommonMessages.ENTITY_REQUIRED_FIELD,
            "null": CommonMessages.ENTITY_REQUIRED_FIELD,
        }
    )

    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'total_tickets', 'tickets_sold')

    def validate_date(self, attrs):
        if attrs.date() <= timezone.now().date():
            raise serializers.ValidationError(CommonMessages.PAST_DATE_NOT_ALLOWED)
        return attrs
