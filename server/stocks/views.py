from django.shortcuts import render
from django.conf import settings
from django.http import Http404

import pandas
from alpha_vantage.timeseries import TimeSeries

KEY = settings.AV_API_KEY

def stock_index_view(request):
    context = {}
    return render(request, 'stocks/index.html', context)

def stock_default_view(request, symbol):
    # Convert symbol to upper case
    symbol = symbol.upper()
    # Initialize Time Series
    # ts = TimeSeries(key=KEY, output_format='pandas')
    ts = TimeSeries(key=KEY, output_format='json')
    # Get Data and Meta Data
    try:
        data, meta_data = ts.get_intraday(symbol=symbol,interval='60min', outputsize='full')
    except:
        raise Http404("%s is not a valid symbol." % symbol)
    # Create context
    context = {
        'symbol': symbol,
        'data': data,
        'meta_data': meta_data,
    }
    return render(request, 'stocks/stock.html', context)
