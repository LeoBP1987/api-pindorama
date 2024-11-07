from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from rest_framework import status
from pindorama.models import Tipos
from pindorama.serializers import TiposSerializer

class TiposTestCase(APITestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):
        self.usuario = User.objects.get(username='leonardo')
        self.url = reverse('Tipos-list')
        self.client.force_authenticate(self.usuario)

        self.tipo_01 = Tipos.objects.get(id=1)
        self.tipo_02 = Tipos.objects.get(id=2)

    def test_verifica_requisicao_get_lista_tipos(self):
        'Teste que verifica requisição GET para lista de Tipos'

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verifica_requisicao_get_para_um_tipo(self):
        'Teste que verifica requisição GET para um Tipo'

        response = self.client.get(f'{self.url}{self.tipo_01.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        dados_tipo = self.tipo_01
        dados_serializados = TiposSerializer(dados_tipo).data

        self.assertEqual(response.data, dados_serializados)


    def test_verifica_requisicao_post_um_tipo(self):
        'Teste que verifica requisição POST para um Tipo'

        dados = {
            'tipo':'TesteTipo',
            'descricao':'Teste de descrição Tipo',
            'data_criacao': date.today()
        }        

        response = self.client.post(self.url, data=dados)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_verifica_requisicao_delete_um_tipo(self):
        '''Teste que verifica requisição DELETE para um Tipo'''

        response = self.client.delete(f'{self.url}{self.tipo_02.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_verifica_requisicao_put_um_tipo(self):
        '''Teste que verifica requisição PUT para um Tipo'''

        dados = {
            "tipo": "Nemo.",
            "descricao": "Sequi culpa eligendi sed illum saepe. Aliquid quae molestias. Libero earum vero cumque eligendi error nesciunt.",
            "data_criacao": date.today()
        }

        response = self.client.put(f'{self.url}{self.tipo_01.id}/', data=dados)

        self.assertEqual(response.status_code, status.HTTP_200_OK)