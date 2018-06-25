from django.shortcuts import render
from django.conf import settings
from django.http import Http404
from django.contrib.auth.decorators import login_required

import json
import pandas
from alpha_vantage.timeseries import TimeSeries
from django.core.serializers.json import DjangoJSONEncoder

## Global Constants
KEY = settings.AV_API_KEY
TS = TimeSeries(key=KEY, output_format='pandas')
DEFAULT_TS_FORMAT = 'daily'


## TimeSeries maps

# Map timeseries format to functions
TS_MAP = {
    'intraday': TS.get_intraday,
    'daily':    TS.get_daily,
    'weekly':   TS.get_weekly,
    'monthly':  TS.get_monthly,
}

# Map timeseries format to default kwargs
TS_KWARGS_MAP = {
    'intraday': {'interval': '1min'}
}


## Helper methods

# Get organization information from stock symbol
def get_stock_info(symbol):
    try:
        info = settings.TICKER_DATA[symbol]
    except:
        info = {'Name': '', 'Sector': '', 'Industry': ''}
        print("Details not found for %s" % symbol)
    return info

# Get json data for JS from pandas dataframe
def get_json_data(data):
    data_dict = {}
    data_dict['dates'] = data.index.values.tolist()
    for column in data:
        data_dict[column] = data[column].values.tolist()
    return data_dict


## View methods

# Main dashboard
@login_required
def stock_index_view(request):
    context = {}
    return render(request, 'stocks/index.html', context)

# Time series views
@login_required
def stock_timeseries_view(request, symbol, format):
    symbol = symbol.upper()

    if format not in TS_MAP:
        format = DEFAULT_TS_FORMAT
    # Get data and metadata
    print(symbol, format)
    try:
        kwargs = {'symbol': symbol}
        if format in TS_KWARGS_MAP:
            kwargs.update(TS_KWARGS_MAP[format])
        data, meta_data = TS_MAP[format](**kwargs)
    except:
        raise Http404("%s is not a valid symbol or %s is not a valid format" % (symbol, format))

    # Process data into json format and get organization details
    data_dict   = get_json_data(data)
    info        = get_stock_info(symbol)

    # Create context
    context = {
        'format': format,
        'symbol': symbol,
        'data': json.dumps(data_dict, cls=DjangoJSONEncoder),
    }
    context.update(info)
    context.update(meta_data)
    return render(request, 'stocks/timeseries.html', context)

# Time series default view
@login_required
def stock_timeseries_default(request, symbol):
    return stock_timeseries_view(request, symbol, DEFAULT_TS_FORMAT)
