from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Category,
)

from .serializers import (
    CategorySerializer
)

from .utils import JSONListFormatter

# Create your views here.

class CategoryListApiView(APIView):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all().order_by('-id')
        serializer = CategorySerializer(categories, many=True)
        try:
            data = JSONListFormatter("category", serializer.data)
        except:
            data = []

        return Response(data, status=status.HTTP_200_OK)

class CategoryDetailApiView(APIView):

    def get_object(self, category_id):
        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return None

    def get(self, request, category_id, *args, **kwargs):
        '''
            Retrieves the Post with given category_id
        '''
        category_instance = self.get_object(category_id)
        if not category_instance:
            return Response(
                {"response": "Post with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = CategorySerializer(category_instance)
        try:
            data = JSONListFormatter("category", name_obj=serializer.data)
        except:
            data = []
        return Response(data, status=status.HTTP_200_OK)
