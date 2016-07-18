from django import forms
from .models import Product

publish_choices = (

    ('',''),
    ('publish','Publish'),
    ('draft','Draft')
)

class ProductAddForm(forms.Form):

    title = forms.CharField(label='Product Title')
    description = forms.CharField(widget=forms.Textarea(
        attrs={
                "class":"booklos-class",
                "placeholder":"description",
                "some-attr":"this",
        }
    ))
    price = forms.DecimalField()
    publish = forms.ChoiceField(choices=publish_choices,required=False)

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 1:
            raise forms.ValidationError("The price must be greater than 0")
        else:
            return price

class ProductModelForm(forms.ModelForm):

    
    description = forms.CharField(widget=forms.Textarea(
        attrs={
                "class":"booklos-class",
                "placeholder":"description",
                "some-attr":"this",
        }
    ))


    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
        ]

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 1:
            raise forms.ValidationError("The price must be greater than 0")
        else:
            return price
