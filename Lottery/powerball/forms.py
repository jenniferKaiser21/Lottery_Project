from django import forms
from django.forms import ValidationError

class PurchaseTicketsForm(forms.Form):
    num_tickets = forms.IntegerField(help_text="How many tickets would you like to purchase?")
    
    def clean_num_tickets(self):
        data = self.cleaned_data
        
        try:
            data = int(data)
        except ValueError:
            raise ValidationError(('Invalid number. Must be an integer.'))
            
        return data