# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

# Permissions
from rest_framework.permissions import IsAuthenticated

# Models
from users.models import User

# Serializers
from search.serializers import CurriculumSerializer

# Permissions
from users.permissions import IsRecruiterUser


'''
Para los reclutadores, esta vista extiende sólo el mixin ListModelMixin y
así nos ahorra mucho trabajo.

Utilizaremos un queryset para indicarle que solo queremos los usuarios 
activos y que no sean reclutadores, 

Por último le diremos que la clase serializadora será CurriculumSerializer.
'''
class SearchViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    queryset = User.objects.filter(is_active=True, is_recruiter=False)
    serializer_class = CurriculumSerializer
    filter_backends = (SearchFilter,)
    search_fields = (
        'extract', 
        'city', 
        'country', 
        'experience__company', 
        'experience__description', 
        'education__title', 
        'extra_education__description',
        'projects__description',
    )
    
    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsRecruiterUser]
        return [permission() for permission in permission_classes]