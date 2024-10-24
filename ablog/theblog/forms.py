from django import forms
from .models import post, category, Comment


class formpost(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'author', 'category', 'body', 'snippet', 'header_image']
        labels = {
            'title': 'Título',
            'author': 'Autor',
            'category': 'Categoría',
            'body': 'Contenido',
            'snippet': 'Resumen',
            'header_image': 'Imagen de Encabezado',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget = forms.Select(
            choices=category.objects.all().values_list('name', 'name'),
            attrs={'class': 'form-control'}
        )


class editpost(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'author', 'body', 'snippet']
        labels = {
            'title': 'Título',
            'author': 'Autor',
            'body': 'Contenido',
            'snippet': 'Resumen',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        labels = {
            'name': 'Nombre',
            'body': 'Comentario',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

#nuevo...
class DateFilterForm(forms.Form):
    YEAR_CHOICES = [(year, year) for year in range(2020, 2025)]  # Cambia el rango de años según lo necesites
    MONTH_CHOICES = [
        (1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'),
        (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'),
        (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre'),
    ]

    month = forms.ChoiceField(choices=MONTH_CHOICES, required=True, label='Mes')
    year = forms.ChoiceField(choices=YEAR_CHOICES, required=True, label='Año')