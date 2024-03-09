from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import Countries
from .serializers import CountriesSerializer
import requests
from rest_framework.response import Response
from rest_framework import status


class CountriesViewset(ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    


    def create(self, request):
        iso2 = request.data.get('iso2','')

        site = f'https://countriesnow.space/api/v0.1/countries/capital'
        data = {"iso2": iso2}



        requisicao = requests.post(site, json=data)

        if requisicao.status_code == 200:
            response_data = requisicao.json()
            # Acessando os dados corretamente da resposta JSON
            data = response_data.get('data', {})
            error = response_data.get('error', False)
            msg = response_data.get('msg', '')
            name = data.get('name', '')
            capital = data.get('capital', '')
            iso3 = data.get('iso3', '')
            
            # Criando ou atualizando uma instância de Countries
            country, created = Countries.objects.update_or_create(
                iso2=iso2,
                defaults={
                    'data': data,
                    'error': error,
                    'msg': msg,
                    'name': name,
                    'capital': capital,
                    'iso3': iso3
                }
            )

            # Retornando a resposta com o serializador
            serializer = self.get_serializer(country)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Erro na solicitação'}, status=requisicao.status_code)