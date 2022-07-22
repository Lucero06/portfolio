from django import forms



class MailForm(forms.Form):
    required_css_class = 'required'
    
    name=forms.CharField(label='Tu nombre', max_length=300, required=True)
    mail=forms.EmailField(label='Tu correo:', required=True)
    cellphone_number=forms.CharField(label='Núm. de Celular', max_length=20, required=False)
    phone_number=forms.CharField(label='Núm. Tel. Fijo', max_length=20, required=False)
    body=forms.CharField(label='Mensaje:', max_length=350, required=True, widget=forms.Textarea)
    
    
