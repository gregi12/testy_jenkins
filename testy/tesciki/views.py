from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def add_numbers(request):
    try:
        num1 = request.data['num1']
        num2 = request.data['num2']
        result = int(num1) + int(num2)
        return Response({'result': result}, status=status.HTTP_200_OK)
    except ValueError:
        return Response({'error': 'Invalid input. Please provide valid numbers.'}, status=status.HTTP_400_BAD_REQUEST)