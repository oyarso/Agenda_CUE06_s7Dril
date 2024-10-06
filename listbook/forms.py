from django import forms 
from .models import BoardsModel 


class WidgetForm(forms.Form): 
    Titulo = forms.CharField(max_length = 150) 
    Autor = forms.CharField(max_length = 150) 
    Valoracion = forms.IntegerField(min_value=0, max_value=10000)  

class BoardsForm(forms.ModelForm): 
# specify the name of model to use 
    class Meta: 
        model = BoardsModel 
        fields = "__all__" 