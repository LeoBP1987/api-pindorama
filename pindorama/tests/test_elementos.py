from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date
from pindorama.models import Elementos
from pindorama.serializers import ElementosSerializer
from django.conf import settings
import os
import shutil

class ElementosSerializerTestCase(APITestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):

        self.usuario = User.objects.get(username='leonardo')
        self.url = reverse('Elementos-list')
        self.client.force_authenticate(self.usuario)

        self.elemento_01 = Elementos.objects.get(id=5)
        self.elemento_02 = Elementos.objects.get(id=7)

        self.foto_teste = SimpleUploadedFile(
                name='test_image.jpg',
                content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\xff\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b',
                content_type='image/jpeg'
            )
        
    def tearDown(self):
        media_root = settings.MEDIA_ROOT
        if os.path.exists(media_root):
            shutil.rmtree(media_root)

    def test_verifica_requisicao_get_lista_elementos(self):
        'Teste que verifica requisição GET para lista de Elementos'

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verifica_requisicao_get_para_um_elemento(self):
        'Teste que verifica requisição GET para um Elemento'

        response = self.client.get(f'{self.url}{self.elemento_01.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        dados_elemento = self.elemento_01
        dados_serializados = ElementosSerializer(dados_elemento).data

        self.assertEqual(response.data['id'], dados_serializados['id'])
        self.assertEqual(response.data['elemento'], dados_serializados['elemento'])
        self.assertEqual(response.data['tipo'], dados_serializados['tipo'])
        self.assertEqual(response.data['descricao'], dados_serializados['descricao'])
        self.assertEqual(response.data['foto_elemento'].split('/testserver', 1)[1], dados_serializados['foto_elemento'])


    def test_verifica_requisicao_post_um_elemento(self):
        'Teste que verifica requisição POST para um Elemento'

        dados = {
            "elemento": "Nome elemento testes",
            "tipo": "Tipo elemento teste",
            "descricao": "Descrição Teste",
            "foto_elemento": self.foto_teste,
            "data_criacao": date.today()
        }        

        response = self.client.post(self.url, data=dados)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_verifica_requisicao_delete_um_elemento(self):
        '''Teste que verifica requisição DELETE para um Elemento'''

        response = self.client.delete(f'{self.url}{self.elemento_02.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_verifica_requisicao_put_um_elemento(self):
        '''Teste que verifica requisição PUT para um Elemento'''

        dados = {
            "elemento": "Nome Edição Teste",
            "tipo": "Tipo elemento teste",
            "descricao": "Descrição Edição Teste",
            "foto_elemento": self.foto_teste,
            "data_criacao": date.today()
        }

        response = self.client.put(f'{self.url}{self.elemento_01.id}/', data=dados)

        self.assertEqual(response.status_code, status.HTTP_200_OK)