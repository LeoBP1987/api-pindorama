from django.urls import path, include
from rest_framework import routers
from pindorama.views import TipoViewSet, FormasViewSet, OrigensViewSet, CriaturasViewSet, \
                    AlbumCriaturasViewSet, LendasCriaturasViewSet, ListaAlbumPorCriaturaViewSet, \
                    ListaLendasPorCriaturaViewSet, CriaturasPorTipoViewSet, CriaturasPorFormaViewSet, \
                    CriaturasPorOrigemViewSet, EtiquetasCriaturasViewSet, ElementosViewSet, ListaEtiquetasPorCriaturaViewSet


router = routers.DefaultRouter()
router.register('tipos', TipoViewSet, basename='Tipos')
router.register('formas', FormasViewSet, basename='Formas')
router.register('origens', OrigensViewSet, basename='Origens')
router.register('criaturas', CriaturasViewSet, basename='Criaturas')
router.register('album', AlbumCriaturasViewSet, basename='Album')
router.register('lendas', LendasCriaturasViewSet, basename='Lendas')
router.register('etiquetas', EtiquetasCriaturasViewSet, basename='Etiquetas')
router.register('elementos', ElementosViewSet, basename='Elementos')


urlpatterns = [
    path('', include(router.urls)),
    path('album/<int:id>/criaturas/', ListaAlbumPorCriaturaViewSet.as_view()),
    path('lendas/<int:id>/criaturas/', ListaLendasPorCriaturaViewSet.as_view()),
    path('etiquetas/<int:id>/criaturas/', ListaEtiquetasPorCriaturaViewSet.as_view()),
    path('criaturas/<int:id>/tipo/', CriaturasPorTipoViewSet.as_view()),
    path('criaturas/<int:id>/forma/', CriaturasPorFormaViewSet.as_view()),
    path('criaturas/<int:id>/origem/', CriaturasPorOrigemViewSet.as_view())
]