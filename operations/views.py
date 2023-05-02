import random
import re
import requests
import urllib.parse
import math

from django.shortcuts import get_object_or_404

from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import permissions, status

from operations.serializers import OperationSerializer
from operations.models import Operation
from records.models import Record
from users.models import User

# Create your views here.


class OperationViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


@api_view(['POST'])
def random_generate(request):
    # Generate a random op_type (addition, subtraction, multiplication, division, square_root, random_string)
    op_type = random.choice(
        ['addition', 'subtraction', 'multiplication', 'division', 'square_root', 'random_string'])

    if op_type == 'addition' or op_type == 'subtraction' or op_type == 'multiplication' or op_type == 'division':
        cost = 1
    elif op_type == 'square_root':
        cost = 5
    elif op_type == 'random_string':
        cost = 10
    else:
        cost = 100

    operation = Operation.objects.create(cost=cost, op_type=op_type)

    return Response({
        "message": "Operation created successfully",
        "url": f"http://localhost:8000/v1/operations/{operation.id}/",
        "operation": {
            "id": operation.id,
            "cost": operation.cost,
            "op_type": operation.op_type,
        }
    })


class Calculate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        operator_pattern = r'[+\-*/]|sqrt\('
        operator_dict = {
            "+": {
                "name": "addition",
                "cost": 1
            },
            "-": {
                "name": "subtraction",
                "cost": 1
            },
            "*": {
                "name": "multiplication",
                "cost": 2
            },
            "/": {
                "name": "division",
                "cost": 2
            },
            "sqrt(": {
                "name": "square_root",
                "cost": 5
            }
        }

        try:
            username = request.user
            user = get_object_or_404(User, username=username)
        except:
            return Response(
                data={
                    "message": "User does not exist"
                },
                status=status.HTTP_404_NOT_FOUND
            )


        equation = request.data.get('equation')
        
        equation = urllib.parse.unquote(equation)

        if equation is None:
            return Response(
                data={
                    "message": "Equation is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Find the operator in a string using regex

        match = re.search(operator_pattern, equation)

        if not match:
            return Response({
                "message": "Invalid equation"
            })

        operator = match.group()
        op_type = operator_dict[operator]["name"]
        cost = operator_dict[operator]["cost"]

        operation = Operation.objects.create(
            op_type=op_type,
            cost=cost,
        )
        
        # Replace sqrt with math.sqrt
        equation = equation.replace("sqrt", "math.sqrt")

        result = eval(equation)
        
    
        user.balance -= cost
        user.save()

        Record.objects.create(
            operation=operation,
            user=user,
            amount=cost,
            user_balance=user.balance,
            operation_response="Success"
        )

        print(f'result: {result} user.balance: {user.balance}')

        return Response({
            "result": result,
            "balance": user.balance,
        }, status=status.HTTP_201_CREATED)


class GetRandomString(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    def get(self, request):
        url = 'https://www.random.org/strings/?num=1&len=8&digits=on&upperalpha=on&loweralpha=on&unique=on&format=plain&rnd=new'
        response = requests.get(url)
        random_string = response.text[:-2]
        return Response(random_string)
