from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from RuneApp.models import Category, Characteristic, Rune
from RuneApp.serializers import CategorySerializer, CharacteristicSerializer, RuneSerializer

# Create your views here.


@csrf_exempt
def showCategories(request):
    if request.method == 'GET':
        try:
            categories = Category.objects.all()
            categories_serializer = CategorySerializer(categories, many=True)
            return JsonResponse(categories_serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)})


@csrf_exempt
def createCategories(request):
    if request.method == 'POST':
        try:
            category_data = JSONParser().parse(request)
            name = category_data.get('Name')
            if Category.objects.filter(Name=name).exists():
                return JsonResponse({"error": "A category with this name already exists."})
            category_serializer = CategorySerializer(data=category_data)
            if category_serializer.is_valid():
                category_serializer.save()
                return JsonResponse({"message": "Category created successfully!"})
            return JsonResponse({"error": category_serializer.errors})
        except Exception as e:
            return JsonResponse({"error": str(e)})


@csrf_exempt
def editCategory(request):
    if request.method == 'PUT':
        try:
            category_data = JSONParser().parse(request)
            category = Category.objects.get(ID=category_data['ID'])
            new_name = category_data.get('Name')
            if category.Name == new_name:
                return JsonResponse({"error": "The new name is the same as the old one."})
            if Category.objects.filter(Name=new_name).exists():
                return JsonResponse({"error": "A category with this name already exists."})
            category_serializer = CategorySerializer(category, data=category_data)
            if category_serializer.is_valid():
                category_serializer.save()
                return JsonResponse({"message": "Category updated successfully!"})
            return JsonResponse({"error": category_serializer.errors})
        except Exception as e:
            return JsonResponse({"error": str(e)})


@csrf_exempt
def deleteCategory(request, id):
    if request.method == 'DELETE':
        try:
            category = Category.objects.get(ID=id)
            category.delete()
            return JsonResponse({"message": "Category deleted successfully!"})
        except Exception as e:
            return JsonResponse({"error": str(e)})