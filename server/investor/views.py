from django.shortcuts import render
from django.http import JsonResponse

## View methods

# Registration
def investor_register_view(request):
    context = {}
    return render(request, 'investor/register.html', context)

# Track symbol view
def track_symbol_view(request, symbol):
    data = {
        'symbol':   symbol,
    }
    print(data)
    return JsonResponse(data)
