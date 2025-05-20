from rest_framework import viewsets, generics, filters
from pindorama.models import Tipos, Formas, Origens, Criaturas, AlbumCriaturas, LendasCriaturas, EtiquetasCriaturas, Elementos
from pindorama.serializers import TiposSerializer, FormasSerializer, OrigensSerializer, CriaturasSerializer, \
    AlbumCriaturasSerializer, LendasCriaturasSerializer, ListaAlbumPorCriaturaSerializer, \
    ListaLendasPorCriaturasSerializer, CriaturasPorTipoSerializers, CriaturasPorFormaSerializers, ListaEtiquetasPorCriaturaSerializer, \
    CriaturasPorOrigemSerializers, EtiquetasCriaturasSerializer, ElementosSerializer, ListaCriaturasPorEtiquetaSerializers, LoginSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipos.objects.all().order_by('tipo')
    serializer_class = TiposSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering_fields = ['tipo', ]

class FormasViewSet(viewsets.ModelViewSet):
    queryset = Formas.objects.all().order_by('forma')
    serializer_class = FormasSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering_fields = ['forma', ]
    search_fields = ['forma', ]

class OrigensViewSet(viewsets.ModelViewSet):
    queryset = Origens.objects.all().order_by('origem')
    serializer_class = OrigensSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering_fields = ['origem', ]
    search_fields = ['origem', ]

class CriaturasViewSet(viewsets.ModelViewSet):
    queryset = Criaturas.objects.all().order_by('criatura')
    serializer_class = CriaturasSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering_fields = ['criatura', ]
    search_fields = ['criatura', 'tipo', 'forma', 'origem', ]

class EtiquetasCriaturasViewSet(viewsets.ModelViewSet):
    queryset = EtiquetasCriaturas.objects.all().order_by('criatura')
    serializer_class = EtiquetasCriaturasSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering_fields = ['criatura', ]
    search_fields = ['criatura', ]

class AlbumCriaturasViewSet(viewsets.ModelViewSet):
    queryset = AlbumCriaturas.objects.all().order_by('criatura')
    serializer_class = AlbumCriaturasSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering_fields = ['criatura', ]
    search_fields = ['criatura', ]

class LendasCriaturasViewSet(viewsets.ModelViewSet):
    queryset = LendasCriaturas.objects.all().order_by('titulo')
    serializer_class = LendasCriaturasSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering_fields = ['criatura', ]
    search_fields = ['criatura', ]

class ElementosViewSet(viewsets.ModelViewSet):
    queryset = Elementos.objects.all().order_by('elemento')
    serializer_class = ElementosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering_fields = ['elemento', ]
    search_fields = ['elemento', ]

class ListaAlbumPorCriaturaViewSet(generics.ListAPIView):
    
    def get_queryset(self):
        queryset = AlbumCriaturas.objects.filter(criatura_id=self.kwargs['id']).order_by('id')
        return queryset
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ListaAlbumPorCriaturaSerializer

class ListaLendasPorCriaturaViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = LendasCriaturas.objects.filter(criatura_id=self.kwargs['id']).order_by('id')
        return queryset
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ListaLendasPorCriaturasSerializer

class ListaEtiquetasPorCriaturaViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = EtiquetasCriaturas.objects.filter(criatura_id=self.kwargs['id']).order_by('id')
        return queryset
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ListaEtiquetasPorCriaturaSerializer

class CriaturasPorTipoViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = Criaturas.objects.filter(tipo_id=self.kwargs['id']).order_by('id')
        return queryset
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CriaturasPorTipoSerializers
    
class CriaturasPorFormaViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = Criaturas.objects.filter(forma_id=self.kwargs['id']).order_by('id')
        return queryset
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CriaturasPorFormaSerializers
    
class CriaturasPorOrigemViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = Criaturas.objects.filter(origem_id=self.kwargs['id']).order_by('id')
        return queryset
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CriaturasPorOrigemSerializers

class ListaCriaturasPorEtiquetasViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = EtiquetasCriaturas.objects.filter(etiqueta=self.kwargs['etiqueta']).order_by('id')
        return queryset
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ListaCriaturasPorEtiquetaSerializers

class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)

        print("Chamou")
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            })
        return Response(
            {'detail': 'Credenciais inválidas'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
class LogoutViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout realizado com sucesso!"}, status=200)
        except Exception as e:
            return Response({"error": "Token inválido ou já expirado."}, status=400)