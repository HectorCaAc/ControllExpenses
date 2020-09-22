from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.renderers import  JSONRenderer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.db.models import Sum

from account.models import CustomUser
from expenses.models import Category, Entry, Income

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def add_entry(request):
    """
        Add spend to certain user
    """
    print('*'*10)
    print('Request received')
    print(request.data)
    return Response({'message': 'OK'},status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def add_income(request):
    """
        Add Income to certain user
    """
    print('*'*10+'Income'+'*'*10)
    print(request.data)
    print(request.user.is_authenticated)
    amount = int(request.data['amount'])
    income_add = Income(user=request.user, description=request.data['description'],
                        amount=amount)
    repetition = request.data.get('repetition', 'off')
    days = int(request.data.get('next-paycheck',0))
    if repetition == 'on' and days > 0:
        income_add.circle_repetition = days
        income_add.repition = True
    income_add.save()
    print('income stored')
    return Response({'message': 'OK'},status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def add_category(request):
    """
        Add new category to certain user
    """
    print('*'*10)
    print('Add Category')
    return Response({'message': 'OK'},status=status.HTTP_200_OK)