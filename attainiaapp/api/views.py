# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from . import models
from . import serializers

# originally had a separate viewset for each of all users, inactive, and dormant
# but having a queryset made more sense

# class UserViewset(viewsets.ModelViewSet):
#   queryset = models.User.objects.all()
#   serializer_class = serializers.UserSerializer


class UserList(generics.ListAPIView):
  # queryset = models.User.objects.all()
  serializer_class = serializers.UserSerializer

  def get_queryset(self):
    queryset = models.User.objects.all()
    status = self.request.query_params.get('status', None)
    if status is not None:
      if (status=="active"):
        queryset = queryset.filter(login_count__gte=1)
      elif (status=="dormant"): 
        queryset = queryset.filter(login_count__lt=1)
      else:
        return queryset.none()
    return queryset
