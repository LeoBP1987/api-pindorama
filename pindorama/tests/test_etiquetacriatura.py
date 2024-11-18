from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date
from pindorama.models import EtiquetasCriaturas
from pindorama.serializers import EtiquetasCriaturasSerializer
from django.conf import settings
import os
import shutil

class EtiquetaCriaturasTestCase(APITestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):

        self.usuario = User.objects.get(username='leonardo')
        self.url = reverse('Etiquetas-list')
        self.client.force_authenticate(self.usuario)

        self.etiqueta_01 = EtiquetasCriaturas.objects.get(id=5)
        self.etiqueta_02 = EtiquetasCriaturas.objects.get(id=7)

        self.foto_teste = SimpleUploadedFile(
                name='test_image.jpg',
                content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\xff\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b',
                content_type='image/jpeg'
            )
        
    def tearDown(self):
        media_root = settings.MEDIA_ROOT
        if os.path.exists(media_root):
            shutil.rmtree(media_root)

    def test_verifica_requisicao_get_lista_etiquetas(self):
        'Teste que verifica requisição GET para lista de Etiqueta'

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verifica_requisicao_get_para_uma_etiqueta(self):
        'Teste que verifica requisição GET para uma Etiqueta'

        response = self.client.get(f'{self.url}{self.etiqueta_01.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        dados_etiqueta = self.etiqueta_01
        dados_serializados = EtiquetasCriaturasSerializer(dados_etiqueta).data

        self.assertEqual(response.data['id'], dados_serializados['id'])
        self.assertEqual(response.data['criatura'], dados_serializados['criatura'])
        self.assertEqual(response.data['etiqueta'], dados_serializados['etiqueta'])


    def test_verifica_requisicao_post_uma_etiqueta(self):
        'Teste que verifica requisição POST para uma Etiqueta'

        dados = {
            "criatura": 5,
            "etiqueta": "Teste",
            "data_criacao": date.today()
        }        

        response = self.client.post(self.url, data=dados)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_verifica_requisicao_delete_uma_etiqueta(self):
        '''Teste que verifica requisição DELETE para uma Etiqueta'''

        response = self.client.delete(f'{self.url}{self.etiqueta_02.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_verifica_requisicao_put_uma_etiqueta(self):
        '''Teste que verifica requisição PUT para uma Etiqueta'''

        dados = {
            "criatura": 8,
            "etiqueta": "Etiqueta",
            "data_criacao": date.today()
        }

        response = self.client.put(f'{self.url}{self.etiqueta_01.id}/', data=dados)

        self.assertEqual(response.status_code, status.HTTP_200_OK)