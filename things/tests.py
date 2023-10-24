from django.test import TestCase

# Create your tests here.
def clean_quantity(self):
            quantity = self.cleaned_data.get('quantity')
            if quantity < 0:
                raise forms.ValidationError('Quantity must be a non-negative number.')
            return quantity
        
def clean_name(self):
        name = self.cleaned_data.get('name')
        if Thing.objects.filter(name=name).exists():
            raise forms.ValidationError('This name is already in use.')
        return name