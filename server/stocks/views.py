from django.shortcuts import render
from django.conf import settings
from django.http import Http404

import json
import pandas
from alpha_vantage.timeseries import TimeSeries
from django.core.serializers.json import DjangoJSONEncoder

KEY = settings.AV_API_KEY

def printIfDebug(str):
    if settings.DEBUG:
        print(str)

def stock_index_view(request):
    context = {}
    return render(request, 'stocks/index.html', context)

def stock_default_view(request, symbol):
    # Convert symbol to upper case
    symbol = symbol.upper()

    # Initialize timeseries
    ts = TimeSeries(key=KEY, output_format='pandas')

    # Get data and metadata
    try:
        data, meta_data = ts.get_intraday(symbol=symbol,interval='1min')
    except:
        raise Http404("%s is not a valid symbol." % symbol)

    # Process data into json format
    data_dict = {}
    data_dict["dates"] = data.index.values.tolist()
    for column in data:
        data_dict[column] = data[column].values.tolist()

    # Get organization details
    try:
        info = settings.TICKER_DATA[symbol]
    except:
        info = {"Name": "", "Sector": "", "Industry": ""}
        print("Details not found for %s" % symbol)

    # Create context
    context = {
        'symbol': symbol,
        'data': json.dumps(data_dict, cls=DjangoJSONEncoder),
        # 'data': data,
        'info': info,
        'meta': meta_data
    }
    context.update(info)
    context.update(meta_data)
    return render(request, 'stocks/stock.html', context)
