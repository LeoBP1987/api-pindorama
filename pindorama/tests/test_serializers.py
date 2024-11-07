from django.test import TestCase
from pindorama.models import Tipos, Formas, Origens, Criaturas, AlbumCriaturas, LendasCriaturas
from pindorama.serializers import TiposSerializer, FormasSerializer, OrigensSerializer, CriaturasSerializer, \
    AlbumCriaturasSerializer, LendasCriaturasSerializer, ListaAlbumPorCriaturaSerializer, \
    ListaLendasPorCriaturasSerializer, CriaturasPorTipoSerializers, CriaturasPorFormaSerializers, \
    CriaturasPorOrigemSerializers

class SerializerTiposTestCase(TestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):
        self.tipo = Tipos.objects.get(id=1)
        self.tipo.serializers = TiposSerializer(instance=self.tipo)

    def test_verifica_campos_serializados_de_tipos(self):
        'Teste que verifica os campos serializados do modelo Tipos'

        dados = self.tipo.serializers.data

        self.assertEqual(set(dados.keys()), set(['id', 'tipo', 'descricao']))

    def test_verifica_conteudos_serializados_de_tipo(self):
        'Teste que verifica o conteudo dos campos serializados do modelo Tipos'

        dados = self.tipo.serializers.data

        self.assertEqual(dados['id'], self.tipo.id)
        self.assertEqual(dados['tipo'], self.tipo.tipo)
        self.assertEqual(dados['descricao'], self.tipo.descricao)

class SerializerFormasTestCase(TestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):
        self.forma = Formas.objects.get(id=3)
        self.forma.serializers = FormasSerializer(instance=self.forma)

    def test_verifica_campos_serializados_de_formas(self):
        'Teste que verifica os campos serializados do modelo Formas'

        dados = self.forma.serializers.data

        self.assertEqual(set(dados.keys()), set(['id', 'forma', 'descricao']))

    def test_verifica_conteudos_serializados_de_formas(self):
        'Teste que verifica o conteudo dos campos serializados de Formas'

        dados = self.forma.serializers.data

        self.assertEqual(dados['id'], self.forma.id)
        self.assertEqual(dados['forma'], self.forma.forma)
        self.assertEqual(dados['descricao'], self.forma.descricao)

class SerializerOrigensTestCase(TestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):
        self.origem = Origens.objects.get(id=3)
        self.origem.serializers = OrigensSerializer(instance=self.origem)

    def test_verifica_campos_serializados_de_origens(self):
        'Teste que verifica os campos serializados do modelo Origens'

        dados = self.origem.serializers.data

        self.assertEqual(set(dados.keys()), set(['id', 'origem', 'descricao']))

    def test_verifica_conteudos_serializados_de_origens(self):
        'Teste que verifica o conteudo dos campos serializados de Origens'

        dados = self.origem.serializers.data

        self.assertEqual(dados['id'], self.origem.id)
        self.assertEqual(dados['origem'], self.origem.origem)
        self.assertEqual(dados['descricao'], self.origem.descricao)

class SerializerCriaturasTestCase(TestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):
        self.criatura = Criaturas.objects.get(id=5)
        self.criatura.serializers = CriaturasSerializer(instance=self.criatura)

    def test_verifica_campos_serializados_de_criaturas(self):
        'Teste que verifica os campos serializados de Criaturas'

        dados = self.criatura.serializers.data

        self.assertEqual(set(dados.keys()), set(['id', 'criatura', 'tipo', 'forma', 'origem', 'foto_perfil', 'descricao']))

    def test_verifica_conteudos_serializados_de_criaturas(self):
        'Teste que verifica o conteudo dos campos de Criaturas'

        dados = self.criatura.serializers.data

        self.assertEqual(dados['id'], self.criatura.id)
        self.assertEqual(dados['criatura'], self.criatura.criatura)
        self.assertEqual(dados['tipo'], self.criatura.tipo.id)
        self.assertEqual(dados['forma'], self.criatura.forma.id)
        self.assertEqual(dados['origem'], self.criatura.origem.id)
        self.assertEqual(dados['foto_perfil'], self.criatura.foto_perfil.url)
        self.assertEqual(dados['descricao'], self.criatura.descricao)

