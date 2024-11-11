from django.test import TestCase
from pindorama.models import Tipos, Formas, Origens, Criaturas, AlbumCriaturas, LendasCriaturas
from datetime import date
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from unidecode import unidecode
import os
import shutil

def cria_instancias_sem_imagens(self):
    self.tipo = Tipos.objects.create(
            tipo = 'TipoTeste',
            descricao = 'Descrição de Tipo Teste',
            data_criacao = date.today()
        )
    self.forma = Formas.objects.create(
        forma = 'FormaTeste',
        descricao = 'Descrição de Forma Teste',
        data_criacao = date.today()
    )
    self.origem = Origens.objects.create(
        origem = 'OrigemTeste',
        descricao = 'Descrição de Origem Teste',
        data_criacao = date.today()       
    )

    return {'tipo':self.tipo, 'forma':self.forma, 'origem':self.origem}

def cria_instancias_de_criatura(self):
    instancias = cria_instancias_sem_imagens(self)

    self.criatura = Criaturas.objects.create(
        criatura = 'CriaturaTeste',
        tipo = instancias['tipo'],
        forma = instancias['forma'],
        origem = instancias['origem'],
        foto_perfil = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\xff\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b',
            content_type='image/jpeg'
        ),
        descricao = 'Descrição de Criaturas Teste',
        data_criacao = date.today()
    )

    return self.criatura



class ModelTiposTestCase(TestCase):
    def setUp(self):
        instancias = cria_instancias_sem_imagens(self)   
        self.tipo = instancias['tipo']

    def test_verifica_atributos_modelo_tipos(self):
        'Teste que verifica atributos do modelo Tipos'

        self.assertEqual(self.tipo.tipo, 'TipoTeste')
        self.assertEqual(self.tipo.descricao, 'Descrição de Tipo Teste')
        self.assertEqual(self.tipo.data_criacao, date.today())

class ModelFormasTestCase(TestCase):
    def setUp(self):
        instancias = cria_instancias_sem_imagens(self)   
        self.forma = instancias['forma']

    def test_verifica_atributos_modelo_formas(self):
        'Teste que verifica atributos do modelo Formas'

        self.assertEqual(self.forma.forma, 'FormaTeste')
        self.assertEqual(self.forma.descricao, 'Descrição de Forma Teste')
        self.assertEqual(self.forma.data_criacao, date.today())

class ModelOrigensTestCase(TestCase):
    def setUp(self):
        instancias = cria_instancias_sem_imagens(self)   
        self.origem = instancias['origem']

    def test_verifica_atributos_modelo_origens(self):
        'Teste que verifica atributos do modelo Origens'

        self.assertEqual(self.origem.origem, 'OrigemTeste')
        self.assertEqual(self.origem.descricao, 'Descrição de Origem Teste')
        self.assertEqual(self.origem.data_criacao, date.today())

class ModelCriaturasTestCase(TestCase):
    def setUp(self):
        self.criatura = cria_instancias_de_criatura(self)

    def tearDown(self):
        media_root = settings.MEDIA_ROOT
        hoje = date.today()
        diretorio_image = f'{media_root}\\foto_perfil\\{hoje.year}\\{str(hoje.month).zfill(2)}\\{str(hoje.day).zfill(2)}\\'
        nome_arquivo = os.path.basename(self.criatura.foto_perfil.name)
        imagem_teste_caminho = os.path.join(diretorio_image, nome_arquivo)
        if os.path.exists(imagem_teste_caminho):
            os.remove(imagem_teste_caminho)

    def test_verifica_atributos_modelo_criaturas(self):
        'Teste que verifica atributos do modelo de Criaturas'

        hoje = date.today()
        caminho_esperado_prefixo = f'foto_perfil/{hoje.year}/{str(hoje.month).zfill(2)}/{str(hoje.day).zfill(2)}/test_image'

        self.assertEqual(self.criatura.criatura, 'CriaturaTeste')
        self.assertEqual(self.criatura.tipo.tipo, 'TipoTeste')
        self.assertEqual(self.criatura.forma.forma, 'FormaTeste')
        self.assertEqual(self.criatura.origem.origem, 'OrigemTeste')
        self.assertTrue(self.criatura.foto_perfil.name.startswith(caminho_esperado_prefixo))
        self.assertEqual(self.criatura.descricao, 'Descrição de Criaturas Teste')
        self.assertEqual(self.criatura.data_criacao, date.today())

