from django.db import models
from unidecode import unidecode

class Tipos(models.Model):
    tipo = models.CharField(max_length=15)
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tipo
    
class Formas(models.Model):
    forma = models.CharField(max_length=20)
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.forma

class Origens(models.Model):
    origem = models.CharField(max_length=50)
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.origem
    
MODOS = (
    ('permanente', 'Permanente'),
    ('periodico', 'Periódico'),
    ('temporario', 'Temporário'),
    ('metamorfico', 'Metamórfico')
)
    
class Criaturas(models.Model):
    criatura = models.CharField(max_length=50)
    tipo = models.ForeignKey(
        to=Tipos,
        on_delete=models.CASCADE,
        related_name='tipos'
    )
    forma = models.ForeignKey(
        to=Formas,
        on_delete=models.CASCADE,
        related_name='formas'
    )
    origem = models.ForeignKey(
        to=Origens,
        on_delete=models.CASCADE,
        related_name='origens'
    )
    foto_perfil = models.ImageField(upload_to='foto_perfil/%Y/%m/%d', blank=True, null=True)
    descricao = models.TextField()
    modo = models.CharField(max_length=20, blank=True, null= True, choices=MODOS)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.criatura
    
def upload_to_album(instance, filename):

    cod = len(AlbumCriaturas.objects.filter(criatura=instance.criatura)) + 1
    nome_sem_acento = unidecode(instance.criatura.criatura).lower()
    nome = nome_sem_acento.replace(" ", "-")

    return f'album/{nome}/{nome}-{cod}{filename[-4:]}'

class EtiquetasCriaturas(models.Model):
    criatura = models.ForeignKey(
        to=Criaturas,
        on_delete=models.CASCADE,
        related_name='etiquetas'
    )
    etiqueta = models.CharField(max_length=20, blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.etiqueta
    
class AlbumCriaturas(models.Model):
    criatura = models.ForeignKey(
        to=Criaturas,
        on_delete=models.CASCADE,
        related_name='fotos'
    )
    foto = models.ImageField(upload_to=upload_to_album)
    fonte = models.CharField(max_length=100, blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.criatura.id

class LendasCriaturas(models.Model):
    criatura = models.ForeignKey(
        to=Criaturas,
        on_delete=models.CASCADE,
        related_name='lendas'
    )
    titulo = models.CharField(max_length=200)
    estoria = models.TextField()
    fonte = models.CharField(max_length=200)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Elementos(models.Model):
    elemento = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20)
    descricao = models.TextField()
    foto_elemento = models.ImageField(upload_to='foto_elemento/%Y/%m/%d')
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.elemento