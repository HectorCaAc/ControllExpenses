from rest_framework import serializers

from expenses.models import Category

"""
    If possible start to add the serializers for all the others categories
"""

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['expense', 'circle_repetition', 'name', 'user']
