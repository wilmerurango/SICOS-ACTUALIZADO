from django import forms
from CostosCirugia.models import *

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = (
            '__all__'
        )

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'style':'width: 12rem;',
            })

        
class TipoProcedimientoForm(forms.ModelForm):
    class Meta:
        model = TipoProcedimiento
        fields = (
            '__all__'
        )

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
