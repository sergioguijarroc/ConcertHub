from django import forms
from .models import Concierto, Artista


class ConciertoForm(forms.ModelForm):
    class Meta:
        model = Concierto
        fields = [
            "nombre",
            "artista_concierto",
            "ubicacion_concierto",
            "fecha",
            "precio_entrada",
            "descripcion",
            "foto",
        ]
        labels = {
            "nombre": "Nombre del concierto",
            "artista_concierto": "Artista",
            "ubicacion_concierto": "Ubicación",
            "fecha": "Fecha",
            "precio_entrada": "Precio de entrada",
            "descripcion": "Descripción",
            "foto": "Foto",
        }
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del concierto"}
            ),
            "artista_concierto": forms.Select(attrs={"class": "form-control"}),
            "ubicacion_concierto": forms.Select(attrs={"class": "form-control"}),
            "fecha": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "precio_entrada": forms.NumberInput(
                attrs={"class": "form-control", "min": 0}
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Descripción del concierto",
                }
            ),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
        }


class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = [
            "nombre",
            "genero",
            "descripcion",
            "foto",
        ]
        labels = {
            "nombre": "Nombre del artista",
            "genero": "Género",
            "descripcion": "Descripción",
            "foto": "Foto",
        }
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del artista"}
            ),
            "genero": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Género del artista"}
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Descripción del artista",
                }
            ),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
        }
