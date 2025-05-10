import os
from django.shortcuts import render
from .forms import CurrencyConversionForm
import requests

def currency_convert(request):
    form = CurrencyConversionForm(request.POST or None)  # Initialize form with POST data if available
    
    if request.method == 'POST':
        if form.is_valid():
            amount = form.cleaned_data['amount']
            from_currency = form.cleaned_data['from_currency']
            to_currency = form.cleaned_data['to_currency']

            # Get Exchangerates API
            API_KEY = os.getenv('EXCHANGERATES_API_ID')
            # Include both from and to currencies in the symbols parameter
            endpoint = f'https://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&symbols={from_currency},{to_currency}'
            
            try:
                response = requests.get(endpoint)
                response.raise_for_status()  # Raises an HTTPError for bad responses
                data = response.json()
                
                # Check if API returned successfully
                if not data.get('success', True):
                    raise ValueError(f"API error: {data.get('error', {}).get('info', 'Unknown error')}")
                
                # Get the rates
                rates = data.get('rates', {})
                
                # Check if both currencies are in the response
                if from_currency not in rates or to_currency not in rates:
                    raise ValueError("One or both currencies not found in API response")
                
                # Calculate conversion rate (convert from_currency to EUR, then EUR to to_currency)
                # Since the API uses EUR as base, we need to do this conversion
                eur_equivalent = amount / rates[from_currency]
                converted_amount = eur_equivalent * rates[to_currency]
                conversion_rate = (rates[to_currency] / rates[from_currency])

                context = {
                    'form': form,
                    'amount': amount,
                    'from_currency': from_currency,
                    'to_currency': to_currency,
                    'conversion_rate': conversion_rate,
                    'converted_amount': converted_amount,
                }
                
                return render(request, 'currency_convert/currency_convert.html', context)
            
            except (requests.RequestException, ValueError, KeyError) as e:
                # Handle API errors
                error_message = f"Error converting currency: {str(e)}"
                context = {
                    'form': form,
                    'error': error_message
                }
                return render(request, 'currency_convert/currency_convert.html', context)
    
    # GET request or form not valid
    context = {'form': form}
    return render(request, 'currency_convert/currency_convert.html', context)