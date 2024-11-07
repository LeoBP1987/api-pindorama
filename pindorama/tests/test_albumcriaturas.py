from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date
from pindorama.models import AlbumCriaturas
from pindorama.serializers import AlbumCriaturasSerializer

class AlbumCriaturasTestCase(APITestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):

        self.usuario = User.objects.get(username='leonardo')
        self.url = reverse('Album-list')
        self.client.force_authenticate(self.usuario)

        self.album_01 = AlbumCriaturas.objects.get(id=5)
        self.album_02 = AlbumCriaturas.objects.get(id=7)

        self.foto_teste = SimpleUploadedFile(
                name='test_image.jpg',
                content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\xff\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b',
                content_type='image/jpeg'
            )

    def test_verifica_requisicao_get_lista_albums(self):
        'Teste que verifica requisição GET para lista de Album'

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verifica_requisicao_get_para_um_album(self):
        'Teste que verifica requisição GET para um Album'

        response = self.client.get(f'{self.url}{self.album_01.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        dados_album = self.album_01
        dados_serializados = AlbumCriaturasSerializer(dados_album).data

        self.assertEqual(response.data['id'], dados_serializados['id'])
        self.assertEqual(response.data['criatura'], dados_serializados['criatura'])
        self.assertEqual(response.data['foto'].split('server')[1], dados_serializados['foto'])
        self.assertEqual(response.data['fonte'], dados_serializados['fonte'])


    def test_verifica_requisicao_post_um_album(self):
        'Teste que verifica requisição POST para um Album'

        dados = {
            "criatura": 5,
            "foto": self.foto_teste,
            "fonte": "Fonte do Album Teste",
            "data_criacao": date.today()
        }        

        response = self.client.post(self.url, data=dados)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_verifica_requisicao_delete_um_album(self):
        '''Teste que verifica requisição DELETE para um Album'''

        response = self.client.delete(f'{self.url}{self.album_02.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_verifica_requisicao_put_um_album(self):
        '''Teste que verifica requisição PUT para um Album'''

        dados = {
            "criatura": 8,
            "foto": self.foto_teste,
            "fonte": "Descrição Album Teste",
            "data_criacao": date.today()
        }

        response = self.client.put(f'{self.url}{self.album_01.id}/', data=dados)

        self.assertEqual(response.status_code, status.HTTP_200_OK)