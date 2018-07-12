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

# Get symbol object from symbol and type
def get_symbol_object(type, symbol):
    type, symbol, slug = get_symbol_data(type + ":" + symbol)
    obj, created = Symbol.objects.get_or_create(
        type=type, symbol=symbol, slug=slug
    )
    return obj

# Get Symbol information
def get_symbol_data(symbol_verbose):
    type = symbol_verbose.split(':')[0]
    symbol = symbol_verbose.split(':')[1]
    slug = SLUG_MAP[type].format(symbol)
    return type, symbol, slug

# Check if symbol is tracked
def is_symbol_tracked(type, symbol, user):
    try:
        symbol = get_symbol_object(type, symbol)
    except:
        return False
    tracker = Investor.objects.get(user=user)
    return tracker in symbol.trackers.all()


## View methods
## NOTE:    These views cannot directly be called, and are only called through
##          stocks/views, crypto/views, etc. Thus, login_required is not necessary.

# Track symbol view
def track_symbol_view(request, type, symbol):
    symbol = get_symbol_object(type, symbol)
    tracker = Investor.objects.get(user=request.user)
    symbol.trackers.add(tracker)
    data = {}
    return JsonResponse(data)

# Track symbol view
def untrack_symbol_view(request, type, symbol):
    symbol = get_symbol_object(type, symbol)
    tracker = Investor.objects.get(user=request.user)
    symbol.trackers.remove(tracker)
    data = {}
    return JsonResponse(data)
