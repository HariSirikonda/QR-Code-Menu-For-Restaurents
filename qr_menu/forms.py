from django import forms

class QRCodeForm(forms.Form):
    restaurent_name = forms.CharField(
        max_length=100,
        label="Enter the restaurent name",
        widget=forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter restaurent name'
        })
    )
    URL = forms.URLField(
        max_length=100,
        label="Enter the restaurent name",
        widget=forms.URLInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'URL of your form menu'
        })
    )