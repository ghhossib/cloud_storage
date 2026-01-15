#сериализатор это класс преобразующий данные для api
from django.contrib.auth import authenticate
from django.contrib.messages.api import success
from rest_framework import serializers

class LoginSerilizer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True,write_only=True)

    def validate(self,data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError({
                'success': False,
                'message': {
                    "email": ["field email can not be blank" if not email else ''],
                    "password": ["field password can not be blank" if not password else '']
                }
            })
        #аунтетификация
        user = authenticate(email,password=email)

        if user is None:
            raise serializers.ValidationError(
                {
                    'success': False,
                    'message': "Login failed"
                }
            )
        data['user']
        return data