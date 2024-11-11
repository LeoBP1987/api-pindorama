from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date
from pindorama.models import Criaturas, Tipos, Formas, Origens
from pindorama.serializers import CriaturasSerializer
from django.conf import settings
import os

class CriaturasTestCase(APITestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):

        self.usuario = User.objects.get(username='leonardo')
        self.url = reverse('Criaturas-list')
        self.client.force_authenticate(self.usuario)

        self.criatura_01 = Criaturas.objects.get(id=5)
        self.criatura_02 = Criaturas.objects.get(id=10)

        self.imagem_teste = SimpleUploadedFile(
                name='test_image.jpg',
                content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\xff\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b',
                content_type='image/jpeg'
            )
        
    def tearDown(self):
        media_root = settings.MEDIA_ROOT
        imagem_teste_caminho = os.path.join(media_root, 'test_image.jpg')
        if os.path.exists(imagem_teste_caminho):
            os.remove(imagem_teste_caminho)
    
    def test_verifica_requisicao_get_lista_criaturas(self):
        'Teste que verifica requisição GET para lista de Criaturas'

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verifica_requisicao_get_para_um_criatura(self):
        'Teste que verifica requisição GET para um Criatura'

        response = self.client.get(f'{self.url}{self.criatura_01.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        dados_criatura = self.criatura_01
        dados_serializados = CriaturasSerializer(dados_criatura).data

        self.assertEqual(response.data['id'], dados_serializados['id'])
        self.assertEqual(response.data['criatura'], dados_serializados['criatura'])
        self.assertEqual(response.data['tipo'], dados_serializados['tipo'])
        self.assertEqual(response.data['forma'], dados_serializados['forma'])
        self.assertEqual(response.data['origem'], dados_serializados['origem'])
        self.assertEqual(response.data['foto_perfil'], dados_serializados['foto_perfil'])
        self.assertEqual(response.data['descricao'], dados_serializados['descricao'])

    def test_verifica_requisicao_post_um_criatura(self):
        'Teste que verifica requisição POST para uma Criatura'

        self.tipo = Tipos.objects.get(id=1)
        self.forma = Formas.objects.get(id=3)
        self.origem = Origens.objects.get(id=5)

        dados = {
            "criatura": "Teste Criatura",
            "tipo": 1,
            "forma": 3,
            "origem": 5,
            "foto_perfil": self.imagem_teste,
            "descricao": "Reprehenderit nam a animi laborum id. Aliquid delectus minima non aperiam officiis. Consequatur qui maiores voluptatem ipsam iure libero.",
            "data_criacao": date.today()
        }        

        response = self.client.post(self.url, data=dados)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_verifica_requisicao_delete_uma_criatura(self):
        '''Teste que verifica requisição DELETE para uma Criatura'''

        response = self.client.delete(f'{self.url}{self.criatura_02.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_verifica_requisicao_put_uma_criatura(self):
        '''Teste que verifica requisição PUT para uma Criatura'''

        dados = {
            "criatura": "Teste Criatura PUT",
            "tipo": 3,
            "forma": 5,
            "origem": 7,
            "foto_perfil": self.imagem_teste,
            "descricao": "Reprehenderit nam a animi laborum id. Aliquid delectus minima non aperiam officiis. Consequatur qui maiores voluptatem ipsam iure libero.",
            "data_criacao": date.today()
        }

        response = self.client.put(f'{self.url}{self.criatura_01.id}/', data=dados)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