class SerializerAlbumCriaturasTestCase(TestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):
        self.album = AlbumCriaturas.objects.get(id=7)
        self.album.serializers = AlbumCriaturasSerializer(instance=self.album)

    def test_verifica_campos_serializados_de_album_criaturas(self):
        'Teste que verifica os campos serializados de Album Criaturas'

        dados = self.album.serializers.data

        self.assertEqual(set(dados.keys()), set(['id', 'criatura', 'fonte', 'foto']))

    def test_verifica_conteudo_serializados_de_album_criaturas(self):
        'Teste que verifica o conteudo dos campos serializados de Album Criaturas'

        dados = self.album.serializers.data

        self.assertEqual(dados['id'], self.album.id)
        self.assertEqual(dados['criatura'], self.album.criatura.id)
        self.assertEqual(dados['fonte'], self.album.fonte)
        self.assertEqual(dados['foto'], self.album.foto.url)

class SerializerLendasCriaturasTestCase(TestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):
        self.lendas = LendasCriaturas.objects.get(id=9)
        self.lendas.serializers = LendasCriaturasSerializer(instance=self.lendas)

    def test_verifica_campos_serializados_de_lendas_criaturas(self):
        'Teste que verifica os campos serializados de Lendas Criaturas'

        dados = self.lendas.serializers.data

        self.assertEqual(set(dados.keys()), set(['id', 'criatura', 'titulo', 'estoria', 'fonte']))

    def test_verifica_conteudo_serializados_de_lendas_criaturas(self):
        'Teste que verifica o conteudo dos campos serializados de Lendas Criaturas'

        dados =self.lendas.serializers.data

        self.assertEqual(dados['id'], self.lendas.id)
        self.assertEqual(dados['criatura'], self.lendas.criatura.id)
        self.assertEqual(dados['titulo'], self.lendas.titulo)
        self.assertEqual(dados['estoria'], self.lendas.estoria)
        self.assertEqual(dados['fonte'], self.lendas.fonte)

class SerializerListaAlbumPorCriaturaTestCase(TestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):
        self.album = AlbumCriaturas.objects.get(id=5)
        self.album.serializers = ListaAlbumPorCriaturaSerializer(instance=self.album)

    def test_verifica_campos_serializados_de_lista_album_por_criaturas(self):
        'Teste que verifica os campos serializados de Lista Album por Criaturas'

        dados = self.album.serializers.data

        self.assertEqual(set(dados.keys()), set(['nome_criatura', 'foto', 'fonte']))

    def test_verifica_conteudo_serializados_de_lista_album_por_criaturas(self):
        'Teste que verifica o conteudo dos campos serializados de Lista Album por Criaturas'

        dados = self.album.serializers.data

        self.assertEqual(dados['nome_criatura'], self.album.criatura.criatura)
        self.assertEqual(dados['foto'], self.album.foto.url)
        self.assertEqual(dados['fonte'], self.album.fonte)

class SerializerListaLendasPorCriaturasSerializer(TestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):
        self.lendas = LendasCriaturas.objects.get(id=9)
        self.lendas.serializers = ListaLendasPorCriaturasSerializer(instance=self.lendas)

    def test_verifica_campos_serializados_de_lista_lendas_por_criaturas(self):
        'Teste que verifica os campos serializados de Lista Lendas por Criaturas'

        dados = self.lendas.serializers.data

        self.assertEqual(set(dados.keys()), set(['nome_criatura', 'titulo', 'estoria', 'fonte']))

    def test_verifica_conteudo_serializados_de_lista_lendas_por_criaturas(self):
        'Teste que verifica o conteudo dos campos serializados de Lista Lendas por Criaturas'

        dados = self.lendas.serializers.data

        self.assertEqual(dados['nome_criatura'], self.lendas.criatura.criatura)
        self.assertEqual(dados['titulo'], self.lendas.titulo)
        self.assertEqual(dados['estoria'], self.lendas.estoria)
        self.assertEqual(dados['fonte'], self.lendas.fonte)

