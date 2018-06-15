function plot_ts() {
    'use strict';

    var trace1 = {
        type:   "scatter",
        mode:   "lines",
        name:   symbol + " High",
        x:      dates,
        y:      d_h,
        line: {color: '#17BECF'}
    }

    var trace2 = {
        type:   "scatter",
        mode:   "lines",
        name:   symbol + " Low",
        x:      dates,
        y:      d_l,
        line: {color: '#7F7F7F'}
    }

    var layout = {
        margin: {
            l: 50, r: 50,
            b: 50, t: 50,
            pad: 0
        }
    };

    var data = [trace1, trace2]

    Plotly.newPlot('plot-ts', data, layout);
};

plot_ts();
