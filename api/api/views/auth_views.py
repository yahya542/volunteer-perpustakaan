from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import register
from .serializers.auth_serializers import RegisterSerializer

@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        queryset = register.objects.all()
        serializer = RegisterSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)