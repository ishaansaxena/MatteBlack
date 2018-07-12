from django.shortcuts import render
from django.http import JsonResponse

from symbols.models import Symbol
from investor.models import Investor

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

# Track symbol view
def track_symbol_view(request, symbol):
    type, symbol, slug = get_symbol_data(symbol)
    obj, created = Symbol.objects.get_or_create(
        type=type, symbol=symbol, slug=slug
    )
    tracker = Investor.objects.get(user=request.user)
    obj.trackers.add(tracker)
    data = {
        'symbol':   symbol,
    }
    return JsonResponse(data)

# Track symbol view
def untrack_symbol_view(request, symbol):
    type, symbol, slug = get_symbol_data(symbol)
    obj = Symbol.objects.get(
        type=type, symbol=symbol, slug=slug
    )
    tracker = Investor.objects.get(user=request.user)
    obj.trackers.remove(tracker)
    data = {
        'symbol':   symbol,
    }
    return JsonResponse(data)
