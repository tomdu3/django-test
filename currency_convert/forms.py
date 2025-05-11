from django import forms

class CurrencyConversionForm(forms.Form):
    amount = forms.FloatField(
        label='Amount',
        min_value=0.01,  # Add minimum value validation
        widget=forms.NumberInput(attrs={'step': '0.01'})  # for decimal input
    )
    
    # Define choices once to avoid repetition
    CURRENCY_CHOICES = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP')
    ]
    
    from_currency = forms.ChoiceField(
        choices=CURRENCY_CHOICES,
        label='From Currency'
    )
    
    to_currency = forms.ChoiceField(
        choices=CURRENCY_CHOICES,
        label='To Currency'
    )