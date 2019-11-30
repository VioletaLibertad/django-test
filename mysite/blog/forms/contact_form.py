from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue',
                'placeholder': 'Tu nombre acá porfi',
                'class': 'test-input'
            }
        )
    )  # This is input
    email = forms.EmailField(max_length=254, help_text='Estúpida, tu correo idiota')
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(         # This is hidden input 4 internal use
        max_length=50,                # shows from which page user sent the msg
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write sth!')
