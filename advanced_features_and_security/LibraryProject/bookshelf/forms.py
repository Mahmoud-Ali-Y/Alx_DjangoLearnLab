from django import forms
class ExampleForm(forms.Form):
   title = forms.CharField()
   description = forms.CharField()