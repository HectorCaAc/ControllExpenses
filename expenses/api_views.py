from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.renderers import  JSONRenderer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.contrib.auth import get_user_model
User = get_user_model()

from django.db.models import Sum

from account.models import CustomUser
from expenses.models import Category, Entry, Income
from expenses.serializers import CategorySerializer

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
    
    print('*'*10+'Adding Category'+'*'*10)
    user = request.user
    body = request.data
    data = {
        'expense': body['category_amount'],
        'name': body['add_category'],
        'circle_repetition': body['circle_repetition'],
        'user': user.pk
    }
    print('user {} data {}'.format(user, data))
    serializer = CategorySerializer(data= data)
    if serializer.is_valid():
        check_category = Category.objects.filter(user=user, name=data['name'])
        if check_category.exists():
            return Response({'message': 'Duplicate Category'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'message': 'OK'},status=status.HTTP_200_OK)
    else:
        return Response({'message': 'wrong data', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    print(serializer)

@api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def categories(request, username):
    """
        Get all the categories related to certain user
        URL PARAMS
        --------
        category_name = if given to the url then return details for the string, spaces are by +
    """
    user = User.objects.filter(username=username)
    if not user.exists():
            return Response({'message': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
    category_name = request.GET.get('category_name', None)
    if category_name is None:
        query = Category.objects.filter(user=user.first())
        categories = [None]*query.count()
        index = 0
        for categori in query:
            category_object = {}
            category_object['name']= categori.name
            category_object['expense'] = categori.expense
            category_object['spend_available'] = categori.spend_available
            categories[index] = category_object
            index += 1
        print('*'*10+'GET CATEGORY'+'*'*10)
        print('category_request {}'.format(username))
        print(request)
        data = {
            'message': 'request approved',
            'categories': categories
        }
        print(data)
        return Response(data, status=status.HTTP_200_OK)
    else:
        category_name = category_name.replace('+',' ')
        query = Category.objects.filter(user=user.first(), name=category_name)
        if not query.exists():
            return Response({'message': 'Category not found'}, status=status.HTTP_400_BAD_REQUEST)
        category = query.first()
        attributes = {'expense', 'circle_repetition', 'name', 'current_circle', 'deficit', 'spend_available'}
        data = {}
        for attribute in attributes:
            data[attribute] = getattr(category, attribute, None)
        return Response({'message': 'category found', 'data': data})

        return Response({'message': 'category found', 'data': category_name}, status=status.HTTP_200_OK)

@api_view(['GET'])
def category_description(request, username, category_name):
    user = User.objects.filter(username=username)
    print('BACK END GETTING CATEGORY NAME {} FOR USER {}'.format(category_name, username))
    if not user.exists():
        return Response({'message': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
    category = Category.objects.filter(user=user.first(), name=category_name)
    if not category.exists():
        return Response({'message': 'Category not found'}, status=status.HTTP_400_BAD_REQUEST)
    category = category.first()
    attributes = {'expense', 'circle_repetition', 'name', 'current_circle', 'deficit', 'spend_available'}
    data = {}
    for attribute in attributes:
        data[attribute] = getattr(category, attribute, None)

    return Response({'message': 'category found', 'data': data})
