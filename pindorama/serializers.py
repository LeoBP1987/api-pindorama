from rest_framework import serializers
from pindorama.models import Tipos, Formas, Origens, Criaturas, AlbumCriaturas, LendasCriaturas, EtiquetasCriaturas, Elementos
from pindorama.validators import nome_invalido

class TiposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipos
        fields = ('id', 'tipo', 'descricao')

class FormasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formas
        fields = ('id', 'forma', 'descricao')

class OrigensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origens
        fields = ('id', 'origem', 'descricao')

class CriaturasSerializer(serializers.ModelSerializer):
    tipo_nome = serializers.ReadOnlyField(source = 'tipo.tipo')
    forma_nome = serializers.ReadOnlyField(source = 'forma.forma')
    origem_nome = serializers.ReadOnlyField(source = 'origem.origem')

    class Meta:
        model = Criaturas
        fields = ('id', 'criatura', 'tipo', 'tipo_nome', 'forma', 'forma_nome', 'origem', 'origem_nome', 'foto_perfil', 'descricao', 'modo')    

class AlbumCriaturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumCriaturas
        fields = ('id', 'criatura', 'fonte', 'foto')

class LendasCriaturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = LendasCriaturas
        fields = ('id', 'criatura', 'titulo', 'estoria', 'fonte')

class EtiquetasCriaturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtiquetasCriaturas
        fields = ('id', 'criatura', 'etiqueta')

    def validate(self, dados):
        etiqueta = dados.get('etiqueta', None)

        if etiqueta is None or nome_invalido(dados['etiqueta']):
            raise serializers.ValidationError({'etiqueta':'A etiqueta não pode conter espaços e caracteres especiais.'})
        
        return dados

class ElementosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elementos
        fields = ('id', 'elemento', 'tipo', 'descricao', 'foto_elemento')


class ListaAlbumPorCriaturaSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    nome_criatura = serializers.ReadOnlyField(source = 'criatura.criatura')
    foto = serializers.SerializerMethodField()
    fonte = serializers.SerializerMethodField()

    class Meta:
        model = AlbumCriaturas
        fields = ('id', 'nome_criatura', 'foto', 'fonte')

    def get_id(self, obj):
        return obj.id

    def get_foto(self, obj):
        return obj.foto.url if obj.foto else None
    
    def get_fonte(self, obj):
        return obj.fonte
    
class ListaLendasPorCriaturasSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    nome_criatura = serializers.ReadOnlyField(source = 'criatura.criatura')
    titulo = serializers.SerializerMethodField()
    estoria = serializers.SerializerMethodField()
    fonte = serializers.SerializerMethodField()

    class Meta:
        model = LendasCriaturas
        fields = ('id', 'nome_criatura', 'titulo', 'estoria', 'fonte')

    def get_id(self, obj):
        return obj.id

    def get_titulo(self, obj):
        return obj.titulo
    
    def get_estoria(self, obj):
        return obj.estoria
    
    def get_fonte(self, obj):
        return obj.fonte
    
class ListaEtiquetasPorCriaturaSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    nome_criatura = serializers.ReadOnlyField(source = 'criatura.criatura')
    etiqueta = serializers.SerializerMethodField()

    class Meta:
        model = AlbumCriaturas
        fields = ('id', 'nome_criatura', 'etiqueta')

    def get_etiqueta(self, obj):
        return obj.etiqueta
    
    def get_id(self, obj):
        return obj.id
    
class CriaturasPorTipoSerializers(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    criatura = serializers.SerializerMethodField()
    tipo_nome = serializers.ReadOnlyField(source = 'tipo.tipo')
    forma_nome = serializers.ReadOnlyField(source = 'forma.forma')
    origem_nome = serializers.ReadOnlyField(source = 'origem.origem')
    descricao = serializers.SerializerMethodField()
    foto_perfil = serializers.SerializerMethodField()

    class Meta:
        model = Criaturas
        fields = ('id', 'criatura', 'tipo_nome', 'forma_nome', 'origem_nome', 'descricao', 'foto_perfil')

    def get_id(self, obj):
        return obj.id

    def get_criatura(self, obj):
        return obj.criatura
    
    def get_descricao(self, obj):
        return obj.descricao
    
    def get_foto_perfil(self, obj):
        return obj.foto_perfil.url if obj.foto_perfil else None
    
class CriaturasPorFormaSerializers(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    criatura = serializers.SerializerMethodField()
    tipo_nome = serializers.ReadOnlyField(source = 'tipo.tipo')
    forma_nome = serializers.ReadOnlyField(source = 'forma.forma')
    origem_nome = serializers.ReadOnlyField(source = 'origem.origem')
    descricao = serializers.SerializerMethodField()
    foto_perfil = serializers.SerializerMethodField()

    class Meta:
        model = Criaturas
        fields = ('id', 'criatura', 'tipo_nome', 'forma_nome', 'origem_nome', 'descricao', 'foto_perfil')

    def get_id(self, obj):
        return obj.id

    def get_criatura(self, obj):
        return obj.criatura
    
    def get_descricao(self, obj):
        return obj.descricao
    
    def get_foto_perfil(self, obj):
        return obj.foto_perfil.url if obj.foto_perfil else None
    
class CriaturasPorOrigemSerializers(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    criatura = serializers.SerializerMethodField()
    tipo_nome = serializers.ReadOnlyField(source = 'tipo.tipo')
    forma_nome = serializers.ReadOnlyField(source = 'forma.forma')
    origem_nome = serializers.ReadOnlyField(source = 'origem.origem')
    descricao = serializers.SerializerMethodField()
    foto_perfil = serializers.SerializerMethodField()

    class Meta:
        model = Criaturas
        fields = ('id', 'criatura', 'tipo_nome', 'forma_nome', 'origem_nome', 'descricao', 'foto_perfil')

    def get_criatura(self, obj):
        return obj.criatura
    
    def get_descricao(self, obj):
        return obj.descricao
    
    def get_foto_perfil(self, obj):
        return obj.foto_perfil.url if obj.foto_perfil else None
    
class ListaCriaturasPorEtiquetaSerializers(serializers.ModelSerializer):
    etiqueta = serializers.SerializerMethodField()
    criatura = serializers.ReadOnlyField(source = 'criatura.criatura')
    id = serializers.ReadOnlyField(source = 'criatura.id')
    tipo_nome = serializers.ReadOnlyField(source = 'criatura.tipo.tipo')
    forma_nome = serializers.ReadOnlyField(source = 'criatura.forma.forma')
    origem_nome = serializers.ReadOnlyField(source = 'criatura.origem.origem')
    foto_perfil = serializers.ReadOnlyField(source = 'criatura.foto_perfil.url')
    descricao = serializers.ReadOnlyField(source = 'criatura.descricao')
    modo = serializers.ReadOnlyField(source = 'criatura.modo')

    class Meta:
        model = AlbumCriaturas
        fields = ('etiqueta', 'criatura', 'id', 'tipo_nome', 'forma_nome', 'origem_nome', 'foto_perfil', 'descricao', 'modo')

    def get_etiqueta(self, obj):
        return obj.etiqueta