class ModelAlbumCriaturasTestCase(TestCase):
    def setUp(self):

        self.criatura = cria_instancias_de_criatura(self)

        self.album = AlbumCriaturas.objects.create(
            criatura = self.criatura,
            foto = SimpleUploadedFile(
                name='foto_teste.jpg',
                content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\xff\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b',
                content_type='image/jpeg'
            ),
            fonte = 'Fonte da Foto Teste',
            data_criacao = date.today()
        )

    def tearDown(self):
        media_root = settings.MEDIA_ROOT
        hoje = date.today()
        diretorio_image = f'{media_root}\\foto_perfil\\{hoje.year}\\{str(hoje.month).zfill(2)}\\{str(hoje.day).zfill(2)}\\'
        nome_arquivo = os.path.basename(self.criatura.foto_perfil.name)
        imagem_teste_caminho = os.path.join(diretorio_image, nome_arquivo)
        if os.path.exists(imagem_teste_caminho):
            os.remove(imagem_teste_caminho)

        nome_arquivo = unidecode(self.criatura.criatura).lower()
        diretorio_foto = f'{media_root}\\album\\{nome_arquivo}'
        if os.path.exists(diretorio_foto):
            shutil.rmtree(diretorio_foto)

    def test_verifica_atributos_modelo_album_criaturas(self):
        'Teste que verifica atributos do modelo de Album Criaturas'

        caminho_esperado_prefixo = f'album/{self.criatura.criatura.lower()}/{self.criatura.criatura.lower()}'

        print(caminho_esperado_prefixo)
        print(self.album.foto.name)

        self.assertEqual(self.album.criatura.criatura, 'CriaturaTeste')
        self.assertTrue(self.album.foto.name.startswith(caminho_esperado_prefixo))
        self.assertEqual(self.album.fonte, 'Fonte da Foto Teste')
        self.assertEqual(self.album.data_criacao, date.today())

class ModelLendasCriaturasTestCase(TestCase):
    def setUp(self):
        self.criatura = cria_instancias_de_criatura(self)

        self.lendas = LendasCriaturas.objects.create(
            criatura = self.criatura,
            titulo = 'Titulo da lenda teste',
            estoria = 'Teste de lenda teste',
            fonte = 'Teste fonte lenda',
            data_criacao = date.today()
        )

    def tearDown(self):
        media_root = settings.MEDIA_ROOT
        hoje = date.today()
        diretorio_image = f'{media_root}\\foto_perfil\\{hoje.year}\\{str(hoje.month).zfill(2)}\\{str(hoje.day).zfill(2)}\\'
        nome_arquivo = os.path.basename(self.criatura.foto_perfil.name)
        imagem_teste_caminho = os.path.join(diretorio_image, nome_arquivo)
        if os.path.exists(imagem_teste_caminho):
            os.remove(imagem_teste_caminho)

    def test_verifica_atributos_modelo_lendas_criaturas(self):
        'Teste que verifica os atributos do modelo de Lendas das Criaturas'

        self.assertEqual(self.lendas.criatura.criatura, 'CriaturaTeste')
        self.assertEqual(self.lendas.titulo, 'Titulo da lenda teste')
        self.assertEqual(self.lendas.estoria, 'Teste de lenda teste')
        self.assertEqual(self.lendas.fonte, 'Teste fonte lenda')
        self.assertEqual(self.lendas.data_criacao, date.today())