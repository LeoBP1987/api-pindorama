from rest_framework import viewsets, generics, filters
from pindorama.models import Tipos, Formas, Origens, Criaturas, AlbumCriaturas, LendasCriaturas, EtiquetasCriaturas, Elementos
from pindorama.serializers import TiposSerializer, FormasSerializer, OrigensSerializer, CriaturasSerializer, \
    AlbumCriaturasSerializer, LendasCriaturasSerializer, ListaAlbumPorCriaturaSerializer, \
    ListaLendasPorCriaturasSerializer, CriaturasPorTipoSerializers, CriaturasPorFormaSerializers, ListaEtiquetasPorCriaturaSerializer, \
    CriaturasPorOrigemSerializers, EtiquetasCriaturasSerializer, ElementosSerializer, ListaCriaturasPorEtiquetaSerializers
from django_filters.rest_framework import DjangoFilterBackend

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipos.objects.all().order_by('tipo')
    serializer_class = TiposSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['tipo', ]

class FormasViewSet(viewsets.ModelViewSet):
    queryset = Formas.objects.all().order_by('forma')
    serializer_class = FormasSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['forma', ]
    search_fields = ['forma', ]

class OrigensViewSet(viewsets.ModelViewSet):
    queryset = Origens.objects.all().order_by('origem')
    serializer_class = OrigensSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['origem', ]
    search_fields = ['origem', ]

class CriaturasViewSet(viewsets.ModelViewSet):
    queryset = Criaturas.objects.all().order_by('criatura')
    serializer_class = CriaturasSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['criatura', ]
    search_fields = ['criatura', 'tipo', 'forma', 'origem', ]

class EtiquetasCriaturasViewSet(viewsets.ModelViewSet):
    queryset = EtiquetasCriaturas.objects.all().order_by('criatura')
    serializer_class = EtiquetasCriaturasSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['criatura', ]
    search_fields = ['criatura', ]

class AlbumCriaturasViewSet(viewsets.ModelViewSet):
    queryset = AlbumCriaturas.objects.all().order_by('criatura')
    serializer_class = AlbumCriaturasSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['criatura', ]
    search_fields = ['criatura', ]

class LendasCriaturasViewSet(viewsets.ModelViewSet):
    queryset = LendasCriaturas.objects.all().order_by('titulo')
    serializer_class = LendasCriaturasSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['criatura', ]
    search_fields = ['criatura', ]

class ElementosViewSet(viewsets.ModelViewSet):
    queryset = Elementos.objects.all().order_by('elemento')
    serializer_class = ElementosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['elemento', ]
    search_fields = ['elemento', ]

class ListaAlbumPorCriaturaViewSet(generics.ListAPIView):
    
    def get_queryset(self):
        queryset = AlbumCriaturas.objects.filter(criatura_id=self.kwargs['id']).order_by('id')
        return queryset
    
    serializer_class = ListaAlbumPorCriaturaSerializer

class ListaLendasPorCriaturaViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = LendasCriaturas.objects.filter(criatura_id=self.kwargs['id']).order_by('id')
        return queryset
    
    serializer_class = ListaLendasPorCriaturasSerializer

class ListaEtiquetasPorCriaturaViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = EtiquetasCriaturas.objects.filter(criatura_id=self.kwargs['id']).order_by('id')
        return queryset
    
    serializer_class = ListaEtiquetasPorCriaturaSerializer

class CriaturasPorTipoViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = Criaturas.objects.filter(tipo_id=self.kwargs['id']).order_by('id')
        return queryset
    
    serializer_class = CriaturasPorTipoSerializers
    
class CriaturasPorFormaViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = Criaturas.objects.filter(forma_id=self.kwargs['id']).order_by('id')
        return queryset
    
    serializer_class = CriaturasPorFormaSerializers
    
class CriaturasPorOrigemViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = Criaturas.objects.filter(origem_id=self.kwargs['id']).order_by('id')
        return queryset
    
    serializer_class = CriaturasPorOrigemSerializers

class ListaCriaturasPorEtiquetasViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = EtiquetasCriaturas.objects.filter(etiqueta=self.kwargs['etiqueta']).order_by('id')
        return queryset
    
    serializer_class = ListaCriaturasPorEtiquetaSerializers