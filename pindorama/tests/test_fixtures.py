from django.test import TestCase
from pindorama.models import Tipos, Formas, Origens, Criaturas, AlbumCriaturas, LendasCriaturas, EtiquetasCriaturas, Elementos

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
        etiqueta = EtiquetasCriaturas.objects.get(pk=9)
        elemento = Elementos.objects.get(pk=1)

        self.assertEqual(tipo.tipo, 'Ullam.')
        self.assertEqual(forma.descricao, 'Mollitia amet animi nisi. Deserunt labore deleniti. Eaque quo iure incidunt delectus nihil.')
        self.assertEqual(origem.origem, 'Odio perferendis.')
        self.assertEqual(criatura.tipo.id, 1)
        self.assertEqual(album.fonte, 'In perferendis.')
        self.assertEqual(lenda.data_criacao.strftime('%Y-%m-%d'), '2009-03-28')
        self.assertEqual(etiqueta.etiqueta, 'Quas odio ut sit.')
        self.assertEqual(elemento.descricao, 'Officiis corporis molestiae porro harum ullam optio. Excepturi culpa quidem ducimus tenetur voluptatum. Nostrum ad quis dolorem hic.\nSuscipit ad porro veniam accusamus a veniam. In hic eius vitae.')