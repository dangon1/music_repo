from django.db import models

# Create your models here.

class EstiloMusical(models.Model):
	nome = models.CharField(max_length=255)

	def __str__(self):
		return self.nome

class Musico(models.Model):
	nome = models.CharField(max_length=255)
	cpf = models.BigIntegerField()
	salario = models.DecimalField(max_digits = 10,decimal_places = 2)
	data_nasc = models.DateField()

	def __str__(self):
		return self.nome + " " + str(self.cpf) + " " + str(self.data_nasc) + " " + str(self.salario)

class Banda(models.Model):
	nome = models.CharField(max_length=255)
	estilo_musical = models.ForeignKey(EstiloMusical, on_delete = models.CASCADE)
	musicos = models.ManyToManyField(Musico)

	def _nome_musicos(self):
		nomes = ""
		for musico in self.musicos:
			nomes += musico.nome

		return nomes

	def __str__(self):
		return self.nome + " Estilo: " + str(self.estilo_musical) + " Musicos: " + str(self.musicos)