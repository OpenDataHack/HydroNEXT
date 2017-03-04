from django.db import models
from django.utils.encoding import python_2_unicode_compatible

''' 
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
'''
class Option(models.Model):
    option_type = models.CharField(max_length=200)
    option_code = models.CharField(max_length=200)
    option_text = models.CharField(max_length=200)
    def __str__(self):
        return self.option_type + " "+ self.option_code

@python_2_unicode_compatible  # only if you need to support Python 2
class Localizacion(models.Model):
    lugar_id = models.CharField(max_length=200)
    lugar_ds = models.CharField(max_length=200)
    def __str__(self):
        return self.lugar_ds 
@python_2_unicode_compatible  # only if you need to support Python 2
class Coordenadas(models.Model):
    local_ref = models.ForeignKey(Localizacion, on_delete=models.CASCADE)
    latitud = models.DecimalField(max_digits=15, decimal_places=10)
    longitud = models.DecimalField(max_digits=15, decimal_places=10) 
    descripcion = models.CharField(max_length=200, null=True) 
    def return_coordenadas(self):
     return self.latitud + self.longitud
    def __str__(self):
        return self.descripcion


