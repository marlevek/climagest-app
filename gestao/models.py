from django.db import models


TIPO_PESSOA = [
    ('PF', 'Pessoa Física'),
    ('PJ', 'Pessoa Jurídica'),
]

class Cliente(models.Model):
    tipo = models.CharField(max_length=2, choices=TIPO_PESSOA)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nome 
    
