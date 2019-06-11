from alpha_vantage.timeseries import TimeSeries
from datetime import datetime

import os
import sys
import time

import pandas as pd

class Miner():
    symbols = []
    AV_API_KEY = None

    def __init__(self, symbols):
        self.symbols = symbols[:]
        self.AV_API_KEY = os.environ.get("AV_API_KEY")

    def save_data(self, dir="."):
        # Initialize time series object
        timeSeries = TimeSeries(key=self.AV_API_KEY, output_format='pandas')

        # Create directory if it doesn't exist
        if not os.path.exists(dir):
            os.mkdir(dir)

        # Save each symbol
        for symbol in self.symbols:
            try:
                # Get data
                data, meta = timeSeries.get_daily(symbol=symbol, outputsize='full')
                # Name file
                ofile = os.path.join(dir, symbol + "_" + str(datetime.today().strftime('%Y-%m-%d')))
                # Save pandas data
                data.to_csv(ofile)
                # Print some info
                print("Saved data for symbol {} to {}".format(symbol, ofile))
                print("-- standing by for 15 seconds")
                time.sleep(15)
            except Exception as e:
                print("-- error: could not access/save data for {}".format(symbol))

if __name__ == '__main__':
    m = Miner(sys.argv[1:])
    m.save_data("data")
