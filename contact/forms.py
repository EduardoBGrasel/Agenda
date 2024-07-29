from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(
        attrs={
            'accept': 'image/*',

        }
    ))
    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'image'

    # VALIDAÇÕES

    def clean(self):
        cleand_data = self.cleaned_data
        first_name = cleand_data.get('first_name')
        last_name = cleand_data.get('last_name')
        msg = ValidationError('O primeiro nome não pode ser igual ao segundo',
                                           code='invalid')
        if first_name == last_name:
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError('Veio do add_error')
            )

    
        return first_name

class RegisterForm(UserCreationForm):
    ...