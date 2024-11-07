from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date
from pindorama.models import LendasCriaturas
from pindorama.serializers import LendasCriaturasSerializer

class LendasCriaturasTestCase(APITestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):

        self.usuario = User.objects.get(username='leonardo')
        self.url = reverse('Lendas-list')
        self.client.force_authenticate(self.usuario)

        self.lenda_01 = LendasCriaturas.objects.get(id=5)
        self.lenda_02 = LendasCriaturas.objects.get(id=7)


    def test_verifica_requisicao_get_lista_lendas(self):
        'Teste que verifica requisição GET para lista de Lendas'

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verifica_requisicao_get_para_um_lenda(self):
        'Teste que verifica requisição GET para um Lenda'

        response = self.client.get(f'{self.url}{self.lenda_01.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        dados_lenda = self.lenda_01
        dados_serializados = LendasCriaturasSerializer(dados_lenda).data

        self.assertEqual(response.data['id'], dados_serializados['id'])
        self.assertEqual(response.data['criatura'], dados_serializados['criatura'])
        self.assertEqual(response.data['titulo'], dados_serializados['titulo'])
        self.assertEqual(response.data['estoria'], dados_serializados['estoria'])
        self.assertEqual(response.data['fonte'], dados_serializados['fonte'])


    def test_verifica_requisicao_post_um_lenda(self):
        'Teste que verifica requisição POST para um Lenda'

        dados = {
            "criatura": 5,
            "titulo": "Titulo de Lenda Teste",
            "estoria": "Estoria de Lenda Teste",
            "fonte": "Fonte do Lenda Teste",
            "data_criacao": date.today()
        }        

        response = self.client.post(self.url, data=dados)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_verifica_requisicao_delete_um_lenda(self):
        '''Teste que verifica requisição DELETE para um Lenda'''

        response = self.client.delete(f'{self.url}{self.lenda_02.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_verifica_requisicao_put_um_lenda(self):
        '''Teste que verifica requisição PUT para um Lenda'''

        dados = {
            "criatura": 8,
            "titulo": "Titulo de Lenda Teste",
            "estoria": "Estoria de Lenda Teste",
            "fonte": "Fonte Lenda Teste",
            "data_criacao": date.today()
        }

        response = self.client.put(f'{self.url}{self.lenda_01.id}/', data=dados)

        self.assertEqual(response.status_code, status.HTTP_200_OK)