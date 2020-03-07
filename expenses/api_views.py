from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import  JSONRenderer

from django.db.models import Sum

from account.models import CustomUser
from expenses.models import Category, Entry

@api_view(['POST'])
def delete_category(request):
    print('delete_category')
    id_category = request.data.get('id_category')
    category_to_delete = Category.objects.get(id=id_category)
    if category_to_delete.user == request.user:
        category_to_delete.delete()
        message = {"message":"The category [{}] can be delete".format(id_category)}
        json = JSONRenderer().render(message)
        return Response({"data":json}, status=status.HTTP_200_OK)
    else:
        message = "The category can not be delete"
        print(message)
        return Response({"message":message}, status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
def delete_entries(request):
    data = request.data['expenses_id']
    entries = Entry.objects.filter(id__in=data)
    total = entries.aggregate(Sum('price'))
    print(entries)
    print(total)
    entries.delete()
    user = CustomUser.objects.get(user=request.user)
    user.current_balance += total['price__sum']
    user.save()
    message ="Entries delete"
    return Response({"message":message}, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_entry(request):
    print('THE ADD ENTRY API IS NOT DONE YET, IT WILL BE DONE WHEN REACT IS ADDED TO THE PROGRAM OTHER WISE IS A WASE OF TIME')