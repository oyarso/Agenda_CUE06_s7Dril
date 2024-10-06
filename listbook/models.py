from django.db import models 
# Declaramos el nuevo modelo con el nombte de BoardsModel" 
class BoardsModel(models.Model): 
# Campos del modelo 
    titulo = models.CharField(max_length = 150) 
    autor = models.CharField(max_length = 150) 
    valoracion = models.IntegerField(range(0,10000)) 
def __str__(self): 
    return self.titulo