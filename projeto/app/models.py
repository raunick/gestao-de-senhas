from django.db import models
from django.contrib.auth.models import User

class BaseModelAuditoria(models.Model):
    usuario_criador = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='%(class)s_created',
    )
    usuario_criador_em = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    usuario_atualizador = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='%(class)s_updated',
    )
    usuario_atualizador_em = models.DateTimeField(auto_now=True,null=True, blank=True)
    inativado = models.BooleanField(default=False)
    inativado_em = models.DateTimeField(null=True, blank=True)
    inativado_por = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='%(class)s_disabled',
    )
    
    # Novo campo para rastrear exclusões
    excluido = models.BooleanField(default=False)
    excluido_em = models.DateTimeField(null=True, blank=True)
    excluido_por = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='%(class)s_deleted',
    )

    class Meta:
        abstract = True


class CategoriaComputador(BaseModelAuditoria):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Categoria de computadores" 


class Localizacao(BaseModelAuditoria):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Localizações" 


class Computador(BaseModelAuditoria):
    hostname = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaComputador, on_delete=models.PROTECT)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Computador'
        verbose_name_plural = 'Computadores'

class Fila(BaseModelAuditoria):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)  # Adicionando validação
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Fila'
        verbose_name_plural = 'Filas'

class Chamada(BaseModelAuditoria):
    computador = models.ForeignKey(Computador, on_delete=models.PROTECT)
    fila = models.ForeignKey(Fila, on_delete=models.PROTECT)
    senha = models.CharField(max_length=10)
    horario_entrada = models.DateTimeField(auto_now_add=True)
    horario_saida = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[("pendente", "Pendente"), ("atendida", "Atendida"), ("cancelada", "Cancelada")])

    def __str__(self):
        return f"Guiche: {self.Computador}, Fila: {self.fila}, Senha: {self.senha}, Status: {self.status}"

    class Meta:
        verbose_name = 'Chamada'
        verbose_name_plural = 'Chamadas'
