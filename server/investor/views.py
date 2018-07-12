from django.shortcuts import render
from django.http import JsonResponse

from symbols.models import Symbol

## Maps
SLUG_MAP = {
    'stock': '/s/{}/',
    'crypto': '/c/{}/',
    'forex': '/f/{}/',
}


## Helper methods

# Get Symbol information
def get_symbol_data(symbol):
    type = symbol.split(':')[0]
    symbol = symbol.split(':')[1]
    slug = SLUG_MAP[type].format(symbol)
    return type, symbol, slug


## View methods

# Registration
def investor_register_view(request):
    context = {}
    return render(request, 'investor/register.html', context)

# Track symbol view
def track_symbol_view(request, symbol):
    type, symbol, slug = get_symbol_data(symbol)
    obj, created = Symbol.objects.get_or_create(
        type=type, symbol=symbol, slug=slug
    )
    data = {
        'symbol':   symbol,
        'created':  created,
    }
    print(created)
    return JsonResponse(data)
