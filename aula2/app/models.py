from django.db import models

# Create your models here.

class Departamento(models.Model):
    sigla = models.CharField(max_length=6)
    descricao = models.CharField(max_length=30)


class Salario(models.Model):
    valor = models.FloatField(null=True)


class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    idade = models.IntegerField(null=True)
    nacionalidade = models.CharField(max_length=30)

    def __str__(self):
        return smart_str('%s %s' % (self.nome, self.sobrenome))

    depto_atual = models.ForeignKey(
        Departamento,
        on_delete=models.RESTRICT,
        null=True)
    hist_deptos = models.ManyToManyField(
        Departamento,
        related_name="hist_pessoa_depto"
    )
    hist_salarios = models.ManyToManyField(
        Salario,
        related_name="hist_pessoa_salario"
    )
    depto_chefia = models.OneToOneField(
        Departamento,
        on_delete=models.RESTRICT,
        null=True,
        related_name='chefia_depto',
    )

    SENIORIDADE_CHOICES = [
        ('T', 'Trainee'),
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior'),
    ]

    senioridade = models.CharField(
        max_length=1,
        choices=SENIORIDADE_CHOICES,
        default='T'
    )

    ESCOLARIDADE_CHOICES = [
        ('NI', 'Não informado'),
        ('EF', 'Ensino Fundamental'),
        ('EM', 'Ensino Médio'),
        ('ES', 'Ensino Superior'),
    ]

    escolaridade = models.CharField(
        max_length=2,
        choices=ESCOLARIDADE_CHOICES,
        default='NI'
    )



class OrdenarPessoa(Pessoa):
    class Meta:
        ordering = ["nome"]
        proxy = True
