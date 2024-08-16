from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#importando modelos e serializers
from .models import Professor
from .serializers import ProfessorSerializer

# Create your views here.
class ProfessorView(APIView):

    #define as ações quando recebe um requisicao do tipo post
    def post(self, request):

        #instancia o serialize com os dados recebidos no 'request'
        serializer = ProfessorSerializer(data = request.data)
        if serializer.is_valid():

            #se o formato recebido estiver correto, salva os dados no banco de dados
            serializer.save()

            #retorna com o codigo 201 e os dados do serializer
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        #se o serializer não for valido, retorna erro 400
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
