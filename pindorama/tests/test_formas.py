from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from rest_framework import status
from pindorama.models import Formas
from pindorama.serializers import FormasSerializer

class FormasTestCase(APITestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):
        self.usuario = User.objects.get(username='leonardo')
        self.url = reverse('Formas-list')
        self.client.force_authenticate(self.usuario)

        self.forma_01 = Formas.objects.get(id=5)
        self.forma_02 = Formas.objects.get(id=10)

    def test_verifica_requisicao_get_lista_formas(self):
        'Teste que verifica requisição GET para lista de Formas'

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verifica_requisicao_get_para_um_forma(self):
        'Teste que verifica requisição GET para um Forma'

        response = self.client.get(f'{self.url}{self.forma_01.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        dados_forma = self.forma_01
        dados_serializados = FormasSerializer(dados_forma).data

        self.assertEqual(response.data, dados_serializados)


    def test_verifica_requisicao_post_um_forma(self):
        'Teste que verifica requisição POST para um Forma'

        dados = {
            "forma": "Corporis vero.",
            "descricao": "Quae nihil doloribus itaque. Quibusdam repellat omnis eius numquam consequuntur dignissimos. Incidunt sed harum eius error fugiat unde similique. Veritatis corporis nemo vero ad.",
            "data_criacao": date.today()
        }        

        response = self.client.post(self.url, data=dados)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_verifica_requisicao_delete_um_forma(self):
        '''Teste que verifica requisição DELETE para um Forma'''

        response = self.client.delete(f'{self.url}{self.forma_02.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_verifica_requisicao_put_um_forma(self):
        '''Teste que verifica requisição PUT para um Forma'''

        dados = {
            "forma": "Nemo.",
            "descricao": "Sequi culpa eligendi sed illum saepe. Aliquid quae molestias. Libero earum vero cumque eligendi error nesciunt.",
            "data_criacao": date.today()
        }

        response = self.client.put(f'{self.url}{self.forma_01.id}/', data=dados)

        self.assertEqual(response.status_code, status.HTTP_200_OK)