class SerializerCriaturasPorTipoTestCase(TestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):
        self.criatura = Criaturas.objects.get(id=5)
        self.criatura.serializers = CriaturasPorTipoSerializers(instance=self.criatura)

    def test_verifica_campos_serializados_de_criaturas_por_tipo(self):
        'Teste que verifica os campos serializados de Criaturas por Tipo'

        dados = self.criatura.serializers.data

        self.assertEqual(set(dados.keys()), set(['criatura', 'forma', 'origem', 'descricao', 'foto_perfil']))

    def test_verifica_conteudos_serializados_de_criaturas_por_tipo(self):
        'Teste que verifica o conteudo dos campos de Criaturas por Tipo'

        dados = self.criatura.serializers.data

        self.assertEqual(dados['criatura'], self.criatura.criatura)
        self.assertEqual(dados['forma'], self.criatura.forma.forma)
        self.assertEqual(dados['origem'], self.criatura.origem.origem)
        self.assertEqual(dados['descricao'], self.criatura.descricao)
        self.assertEqual(dados['foto_perfil'], self.criatura.foto_perfil.url)

class SerializerCriaturasPorFormaTestCase(TestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):
        self.criatura = Criaturas.objects.get(id=5)
        self.criatura.serializers = CriaturasPorFormaSerializers(instance=self.criatura)

    def test_verifica_campos_serializados_de_criaturas_por_forma(self):
        'Teste que verifica os campos serializados de Criaturas por Forma'

        dados = self.criatura.serializers.data

        self.assertEqual(set(dados.keys()), set(['criatura', 'tipo', 'origem', 'descricao', 'foto_perfil']))

    def test_verifica_conteudos_serializados_de_criaturas_por_forma(self):
        'Teste que verifica o conteudo dos campos de Criaturas por Forma'

        dados = self.criatura.serializers.data

        self.assertEqual(dados['criatura'], self.criatura.criatura)
        self.assertEqual(dados['tipo'], self.criatura.tipo.tipo)
        self.assertEqual(dados['origem'], self.criatura.origem.origem)
        self.assertEqual(dados['descricao'], self.criatura.descricao)
        self.assertEqual(dados['foto_perfil'], self.criatura.foto_perfil.url)

class SerializerCriaturasPorOrigemTestCase(TestCase):
    fixtures = ['dados_teste.json']

    def setUp(self):
        self.criatura = Criaturas.objects.get(id=5)
        self.criatura.serializers = CriaturasPorOrigemSerializers(instance=self.criatura)

    def test_verifica_campos_serializados_de_criaturas_por_origem(self):
        'Teste que verifica os campos serializados de Criaturas por Origem'

        dados = self.criatura.serializers.data

        self.assertEqual(set(dados.keys()), set(['criatura', 'tipo', 'forma', 'descricao', 'foto_perfil']))

    def test_verifica_conteudos_serializados_de_criaturas_por_origem(self):
        'Teste que verifica o conteudo dos campos de Criaturas por Origem'

        dados = self.criatura.serializers.data

        self.assertEqual(dados['criatura'], self.criatura.criatura)
        self.assertEqual(dados['tipo'], self.criatura.tipo.tipo)
        self.assertEqual(dados['forma'], self.criatura.forma.forma)
        self.assertEqual(dados['descricao'], self.criatura.descricao)
        self.assertEqual(dados['foto_perfil'], self.criatura.foto_perfil.url)