from rest_framework import serializers
from pindorama.models import Tipos, Formas, Origens, Criaturas, AlbumCriaturas, LendasCriaturas

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
    class Meta:
        model = Criaturas
        fields = ('id', 'criatura', 'tipo', 'forma', 'origem', 'foto_perfil', 'descricao')

class AlbumCriaturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumCriaturas
        fields = ('id', 'criatura', 'fonte', 'foto')

class LendasCriaturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = LendasCriaturas
        fields = ('id', 'criatura', 'titulo', 'estoria', 'fonte')

class ListaAlbumPorCriaturaSerializer(serializers.ModelSerializer):
    nome_criatura = serializers.ReadOnlyField(source = 'criatura.criatura')
    foto = serializers.SerializerMethodField()
    fonte = serializers.SerializerMethodField()

    class Meta:
        model = AlbumCriaturas
        fields = ('nome_criatura', 'foto', 'fonte')

    def get_foto(self, obj):
        return obj.foto.url if obj.foto else None
    
    def get_fonte(self, obj):
        return obj.fonte
    
class ListaLendasPorCriaturasSerializer(serializers.ModelSerializer):
    nome_criatura = serializers.ReadOnlyField(source = 'criatura.criatura')
    titulo = serializers.SerializerMethodField()
    estoria = serializers.SerializerMethodField()
    fonte = serializers.SerializerMethodField()

    class Meta:
        model = LendasCriaturas
        fields = ('nome_criatura', 'titulo', 'estoria', 'fonte')

    def get_titulo(self, obj):
        return obj.titulo
    
    def get_estoria(self, obj):
        return obj.estoria
    
    def get_fonte(self, obj):
        return obj.fonte
    
class CriaturasPorTipoSerializers(serializers.ModelSerializer):
    criatura = serializers.SerializerMethodField()
    forma = serializers.ReadOnlyField(source = 'forma.forma')
    origem = serializers.ReadOnlyField(source = 'origem.origem')
    descricao = serializers.SerializerMethodField()
    foto_perfil = serializers.SerializerMethodField()

    class Meta:
        model = Criaturas
        fields = ('criatura', 'forma', 'origem', 'descricao', 'foto_perfil')

    def get_criatura(self, obj):
        return obj.criatura
    
    def get_descricao(self, obj):
        return obj.descricao
    
    def get_foto_perfil(self, obj):
        return obj.foto_perfil.url if obj.foto_perfil else None
    
class CriaturasPorFormaSerializers(serializers.ModelSerializer):
    criatura = serializers.SerializerMethodField()
    tipo = serializers.ReadOnlyField(source = 'tipo.tipo')
    origem = serializers.ReadOnlyField(source = 'origem.origem')
    descricao = serializers.SerializerMethodField()
    foto_perfil = serializers.SerializerMethodField()

    class Meta:
        model = Criaturas
        fields = ('criatura', 'tipo', 'origem', 'descricao', 'foto_perfil')

    def get_criatura(self, obj):
        return obj.criatura
    
    def get_descricao(self, obj):
        return obj.descricao
    
    def get_foto_perfil(self, obj):
        return obj.foto_perfil.url if obj.foto_perfil else None
    
class CriaturasPorOrigemSerializers(serializers.ModelSerializer):
    criatura = serializers.SerializerMethodField()
    tipo = serializers.ReadOnlyField(source = 'tipo.tipo')
    forma = serializers.ReadOnlyField(source = 'forma.forma')
    descricao = serializers.SerializerMethodField()
    foto_perfil = serializers.SerializerMethodField()

    class Meta:
        model = Criaturas
        fields = ('criatura', 'tipo', 'forma', 'descricao', 'foto_perfil')

    def get_criatura(self, obj):
        return obj.criatura
    
    def get_descricao(self, obj):
        return obj.descricao
    
    def get_foto_perfil(self, obj):
        return obj.foto_perfil.url if obj.foto_perfil else None