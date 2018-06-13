from django.shortcuts import render

def stock_index_view(request):
    context = {}
    render(request, 'stocks/index.html', context)

def stock_default_view(request, symbol):
    context = {
        'symbol': symbol,
    }
    render(request, 'stocks/stock.html', context)
