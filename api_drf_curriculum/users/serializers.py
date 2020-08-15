"""Users serializers."""

# Django
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator, FileExtensionValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from users.models import User


'''
Un ModelSerializer se usa para poder recuperar los datos de un elemento 
dado un modelo.
'''
class UserModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )


'''
Un Serializer se encarga de realizar la validación de los datos y 
la posterior acción si es necesaria.
'''
class UserLoginSerializer(serializers.Serializer):

    # Campos que vamos a requerir
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    # Primero validamos los datos
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


'''
Serializer para el registro de un usuario.
'''
class UserSignUpSerializer(serializers.Serializer):
    '''validación del email de usuario'''
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    '''validación del campo username del usuario'''
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    '''validación de la contraseña ingresada por el usuario'''
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    '''valicaciones para el nombre del usuario'''
    first_name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=100)

    '''validaciones de formato permitido para la foto del usuario'''
    photo = serializers.ImageField(
        validators=[FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png']
            )], 
        required=False
    )

    '''Expresión regular usada para la validación del número de usuario'''
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Debes introducir un número con el siguiente formato: +999999999. \
                El límite son de 15 dígitos."
    )
    phone = serializers.CharField(validators=[phone_regex], required=False)

    '''Campos extract, city y country con las validaciones típicas'''
    extract = serializers.CharField(max_length=1000, required=False)
    city = serializers.CharField(max_length=250, required=False)
    country = serializers.CharField(max_length=250, required=False)


    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)

        image = None
        if 'photo' in data:
            image = data['photo']

        if image:
            if image.size > (512 * 1024):
                raise serializers.ValidationError(
                    f"La imagen es demasiado grande, el peso máximo permitido es \
                    de 512KB y el tamaño enviado es de {round(image.size / 1024)}KB")

        return data

    def create(self, data):
        '''este dato se elimina ya que no es requerido en el modelo'''
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        return user

    