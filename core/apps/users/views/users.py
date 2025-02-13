from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet


from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from ..models import UserModel
from ..serializers.users import CreateUserSerializer, ListUserSerializer, RetrieveUserSerializer



@extend_schema(tags=["user"])
class UserView(BaseViewSetMixin, ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = ListUserSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListUserSerializer,
        "retrieve": RetrieveUserSerializer,
        "create": CreateUserSerializer,
        "update": CreateUserSerializer,  
    }


    def retrieve(self, request, pk=None):
        user = get_object_or_404(UserModel, user_id=pk) 
        serializer = RetrieveUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user = get_object_or_404(UserModel, user_id=pk) 
        serializer = CreateUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)