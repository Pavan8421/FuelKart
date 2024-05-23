from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from .models import *
from .serializers import OrderSerializer

# Create your views here.

class OrderCreate(CreateAPIView):
  queryset = Orders.objects.all()
  serializer_class = OrderSerializer
  def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            
            # Custom response data
            response_data = {
                "message": "Data inserted successfully",
                "status": "True",
                "data": serializer.data
            }
            
            return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
        except ValidationError as e:
            return Response({"message": "Data not inserted due to invalid data","status":"False"}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"message": "Data not inserted","status":"False"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class OrderView(ListAPIView):
  queryset = Orders.objects.all()
  serializer_class = OrderSerializer