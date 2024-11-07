from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from pindorama.models import Origens
from pindorama.serializers import OrigensSerializer

class OrigensTestCase(APITestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):

        self.usuario = User.objects.get(username='leonardo')
        self.url = reverse('Origens-list')
        self.client.force_authenticate(self.usuario)

        self.origem_01 = Origens.objects.get(id=3)
        self.origem_02 = Origens.objects.get(id=7)

    def test_verifica_requisicao_get_lista_origens(self):
        'Teste que verifica requisição GET para lista de Origens'

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verifica_requisicao_get_para_um_origens(self):
        'Teste que verifica requisição GET para um Origem'

        response = self.client.get(f'{self.url}{self.origem_01.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        dados_origem = self.origem_01
        dados_serializados = OrigensSerializer(dados_origem).data

        self.assertEqual(response.data, dados_serializados)


    def test_verifica_requisicao_post_um_origem(self):
        'Teste que verifica requisição POST para uma Origem'

        dados = {
            "origem": "TesTeOrigem",
            "descricao": "TesteOrigem",
            "data_criacao": date.today()
        }        

        response = self.client.post(self.url, data=dados)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_verifica_requisicao_delete_um_origens(self):
        '''Teste que verifica requisição DELETE para um Origem'''

        response = self.client.delete(f'{self.url}{self.origem_02.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_verifica_requisicao_put_um_origens(self):
        '''Teste que verifica requisição PUT para um Origem'''

        dados = {
            "origem": "Natus accusantium.",
            "descricao": "Quasi unde soluta earum fuga. Architecto atque voluptate architecto quidem nesciunt sed. Totam veniam dicta.",
            "data_criacao": date.today()
        }

        response = self.client.put(f'{self.url}{self.origem_01.id}/', data=dados)

        self.assertEqual(response.status_code, status.HTTP_200_OK)