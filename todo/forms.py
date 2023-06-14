from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ['is_done']
        widgets = {
            'details': forms.Textarea(attrs={
                'cols': 30,
                'rows': 3,
                'maxlength': 45
            }),
        }
        labels = {
            'title': 'Tytuł',
            'details': 'Opis',
            'date': 'Data',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def label_tag(self, contents=None, attrs=None, label_suffix=None):
        attrs = attrs or {}
        attrs['class'] = 'form-label'
        return super().label_tag(contents=contents, attrs=attrs, label_suffix=label_suffix)