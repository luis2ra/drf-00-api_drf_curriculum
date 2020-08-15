"""Users views."""

# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from users.serializers import (
    UserLoginSerializer, 
    UserModelSerializer,
    UserSignUpSerializer
    )

# Models
from users.models import User


'''
Viewsets
Es un tipo de vista basada en clase que no provee de ningún tipo de método 
como get o post pero que en vez de eso utiliza acciones como list (para listar 
los datos de una tabla) o create (para crear un registro en la tabla).

La clase GenericViewSet se extiende de la clase GenericAPIView.  Ella es una clase 
base en la que nosotros definiremos que métodos vamos a utilizar.
'''
class UserViewSet(viewsets.GenericViewSet):

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)