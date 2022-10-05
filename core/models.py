from django.db import models

class ContatoModel(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome teste')
    idade = models.IntegerField()

    op = (('M', 'Masculino'),
          ('F', 'Feminino')
          )
    sexo = models.CharField(max_length=2, choices=op)
    foto = models.ImageField(upload_to='core/static/fotos', default=None)


    class Meta:
        verbose_name = 'Contato'


    def __str__(self):
        return self.nome