from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input-field'}), max_length=50)
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'input-field'}), max_length=50)
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'input-field'}), max_length=1000)
