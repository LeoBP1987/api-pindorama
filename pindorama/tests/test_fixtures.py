from django.test import TestCase
from pindorama.models import Tipos, Formas, Origens, Criaturas, AlbumCriaturas, LendasCriaturas

class FixturesTests(TestCase):

    fixtures = ['dados_teste.json']

    def test_carregamento_fixtures(self):
        '''Teste de carregamento de Fixture'''

        tipo = Tipos.objects.get(pk=3)
        forma = Formas.objects.get(pk=7)
        origem = Origens.objects.get(pk=5)
        criatura = Criaturas.objects.get(pk=10)
        album = AlbumCriaturas.objects.get(pk=2)
        lenda = LendasCriaturas.objects.get(pk=5)

        self.assertEqual(tipo.tipo, 'Sit.')
        self.assertEqual(forma.descricao, 'Iste nihil officia assumenda. Dolores quas itaque officia a placeat eum eum.\nCum delectus aperiam quis quos quos. Modi ad laboriosam sit eveniet natus.')
        self.assertEqual(origem.origem, 'Sapiente optio quas.')
        self.assertEqual(criatura.tipo.id, 2)
        self.assertEqual(album.fonte, 'Ipsum laborum.')
        self.assertEqual(lenda.data_criacao.strftime('%Y-%m-%d'), '2020-03-27')