from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from events.constant import UserConst
from events.messages import UsersMessages
from events.models import User


class UserSerializer(serializers.ModelSerializer):
    """ This serializer is used for the  user register details"""
    username = serializers.RegexField(
        max_length=150,
        regex=UserConst.USERNAME_REGEX.value,
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all(),
                            message=UsersMessages.ENTITY_ALREADY_EXISTS),
        ],
        error_messages={
            "invalid": UsersMessages.INVALID_USERNAME,
            "required": UsersMessages.ENTITY_REQUIRED_FIELD,
            "max_length": UsersMessages.ENTITY_WITH_MAX_LENGTH_EXCEED.format(max_length=150),
            "blank": UsersMessages.ENTITY_REQUIRED_FIELD,
        }
    )
    password = serializers.RegexField(
        write_only=True,
        required=True,
        max_length=128,
        regex=UserConst.PASSWORD_REGEX.value,
        error_messages={
            "invalid": UsersMessages.INVALID_PASSWORD,
            "required": UsersMessages.ENTITY_REQUIRED_FIELD,
            "blank": UsersMessages.ENTITY_REQUIRED_FIELD,
            "max_length": UsersMessages.ENTITY_WITH_MAX_LENGTH_EXCEED.format(max_length=128),
        })
    role = serializers.ChoiceField(
        required=True,
        choices=User.ROLE_CHOICES,
        error_messages={
            "required": UsersMessages.ENTITY_REQUIRED_FIELD,
        }
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'role', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)