from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import  JSONRenderer
from expenses.models import Category

@api_view(['POST'])
def delete_category(request):
    print('delete_category')
    id_category = request.data.get('id_category')
    category_to_delete = Category.objects.get(id=id_category)
    if category_to_delete.user == request.user:
        message = {"message":"The category [{}] can be delete".format(id_category)}
        json = JSONRenderer().render(message)
        return Response({"data":json}, status=status.HTTP_200_OK)
    else:
        message = "The category can not be delete"
        print(message)
        return Response({"message":message}, status=status.HTTP_403_FORBIDDEN)
