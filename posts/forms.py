from django import forms

class ContentForm(forms.Form):
    form_post = forms.CharField(widget = forms.TextInput)
