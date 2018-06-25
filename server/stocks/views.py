from django.shortcuts import render
from django.conf import settings
from django.http import Http404

import json
import pandas
from alpha_vantage.timeseries import TimeSeries
from django.core.serializers.json import DjangoJSONEncoder

# Get API Key
KEY = settings.AV_API_KEY


# Initialize timeseries
TS = TimeSeries(key=KEY, output_format='pandas')


# Function maps
TS_MAP = {
    "intraday": TS.get_intraday,
}

ARGS_MAP = {
    "intraday": {"interval": "1min"}
}


# Generic helper methods
def get_stock_info(symbol):
    try:
        info = settings.TICKER_DATA[symbol]
    except:
        info = {"Name": "", "Sector": "", "Industry": ""}
        print("Details not found for %s" % symbol)
    return info

def get_json_data(data):
    data_dict = {}
    data_dict["dates"] = data.index.values.tolist()
    for column in data:
        data_dict[column] = data[column].values.tolist()
    return data_dict


# View methods
def stock_index_view(request):
    context = {}
    return render(request, 'stocks/index.html', context)

def stock_timeseries_view(request, symbol):
    symbol = symbol.upper()

    # Get data and metadata
    format = "intraday"
    try:
        kwargs = {"symbol": symbol}
        kwargs.update(ARGS_MAP[format])
        data, meta_data = TS_MAP[format](**kwargs)
    except:
        raise Http404("%s is not a valid symbol." % symbol)

    # Process data into json format and get organization details
    data_dict   = get_json_data(data)
    info        = get_stock_info(symbol)

    # Create context
    context = {
        'symbol': symbol,
        'data': json.dumps(data_dict, cls=DjangoJSONEncoder),
    }
    context.update(info)
    context.update(meta_data)
    print(meta_data)
    return render(request, 'stocks/stock.html', context)
