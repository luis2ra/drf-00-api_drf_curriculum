from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles.models import Plan
from profiles.serializers import PlanSerializer
from profiles.pagination import StandardResultsSetPagination


# Create your views here.
class PlansView(ListAPIView):

    serializer_class = PlanSerializer
    pagination_class = StandardResultsSetPagination


    def get_queryset(self, request):
        queryset = Plan.objects.all()
        return queryset

    def get(self, request):
        queryset = self.get_queryset(request)
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)