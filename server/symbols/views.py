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

# Get symbol object from verbose symbol
def get_symbol_object(symbol):
    type, symbol, slug = get_symbol_data(symbol)
    obj = Symbol.objects.get(
        type=type, symbol=symbol, slug=slug
    )
    return obj

# Get Symbol information
def get_symbol_data(symbol):
    type = symbol.split(':')[0]
    symbol = symbol.split(':')[1]
    slug = SLUG_MAP[type].format(symbol)
    return type, symbol, slug


## View methods

# Track symbol view
def track_symbol_view(request, symbol):
    symbol = get_symbol_object(symbol)
    tracker = Investor.objects.get(user=request.user)
    symbol.trackers.add(tracker)
    data = {}
    return JsonResponse(data)

# Track symbol view
def untrack_symbol_view(request, symbol):
    symbol = get_symbol_object(symbol)
    tracker = Investor.objects.get(user=request.user)
    symbol.trackers.remove(tracker)
    data = {}
    return JsonResponse(data)
